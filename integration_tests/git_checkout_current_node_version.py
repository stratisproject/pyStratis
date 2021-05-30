import os


def git_checkout_current_node_version(version: str) -> None:
    """Checks out the most current version of the StratisFullNode with the specified branch.

    Returns:
        None
    """
    project_uri = 'https://github.com/stratisproject/StratisFullNode.git'
    clone_dir = os.path.join(os.getcwd(), 'StratisFullNode')
    root_dir = os.getcwd()
    if not os.path.exists(os.path.join(clone_dir)):
        os.system(f'git clone {project_uri} {clone_dir}')
        os.chdir(clone_dir)
        os.system('git fetch')
        os.system(f'git checkout -b release/{version} origin/release/{version}')
        os.system(f'git pull')
        os.chdir(root_dir)
    else:
        os.chdir(clone_dir)
        os.system('git fetch')
        os.system(f'git checkout release/{version}')
        os.system(f'git pull')
        os.chdir(root_dir)
