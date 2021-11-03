import sounddevice as sd
import numpy as np

# https://python-sounddevice.readthedocs.io/en/0.3.3/examples.html#plot-microphone-signal-s-in-real-time
# Set up sound for WSL https://research.wmz.ninja/articles/2017/11/setting-up-wsl-with-graphics-and-audio.html

def print_sound(indata, outdata, frames, time, status):
    volume_norm = np.linalg.norm(indata)*10
    print ("|" * int(volume_norm))

with sd.Stream(callback=print_sound):
    sd.sleep(10000)