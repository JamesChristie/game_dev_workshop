#!/usr/bin/env python

import sys
import time

import sdl2
import sdl2.ext

from engine import loop

def execute():
  sdl2.ext.init()

  window = sdl2.ext.Window("Python Game Workshop", size=(1024, 768))
  window.show()

  loop.run()

  window.refresh
  time.sleep(1)

  return 0

if __name__ == "__main__":
  sys.exit(execute())
