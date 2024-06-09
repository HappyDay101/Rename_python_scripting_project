import os
import json
import shutil
from subprocess import PIPE, run
import sys

GAME_DIR_PATTERN = "game"

def find_all_game_paths(source):
    game_paths = []

    for root, dirs, files in os.walk(source):
        for directory in dirs:
            if GAME_DIR_PATTERN in directory.lower():
                pth = os.path.join(source, directory)
                game_paths.append(path)


        break

def main(source, target):
    # Get current working directory
    cwd = os.getcwd()
    source_path = os.path.join(cwd, source)
    target_path = os.path.join(cwd, target)

if __name__ == "__main__":
    args = sys.argv
    print(args)
    if len(args) != 3:
        raise Exception("You must pass a source and target directory - only.")

    source, target = sys.args[1:]
    main(source, target)
