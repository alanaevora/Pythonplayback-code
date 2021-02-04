import sounddevice as sd
import soundfile as sf

#Reference:https://python-sounddevice.readthedocs.io/en/0.4.1/

#recording
def record():
    print("ENTER RECORDING INFORMATION\n")
    print("File name for recording:")
    filename = input()
    print("Sample rate:")
    sample_rate = int(input())
    print("Duration (in sec):")
    duration = int(input())  # seconds
    print("RECORDING " + filename + "...")
    rec_array = sd.rec(sample_rate * duration, samplerate=sample_rate, channels=1)
    print(type(rec_array))
    print("Done.")
    sd.wait()
    sf.write(filename, rec_array, sample_rate)

# playback and record
def playrec():
    print("ENTER PLAYBACK TRACK FILE INFORMATION\n")
    print("Track to play:")
    play_file = input()
    try:
        play_array, sample_rate = sf.read(play_file)
    except FileNotFoundError:
        print(play_file + " is not a file")
    print("ENTER RECORDING INFORMATION\n")
    print("File name for recording:")
    rec_file = input()
    print(sd.query_devices())
    print(sd.default.device)
    sd.default.device = [2, 1]
    print("PLAYING " + play_file + ". RECORDING " + rec_file + "...")
    rec_array = sd.playrec(play_array, sample_rate, channels=1)
    print("Done recording " + rec_file)
    sd.wait()
    sf.write(rec_file, rec_array, sample_rate)


# #playback
def playback():
    print("ENTER TRACK FILE INFORMATION\n")
    print("Track to play:")
    play_file = input()
    try:
        play_array, sample_rate = sf.read(play_file)
    except FileNotFoundError:
        print(play_file + " is not a file")
    print("PLAYING " + play_file + "...")
    sd.play(play_array, sample_rate)
    print("Done.")
    sd.wait()


if __name__ == "__main__":
    playback()
