import pyaudio
import numpy as np

# Initialize PyAudio
pa = pyaudio.PyAudio()

# Set up audio stream
stream = pa.open(format=pyaudio.paInt16,
                 channels=1,
                 rate=44100,
                 input=True,
                 frames_per_buffer=1024)

# Read data from the stream
data = np.frombuffer(stream.read(1024), dtype=np.int16)
# Calculate the RMS (Root Mean Square) of the data
rms = np.sqrt(np.mean(np.square(data)))

# Convert RMS to decibels
db = 20 * np.log10(rms)
try:
    while True:
        data = np.frombuffer(stream.read(1024), dtype=np.int16)
        rms = np.sqrt(np.mean(np.square(data)))
        db = 20 * np.log10(rms)
        print(f"Decibel level: {db} dB")
except KeyboardInterrupt:
    print("\nStopping")

stream.stop_stream()
stream.close()
pa.terminate()