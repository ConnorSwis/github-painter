import git
import logging
import os


logger = logging.getLogger()

def commit_push(commit_message: str="commit"):
    """Commits to Github

    Args:
        commit_message (str, optional): Defaults to "commit".

    Returns:
        bool: True or None
    """
    try:
        env = os.environ
        with open('committer', 'wb') as f:
            f.write(os.urandom(16))
        repo = git.Repo('./.git')
        repo.git.execute(['git', 'commit', '-a', '-m', f'"{commit_message}"'], env=env)
        repo.git.execute(['git', 'push'], env=env)
        logger.info(f'Success: {commit_message}')
        return True
    except Exception as e:
        raise e
        logger.error('commit_push failed: ' + str(e)) 

def save(count: int):
    """Saves position in repeating sequence.

    Args:
        count (int): Current item in seqeuence.
    """
    with open('./src/save', 'w') as f:
        f.write(str(count))

def load():
    """Get latest saved position.

    Returns:
        (int)
    """
    try:
        with open('./src/save', 'r') as f: return int(f.read())
    except FileNotFoundError: ...
            

# def read_image(fp: str):
#     """Creates queue for commits from image.

#     Returns:
#         List[List[int]]: _description_
#     """
#     colors = {
#         (27, 31 , 35) : 0, (14, 68 , 41) : 1,
#         (0 , 109, 50) : 2, (38, 166, 65) : 3,
#         (57, 211, 83) : 4
#     }
#     img = Image.open(fp)
#     data = [colors[pixel] for pixel in img.getdata()]
#     rows = [data[i:i+52] for i in range(0, len(data), 52)]
#     result = [
#         [rows[j][i] for j in range(len(rows))] for i in range(len(rows[0]))
#     ]
#     result = [x for y in result for x in y]
#     logger.info('Data read successfully.')
#     return result
