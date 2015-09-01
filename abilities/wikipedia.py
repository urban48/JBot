
import wikipedia

from abilities.ability_base import AbilityBase
from utils.decorators import command
from utils.objects import CommandObj as co


class Wikipedia(AbilityBase):

    @command(co(['wiki'], 'Search wikipedia'),)
    def get_wiki_page(self, request, command=None):
        self.reply('give me a sec to find it')
        try:
            wiki_res = wikipedia.page(request)
            self.reply('{} \n\n  Link: {}'.format(wiki_res.summary, wiki_res.url))
        except wikipedia.PageError:
            self.reply("sorry {} couldn't find it".format(self.update.message.from_user.first_name))
        except wikipedia.DisambiguationError as e:
            self.reply("you need to be more specific: \n1. {}\n2. {}\n3. {}\n4. {}\netc...".format(*e.options[:4]))
