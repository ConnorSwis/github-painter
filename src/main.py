import threading
from funcs import *
import logging
import schedule
import itertools


logging.basicConfig(
    filename='github_painter.log',
    format='%(asctime)s:%(levelname)s:%(message)s',
    filemode='w',
    level=logging.INFO
)


data = itertools.cycle((0,1,2,3,4)[::-1])

def run():
    cnt = next(data)
    logger.info(str(cnt))
    logger.info('')
    for i in range(cnt):
        msg = f'Commit {i+1}/{cnt}'
        commit_push(msg)

t = lambda: threading.Thread(target=run).start()


schedule.every().day.at("12:58").do(t)

while 1:
    schedule.run_pending()


#  TODO: count % 4; count++ for color. picture can come later.