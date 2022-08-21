import git


remote_url = "https://github.com/ConnorSwis/github-painter.git"

repo = git.Repo('./.git')
# repo = git.Repo.create_remote
repo.git.execute('git add *')
repo.git.execute('git commit -a -m "$1"')
repo.git.execute('git push')