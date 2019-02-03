from os import walk
import discord
import json

class R:
    gifs = []

    @staticmethod
    def load():
        R.gifs.clear()
        f = open('res/gifs.json')
        R.gifs = json.load(f)
        f.close()

