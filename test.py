#!/usr/bin/env python3

'''
Test KBHit

Copyright (c) 2023 Simon D. Levy

MIT License
'''

from kbhit import KBHit

kb = KBHit()

print('Hit any key, or ESC to exit')

while True:

    if kb.kbhit():
        c = kb.getch()
        if ord(c) == 27: # ESC
            break
        print(c)
         
kb.set_normal_term()
