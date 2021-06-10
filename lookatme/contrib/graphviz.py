"""
Renders ASCII art of Graphviz Dot graphs
"""


import urwid
import subprocess

from lookatme.exceptions import IgnoredByContrib


def render_code(token, body, stack, loop):
    lang = token["lang"] or ""
    if lang != "graphviz":
        raise IgnoredByContrib()
    
    first = subprocess.Popen(['/bin/echo', token["text"]], stdout=subprocess.PIPE)
    second = subprocess.check_output(['graph-easy'], stdin=first.stdout)
    return urwid.Text(second)
