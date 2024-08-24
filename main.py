import os
import subprocess
from helpers.validation import Validation as valid


class ScraperMaker():

    def __init__(self, directory, spyder_list = []):

        self.main_file_path = '~/code_projects/'
        self.directory = directory
        self.spyder_list = spyder_list



    def createDirectory(self):
        print(f'This is your directory path: "{self.main_file_path}+{self.directory}"\n')
        print(f"This is your list of spyders: {", ".join(map(str, self.spyder_list))}")












if __name__ == "__main__":
    start = valid()
    directory_name = start[0]
    spyder_list = start[1]
    ScraperMaker(directory_name, spyder_list)    


