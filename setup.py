'''
Python distutils setup file for installing KBHit

Copyright(C) 2019 Simon D.Levy

MIT License
'''

from distutils.core import setup

setup(name='KBHit',
      packages=['kbhit'],
      version='0.1',
      description='Platform-independent keyboard interupts for Python',
      author_email='simon.d.levy@gmail.com',
      url='https://github.com/simondlevy/KBHit',
      license='MIT',
      platforms='Linux; Windows')
