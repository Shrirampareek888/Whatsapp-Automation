# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 21:59:11 2020

@author: shrir
"""

from Send_msg import send_sms
from apscheduler.schedulers.blocking import BlockingScheduler



sched = BlockingScheduler()

sched.add_job(send_sms, 'interval', seconds='specify according to you')

sched.start()