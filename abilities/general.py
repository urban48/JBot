
from abilities.ability_base import AbilityBase
from utils.decorators import command
from utils.objects import CommandObj as co

from conf import settings


class General(AbilityBase):

    @command(co(['help'], 'Show help'))
    def help(self, request, command=None):
        msg = 'here\'s what I can do:\n'
        for ab in self.abilities:
            ability_methods = ab.get_help()
            for cmd in ability_methods:
                msg += '\n{}, commands: {}'.format(cmd[0].help, cmd[0].command)

        self.reply(msg)

    @command(co(['who\'s your daddy'], 'Privilege check'))
    def whos_your_daddy(self, request, command=None):
        if self.update.message.from_user.id in settings.ADMIN_IDS:
            self.reply('You are!')
        else:
            self.reply('Not you!')


