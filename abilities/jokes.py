from time import sleep

import praw

from abilities.ability_base import AbilityBase
from utils.decorators import command
from utils.objects import CommandObj as co


class Jokes(AbilityBase):
    joke_told = []

    @command(co(['tell me a joke', 'humor me', 'tell me a better joke'], 'Tell a joke'))
    def tell_joke(self, request, command=None):
        r = praw.Reddit(user_agent='JBot 0.0.1')
        sub = r.get_subreddit('jokes')

        for joke in sub.get_top_from_day(limit=15):
            if joke.id not in self.joke_told:
                self.reply(joke.title)
                sleep(1)
                self.reply(joke.selftext)

                self.joke_told.append(joke.id)
                return

        self.reply("No more jokes, try tomorrow")
