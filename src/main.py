import git


def commit_push(commit_message: str="commit"):
    "{bruh} Run {run_number} of {days_runs}"
    try:
        repo = git.Repo('./.git')
        repo.git.execute('git add *')
        repo.git.execute(f'git commit -a -m {commit_message}')
        repo.git.execute('git push')
        return True
    except:
        pass


0x1b1f23

if __name__ == "__main__":
    commit_push()