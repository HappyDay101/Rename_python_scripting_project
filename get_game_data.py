import os
import json
import shutil
from subprocess import PIPE, run
import sys

# Variable names
GAME_DIR_PATTERN = "game"
GAME_CODE_EXTENSION = ".go"
GAME_COMPILE_COMMAND = ["go", "build"]

def find_all_game_paths(source):
    # Find all game paths in the given source directory
    game_paths = []

    for root, dirs, files in os.walk(source):
        for directory in dirs:
            if GAME_DIR_PATTERN in directory.lower():
                path = os.path.join(source, directory)
                game_paths.append(path)

        break

    return game_paths

# Rename files and remove end word for clean naming
def get_name_from_paths(paths, to_strip):
    new_names = []
    for path in paths:
        _, dir_name = os.path.split(path)
        new_dir_name = dir_name.replace(to_strip, "")
        new_names.append(new_dir_name)

    return new_names

# Create new directory for renamed files to be saved
def create_dir(path):
    # Create a new directory if it doesn't already exist
    if not os.path.exists(path):
        os.mkdir(path)

# Copy file to new destination
def copy_and_overwrite(source, dest):
    # Copy the source directory to the destination directory, overwriting if it already exists
    if os.path.exists(dest):
        shutil.rmtree(dest)
    shutil.copytree(source, dest)

# Write JSON file to save directory names and how many there are
def make_json_metadata_file(path, game_dirs):
    # Create a JSON file with the directory names and the number of directories
    data = {
        "gameNames": game_dirs,
        "numberOfGames": len(game_dirs)
    }
    # Use 'with' for context management to prevent data leaks
    with open(path, "w") as f:
        json.dump(data, f)

def compile_game_code(path):
    # Compile the game code in the specified path
    code_file_name = None
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(GAME_CODE_EXTENSION):
                code_file_name = file
                break

        break
    if code_file_name is None:
        return

    command = GAME_COMPILE_COMMAND + [code_file_name]
    run_command(command, path)

def run_command(command, path):
    # Get current working directory
    cwd = os.getcwd()
    # Change to new directory
    os.chdir(path)

    try:
        result = run(command, stdout=PIPE, stdin=PIPE, universal_newlines=True, check=True)
        print("Compile result:", result)
    except subprocess.CalledProcessError as e:
        print("Error occurred while compiling:", e)
    finally:
        # After command is finished, go back to the starting directory
        os.chdir(cwd)

def main(source, target):
    # Get current working directory
    cwd = os.getcwd()
    source_path = os.path.join(cwd, source)
    target_path = os.path.join(cwd, target)

    try:
        game_paths = find_all_game_paths(source_path)
        new_game_dirs = get_name_from_paths(game_paths, "_game")

        create_dir(target_path)

        # Take matching names in two arrays and create a tuple, which gives access at the same time
        for src, dest in zip(game_paths, new_game_dirs):
            dest_path = os.path.join(target_path, dest)
            copy_and_overwrite(src, dest_path)
            compile_game_code(dest_path)

        json_path = os.path.join(target_path, "metadata.json")
        make_json_metadata_file(json_path, new_game_dirs)
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    args = sys.argv
    print(args)
    if len(args) != 3:
        print("You must pass a source and target directory only.")
    else:
        source, target = sys.argv[1:]
        main(source, target)
