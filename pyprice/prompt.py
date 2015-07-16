# -*- coding:utf-8 -*-


COLORS = {
    'reset': '\033[0m',
    'red': '\033[31m',
    'yellow': '\033[33m',
    'blue': '\033[34m',
    'magenta': '\033[35m',
    'sian': '\033[36m'
}


def colored(text, color):
    return "".join((COLORS[color], str(text), COLORS['reset']))
