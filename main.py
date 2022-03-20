import time
import sounddevice as sd
import soundfile as sf
from threading import Thread

def audioFunc1():
    audio1 = "silahsesi.wav"
    data1, fs1 = sf.read(audio1, dtype='float32')
    sd.play(data1, fs1, device=6)   #headset


def audioFunc2():
    audio2 = "footSound.wav"
    data2, fs2 = sf.read(audio2, dtype='float32')
    sd.play(data2, fs2, device=5)  #speakers


def audioFunc3():
    audio3 = "silahsesi.wav"
    data3, fs3 = sf.read(audio3, dtype='float32')
    sd.play(data3, fs3, device=6)   #speakers


def audioFunc1():
    audio4 = "silahsesi.wav"
    data4, fs4 = sf.read(audio4, dtype='float32')
    sd.play(data4, fs4, device=6)   #speakers


if __name__ == '__main__':
    print(sd.query_devices())
    t1 = Thread(target = audioFunc1)
    t2 = Thread(target = audioFunc2)
    #t3 = Thread(target = audioFunc3)
    #t4 = Thread(target = audioFunc4)

    t1.start()
    t2.start()
    #t3.start()
    #t4.start()

    time.sleep(10) #wait for the sound play

    t1.join()
    t2.join()
    #t3.join()
    #t4.join()