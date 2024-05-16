from pydub import AudioSegment
amr_audio = AudioSegment.from_file(r"D:\Content\Music\Eternal Turtle\Blowfish.amr", format="amr")
amr_audio.export(r"output_file.wav", format="wav")