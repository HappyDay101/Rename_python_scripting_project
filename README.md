# Python renaming file script

This Python script is designed to find, copy, and compile files with `_game` in their titles from a source directory to a target directory. It also creates a JSON metadata file containing the names of the new file directories and the total number of files.

## Features

- Finds all directories in the source directory
- Copies directories from the source directory to the target directory
- Compiles the game code in the copied directories
- Creates a JSON metadata file with the names of the file directories and the total number of games

## How to Use

1. Clone this repository to your local machine.
2. Navigate to the directory containing the script.
3. Run the script with the source and target directories as command line arguments:

bash
- MacOS: `python3 get_game_data.py <source_directory> <target_directory>`
- Windows: `python get_game_data.py <source_directory> <target_directory>`

Replace <source_directory> with the path to the directory containing the game directories, and replace <target_directory> with the path to the directory where you want the game directories to be copied.

## Requirements
- Python 3
- Go (for compiling the game code)
