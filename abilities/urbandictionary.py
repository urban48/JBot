import requests

from abilities.ability_base import AbilityBase
from utils.decorators import command
from utils.objects import CommandObj as co


class Urbandictionary(AbilityBase):

    def api_call(self, term):
        params = {'term': term}
        try:
            res = requests.get('http://api.urbandictionary.com/v0/define', params=params)
        except Exception:
            return {}
        if res.status_code == 200:
            return res.json()

        return {}

    @command(co(['define'], 'Define words using Urbandictionary'),)
    def define(self, request, command=None):
        res = self.api_call(request)

        if not res['result_type'] == 'exact':
            self.reply('Could not find definition to {}'.format(request))
            return

        definition = res['list'][0]['definition']
        example = res['list'][0]['example']
        self.reply('{}\n\nExample:\n{}'.format(definition, example))




