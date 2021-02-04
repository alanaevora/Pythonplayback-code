# TESTING THREADING FOR PLAYBACK.... SUCCESS!##############################
# Reference: https://classes.engineering.wustl.edu/ese205/core/index.php?title=Playing_multiple_sounds_at_once

from threading import Thread
import soundfile as sf
import sounddevice as sd


def record(filename, sample_rate, duration):
    print("RECORDING " + filename + "...")
    rec_array = sd.rec(sample_rate * duration, samplerate=sample_rate, channels=1)
    print(type(rec_array))
    print("Done.")
    sd.wait()
    sf.write(filename, rec_array, sample_rate)


def playback(play_file):
    print(play_file)
    try:
        play_array, sample_rate = sf.read(play_file)
    except FileNotFoundError:
        print(play_file + " is not a file")
    print("PLAYING " + play_file + "...")
    sd.play(play_array, sample_rate)
    print("Done.")
    sd.wait()


def playrec(play_file, rec_file):
    try:
        play_array, sample_rate = sf.read(play_file)
    except FileNotFoundError:
        print(play_file + " is not a file")
    print("PLAYING " + play_file + ". RECORDING " + rec_file + "...")
    rec_array = sd.playrec(play_array, sample_rate, channels=1)
    print("Done recording " + rec_file)
    sd.wait()
    sf.write(rec_file, rec_array, sample_rate)


threads_playrec = []

if __name__ == '__main__':
    threads_playrec.append(Thread(target=playrec, args=["alana's.wav", "daniel's.wav"]))
    threads_playrec.append(Thread(target=playrec, args=["elise's.wav", "jagger's.wav"]))
for thread in threads_playrec:
    thread.start()


threads_record = []

if __name__ == '__main__':
    threads_record.append(Thread(target=record, args=["alana's.wav", 48000, 3]))
    threads_record.append(Thread(target=record, args=["elise's.wav", 48000, 3]))
# for thread in threads_record:
#     thread.start()


# threads_playback = []
#
# if __name__ == '__main__':
#     threads_playback.append(Thread(target=playback, args=["alana's.wav"]))
#     threads_playback.append(Thread(target=playback, args=["elise's.wav"]))
# for thread in threads_playback:
#     thread.start()
