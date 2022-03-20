# # import playsound as ps
# # import os
# # import sounddevice as sd
# # import numpy
# #
# # # print(sd.query_devices())
# # # devices = sd.query_devices()
# # # indexOfInputDevice = 1
# # #
# # # sd.default.device = 5
# # #
# # # file = "C:\\Users\\yunus\\PycharmProjects\\Sound-Localization\\footSound.wav"
# # # ps.playsound(os.system(file))
# # #
# # # sd.play(file)
# #
# # import sounddevice as sd
# # import numpy as np
# # (fs1, x) = read('footSound.wav', 'rb')
# # sd.play(x, fs1)
#
# from tkinter import *
# import sounddevice
# import threading
# import soundfile
#
# DATA_TYPE = "int16"
#
#
# class myThread(threading.Thread):
#     def __init__(self, args):
#         threading.Thread.__init__(self)
#         self.args = args
#
#     def run(self):
#         playmp3(self.args)
#
#
# class streamData:
#     def __init__(self, index):
#         self.outstream = create_running_output_stream(index)
#
#
# class musicData:
#     def __init__(self, path):
#         self.music = load_sound_file_into_memory(path)
#
#
# def load_sound_file_into_memory(path):
#     audio_data, _ = soundfile.read(path, dtype=DATA_TYPE)
#     return audio_data
#
#
# def get_device_number_if_usb_soundcard(index_info):
#     index, info = index_info
#     if "Kulaklıklar" in info["name"] or "THX Spatial Audio" in info["name"] and info["hostapi"] == 3:
#         return index
#     return False
#
#
# def create_running_output_stream(index):
#     output = sounddevice.RawOutputStream(
#         device=index,
#         dtype=DATA_TYPE
#     )
#     return output
#
# a = sounddevice.query_devices()
# sound_card_indices = list(filter(lambda x: x is not False,
#                                  map(get_device_number_if_usb_soundcard,
#                                      [index_info for index_info in enumerate(sounddevice.query_devices())])))
#
# song1 = musicData("C:\\Users\\yunus\\PycharmProjects\\Sound-Localization\\footSound.wav")
# song2 = musicData("C:\\Users\\yunus\\PycharmProjects\\Sound-Localization\\silahsesi.wav")
# stream1 = streamData(sound_card_indices[0])
# stream2 = streamData(sound_card_indices[1])
#
#
# def playmp3(args):
#     if args == 1:
#         stream1.outstream.write(song1.music)
#     else:
#         stream2.outstream.write(song2.music)
#
#
# def play1():
#     global thread1
#     thread1 = myThread(1)
#     stream1.outstream.start()
#     thread1.start()
#
#
# def play2():
#     global thread2
#     thread2 = myThread(2)
#     stream2.outstream.start()
#     thread2.start()
#
#
# def stop1():
#     stream1.outstream.stop()
#     print(thread1.isAlive())
#
#
# def stop2():
#     stream2.outstream.stop()
#     print(thread2.isAlive())
#
#
# myWindow = Tk()
#
# myWindow.title('Python MP3 player')
# Label(myWindow, text="").grid(row=0)
# Label(myWindow, text="").grid(row=1)
# Label(myWindow, text="").grid(row=2, column=0, sticky=W, padx=15, pady=15)
# Button(myWindow, text='wav.1', command=play1).grid(row=2, column=1, sticky=W, padx=5, pady=5)
# Label(myWindow, text="").grid(row=2, column=2, sticky=W, padx=15, pady=15)
# Button(myWindow, text='wav.2', command=play2).grid(row=2, column=3, sticky=W, padx=5, pady=5)
# Label(myWindow, text="").grid(row=2, column=4, sticky=W, padx=15, pady=15)
# Label(myWindow, text="").grid(row=3)
# Label(myWindow, text="").grid(row=4, column=0, sticky=W, padx=15, pady=15)
# Button(myWindow, text='stop', command=stop1).grid(row=4, column=1, sticky=W, padx=5, pady=5)
# Label(myWindow, text="").grid(row=4, column=2, sticky=W, padx=15, pady=15)
# Button(myWindow, text='stop', command=stop2).grid(row=4, column=3, sticky=W, padx=5, pady=5)
# Label(myWindow, text="").grid(row=4, column=4, sticky=W, padx=15, pady=15)
#
# myWindow.mainloop()
import time

import sounddevice as sd
import soundfile as sf
import threading
from threading import Thread

def audioFunc1():
    audio1 = "silahsesi.wav"
    data1, fs1 = sf.read(audio1, dtype='float32')
    sd.play(data1, fs1, device=6)   #speakers


def audioFunc2():
    audio2 = "footSound.wav"
    data2, fs2 = sf.read(audio2, dtype='float32')
    sd.play(data2, fs2, device=5)  #headset

if __name__ == '__main__':
    print(sd.query_devices())
    t1 = Thread(target = audioFunc1)
    t2 = Thread(target = audioFunc2)

    t1.start()
    t2.start()

    time.sleep(10000)

    t1.join()
    t2.join()