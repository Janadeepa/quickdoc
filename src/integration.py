# src/integration.py

import subprocess

def git_commit_changes(commit_message):
    subprocess.run(['git', 'add', '.'])
    subprocess.run(['git', 'commit', '-m', commit_message])

def git_push_to_remote(branch_name='main'):
    subprocess.run(['git', 'push', 'origin', branch_name])

# Example usage:
if __name__ == "__main__":
    git_commit_changes("Updated documentation.")
    git_push_to_remote()
