#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author: <Zurdi>

import sys
import os
import psutil
import signal

BASE_DIR = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(BASE_DIR, 'lib'))

from lib_log_nbz import Logging
logger = Logging()


logs = ['geckodriver.log', 'bmp.log', 'server.log']
for log in logs:
    if os.path.isfile(os.path.join(os.getcwd(), log)):
        os.remove(os.path.join(os.getcwd(), log))

ppid = psutil.Process(os.getpid()).ppid()
os.killpg(ppid, signal.SIGTERM)
