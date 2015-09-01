

from abilities.ability_base import AbilityBase
from utils.decorators import command
from utils.objects import CommandObj as co


class General(AbilityBase):

    @command(co(['help'], 'Show help'))
    def help(self, request, command=None):
        msg = 'here\'s what I can do:\n'
        for ab in self.abilities:
            ability_methods = ab.get_help()
            for cmd in ability_methods:
                msg += '\n{}, commands: {}'.format(cmd[0].help, cmd[0].command)

        self.reply(msg)