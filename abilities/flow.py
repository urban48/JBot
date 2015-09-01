
import time

from abilities.ability_base import AbilityBase
from utils.decorators import command
from utils.objects import CommandObj as co


class Flow(AbilityBase):

    flow = {}

    @command(co(['set flow'], 'Set the flow'),)
    def set_flow(self, request, command=None):

        if not request:
            self.reply('Cant set empty flow!')
            return

        flow_obj = {'name': self.update.message.from_user.first_name, 'flow': request, 'time': time.strftime("%d/%m/%y %H:%M")}
        Flow.flow[self.update.message.chat_id] = flow_obj
        self.reply('flow set to: {}'.format(request))

    @command(co(['whats the flow', 'what\'s the flow'], 'Show the flow'),)
    def get_flow(self, request=None, command=None):
        flow_obj = Flow.flow.get(self.update.message.chat_id)
        if not flow_obj:
            self.reply('flow not set')
            return
        self.reply('{name} set the flow at {time} to: {flow}'.format(**flow_obj))