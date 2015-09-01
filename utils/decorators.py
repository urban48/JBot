from utils.objects import CommandObj


def command(*args):
    def wrap_ob(ob):
        for cmd in args:
            if not isinstance(cmd, CommandObj):
                raise Exception('Decorator args must be from type: CommandObj')
            setattr(ob, 'commands', args)
        return ob
    return wrap_ob