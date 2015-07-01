__module_name__ = "autojoin on invite"
__module_version__ = "1.0"

import hexchat


def join(word, word_eol, userdata):
	hexchat.command('join ' + word[0])


hexchat.hook_print('Invited', join)
