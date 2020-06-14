from simpleeval import simple_eval
from time import sleep
from termcolor import colored
import random

class Bot:

    wait = 1

    def __init__(self, runtype='once'):
        self.q = ''
        self.a = ''
        self.runtype = runtype

    def _think(self, s):
        return s
    
    def _format(self, s):
        sleep(Bot.wait)
        return colored(s, 'blue')

    def _run_once(self):
        print(self._think(self.a))

    def _run_looped(self):
        while True:
            if self.a in ['x', 'q', 'exit', 'quit']:
                break
            print(self._think(self.a))
            self.a = input()

    def run(self):
        print(self._format(self.q))
        self.a = input()
        if self.runtype == 'once':
            self._run_once()
        elif self.runtype == 'loop':
            self._run_looped()
                


class HelloBot(Bot):
    def __init__(self, runtype='once'):
        self.runtype = runtype
        self.q = "Hi, what is your name?"

    def _think(self, s):
        return f"Hello {s}"

class GreetingBot(Bot):
    def __init__(self):
        self.q = "How are you today?"
    
    def _think(self, s):
        if 'good' in s.lower() or 'fine' in s.lower():
            return "I'm feeling good too"
        else:
            return "Sorry to hear that"

class FavoriteColorBot(Bot):
    def __init__(self):
        self.q = "What's your favorite color?"
    
    def _think(self, s):
        colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'purple']
        return f"You like {s.lower()}? My favorite color is {random.choice(colors)}"

class Garfield:

    def __init__(self, wait=1):
        Bot.wait = wait
        self.bots = []
    
    def add(self, bot):
        self.bots.append(bot)
    
    def _prompt(self, s):
        print(s)
        print()

    def run(self):
        self._prompt("This is Garfield dialog system. Let's talk.")
        for bot in self.bots:
            bot.run()

class CalBot(Bot):
    def __init__(self, runtype='once'):
        self.runtype = runtype
        self.q = "Through recent upgrade I can do calculation now. Input some arithmetic expression to try:"
    
    def _think(self, s):
        result = simple_eval(s)
        return f"Done.Result = {result}"

garfield = Garfield(1)

garfield.add(HelloBot())
garfield.add(CalBot('loop'))

garfield.run()