
import wolframalpha

from abilities.ability_base import AbilityBase
from utils.decorators import command
from utils.objects import CommandObj as co


class Wolfram(AbilityBase):

    @command(co('?', 'Tries to find the answer'))
    def ask(self, request, command=None):
        client = wolframalpha.Client(app_id='EQGUQ9-EH8T86J5PK')
        try:
            self.reply('let me think...')
            res = client.query(request)
            self.reply(next(res.results).text)
        except Exception:
            self.reply('Can\'t find the answer to that')

