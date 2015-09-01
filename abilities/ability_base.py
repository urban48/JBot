

class AbilityBase(object):

    def __init__(self, bot, update, abilities):
        self.update = update
        self.bot = bot
        self.abilities = abilities

    def reply(self, replay):
        chat_id = self.update.message.chat_id
        self.bot.sendMessage(chat_id=chat_id, text=replay)

    @classmethod
    def get_commands(cls):
        methods = [vars(cls)[method] for method in vars(cls) if hasattr(vars(cls)[method], 'commands')]
        return {method.__name__: list(map(lambda x: x.command, getattr(method, 'commands'))) for method in methods}
    @classmethod
    def get_help(cls):
        methods = [vars(cls)[method] for method in vars(cls) if hasattr(vars(cls)[method], 'commands')]
        return [vars(method).get('commands') for method in methods]
