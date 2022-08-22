import git

def commit_push() -> bool:
    try:
        repo = git.Repo('./.git')
        repo.git.execute('git add *')
        repo.git.execute('git commit -a -m "commit"')
        repo.git.execute('git push')
        return True
    except:
        pass

colors = {
    0 : (27, 31, 35),
    1 : (14, 68, 41),
    2 : (38, 166, 65),
    3 : (0, 109, 50),
    4 : (57, 211, 83)
}

0x1b1f23

if __name__ == "__main__":
    commit_push()