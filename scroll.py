#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Console Text Scroller
~~~~~~~~~~~~~~~~~~~~~

Scroll a text on the console.

Don't forget to play with the modifier arguments!

:Copyright: 2007-2008 Jochen Kupperschmidt
:Date: 31-Aug-2008
:License: MIT_

.. _MIT: http://www.opensource.org/licenses/mit-license.php
"""

from itertools import cycle
from sys import stdout
from time import sleep


def stepper(limit, step_size, loop, backward, bounce):
    """Generate step indices sequence."""
    steps = range(0, limit + 1, step_size)
    if backward:
        steps.reverse()
    if bounce:
        list(steps).extend(reversed(steps))
    if loop:
        steps = cycle(steps)
    return iter(steps)

def display(string):
    """Instantly write to standard output."""
    stdout.write('\r' + string)
    stdout.flush()

def scroll(message, window, backward=False, bounce=True,
           loop=True, step_size=1, delay=0.1, template='[%s]'):
    """Scroll a message."""
    string = ''.join((' ' * window, message, ' ' * window))
    limit = window + len(message)
    steps = stepper(limit, step_size, loop, backward, bounce)
    try:
        for step in steps:
            display(template % string[step:window + step])
            sleep(delay)
    except KeyboardInterrupt:
        pass
    finally:
        # Clean up.
        display((' ' * (window + len(template) - 2)) + '\r')

if __name__ == '__main__':
    scroll('Hello Sam!', 20)