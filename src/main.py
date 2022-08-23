import threading
from funcs import *
import logging


logging.basicConfig(
    filename='github_painter.log',
    format='%(asctime)s:%(levelname)s: %(message)s',
    filemode='w',
    level=logging.DEBUG
)


fp = './src/design2.bmp'
data = read_image(fp)
commit_push()