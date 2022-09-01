import itertools
import logging
import threading

import schedule

from funcs import *


logging.basicConfig(
    filename='github_painter.log',
    format='%(asctime)s:%(levelname)s:%(message)s',
    filemode='w',
    level=logging.INFO
)


data = itertools.cycle((0,1,2,3,4)[::-1])
if (n:=load()):  # catches up to save, if not first run.
    while True:
        if next(data) == n: break

def run():
    cnt = next(data)
    logger.info("Beginning Run")
    for i in range(cnt):
        commit_push(f'Commit {i+1}/{cnt}')
    save(cnt)


tyson = lambda: threading.Thread(target=run).start()

schedule.every().day.at("12:00").do(tyson)


while 1:
    schedule.run_pending()
