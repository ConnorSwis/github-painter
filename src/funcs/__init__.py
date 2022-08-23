import git
import logging
import os
from PIL import Image


logger = logging.getLogger()

def commit_push(commit_message: str="commit"):
    """Commits to Github

    Args:
        commit_message (str, optional): Defaults to "commit".

    Returns:
        bool: True or None
    """
    try:
        repo = git.Repo('./.git')
        repo.git.execute('git add *')
        repo.git.execute(f'git commit -m "{commit_message}"')
        repo.git.execute('git push')
        with open('committer', 'wb') as f:
            f.write(os.urandom(16))
        logger.info(f'Success: {commit_message}')
        return True
    except Exception as e:
        logger.error('commit_push failed: '+str(e)) 



def read_image(fp: str):
    """Creates queue for commits from image.

    Returns:
        List[List[int]]: _description_
    """
    colors = {
        (27, 31 , 35) : 0, (14, 68 , 41) : 1,
        (0 , 109, 50) : 2, (38, 166, 65) : 3,
        (57, 211, 83) : 4
    }
    img = Image.open(fp)
    data = [colors[pixel] for pixel in img.getdata()]
    rows = [data[i:i+52] for i in range(0, len(data), 52)]
    result = [
        [rows[j][i] for j in range(len(rows))] for i in range(len(rows[0]))
    ]
    result = [x for y in result for x in y]
    logger.info('Data read successfully.')
    return result