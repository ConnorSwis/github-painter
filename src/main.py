import threading
from funcs import *
import logging
import schedule


logging.basicConfig(
    filename='github_painter.log',
    format='%(asctime)s:%(levelname)s: %(message)s',
    filemode='w',
    level=logging.DEBUG
)


fp = './src/design.bmp'
data = read_image(fp)

def run():
    cnt = data.pop(0)
    logger.info(str(cnt))
    for i in range(cnt):
        gil_dumb = 364-len(data)
        msg = f'Day {gil_dumb}/364 Commit {i}/{cnt}'
        commit_push(msg)

t = lambda: threading.Thread(target=run).start()

schedule.every().day.at("12:04").do(t)

while 1:
    schedule.run_pending()


#  TODO: count % 4; count++ for color. picture can come later.