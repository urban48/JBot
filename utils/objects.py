
class CommandObj(object):
    def __init__(self, command, help, sub_command=''):
        self.command = command
        self.help = help
        self.sub_command = sub_command

    def is_match(self, in_command):
        return (self.command, self.sub_command) == in_command.partition(' ')[::2]
