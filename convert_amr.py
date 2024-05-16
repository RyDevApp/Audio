from pydub import AudioSegment

# Load your AMR file
amr_audio = AudioSegment.from_file("path/to/your/file.amr", format="amr")

# Convert to MP3
amr_audio.export("output_file.mp3", format="mp3")

# Or, Convert to WAV
amr_audio.export("output_file.wav", format="wav")
