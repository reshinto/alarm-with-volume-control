import subprocess


path = "sample.mp3"

def play(path):
    subprocess.call(["ffplay", "-nodisp", "-autoexit", path])


play(path)
