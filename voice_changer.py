import pyaudio
import subprocess
import numpy as np
from pydub import AudioSegment
from io import BytesIO

# Function to change pitch (simple example)
def change_pitch(data, octaves):
    audio = AudioSegment.from_raw(BytesIO(data), sample_width=2, frame_rate=44100, channels=1)
    new_sample_rate = int(audio.frame_rate * (2.0 ** octaves))
    new_audio = audio._spawn(audio.raw_data, overrides={'frame_rate': new_sample_rate})
    return new_audio.raw_data

# Setup PyAudio parameters
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 1024

# Initialize PyAudio
audio = pyaudio.PyAudio()

# Streaming and processing audio

# Initialize PyAudio
audio = pyaudio.PyAudio()

# Get the number of available input devices
num_devices = audio.get_device_count()

# Print the available input devices and their indices
for i in range(num_devices):
    device_info = audio.get_device_info_by_index(i)
    if device_info['maxInputChannels'] > 0:
        print(f"Device {i}: {device_info['name']}")

# Run the streaming function
stream()
def stream():
    # Open stream
    stream = audio.open(format=FORMAT, channels=CHANNELS,
                        rate=RATE, input=True,
                        output=True, frames_per_buffer=CHUNK, input_device_index=1)  # Change input_device_index to the appropriate microphone input index

    try:
        while True:
            # Read from stream
            data = stream.read(CHUNK)
            # Process audio
            modified_data = change_pitch(data, 1)  # Change pitch here
            # Play modified audio
            stream.write(modified_data)
    except KeyboardInterrupt:
        # Stop and close stream
        stream.stop_stream()
        stream.close()
        audio.terminate()

# Run the streaming function
stream()