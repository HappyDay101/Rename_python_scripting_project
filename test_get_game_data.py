import unittest
import os
import shutil
from get_game_data import main

class TestMain(unittest.TestCase):
    def setUp(self):
        # Create a temporary source directory for testing
        self.source_dir = "test_source"
        os.mkdir(self.source_dir)

        # Create a temporary target directory for testing
        self.target_dir = "test_target"
        os.mkdir(self.target_dir)

    def tearDown(self):
        # Remove the temporary directories after testing
        shutil.rmtree(self.source_dir)
        shutil.rmtree(self.target_dir)

    def test_main(self):
        # Create some dummy game directories in the source directory
        game_dir1 = os.path.join(self.source_dir, "game1")
        os.mkdir(game_dir1)
        game_dir2 = os.path.join(self.source_dir, "game2")
        os.mkdir(game_dir2)

        # Call the main function with the test directories
        main(self.source_dir, self.target_dir)

        # Assert that the target directory contains the renamed game directories
        renamed_game_dir1 = os.path.join(self.target_dir, "game1")
        renamed_game_dir2 = os.path.join(self.target_dir, "game2")
        self.assertTrue(os.path.exists(renamed_game_dir1))
        self.assertTrue(os.path.exists(renamed_game_dir2))

        # Assert that the target directory contains the metadata.json file
        metadata_file = os.path.join(self.target_dir, "metadata.json")
        self.assertTrue(os.path.exists(metadata_file))

if __name__ == "__main__":
    unittest.main()
