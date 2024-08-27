class Validation():

    def __init__(self):
        
        self.main_file_path = '~/code_projects/'
        self.directory_name = input('What do you want to name the directory?: ')
        self.spyder_list = input("Please list the name of spyder(s) you would like to create (please separate each name with a comma ','): ")


    def initialize(self):
        spyders = self.get_spyder_list(self.spyder_list)
        directory_name = self.directory_name
        result = (directory_name, spyders)
        return result


    def spyder_list_check(self, spyder_list):
        clean_list = spyder_list.split(',')
        return clean_list
    
    def get_spyder_list(self, spyders):
        check = self.spyder_list_check(spyders)
        confirm_list = input(f'Create this list of spiders? Y/n : {", ".join(map(str, check))}')
        while confirm_list != 'y':
            check = self.spyder_list_check(spyders)
            confirm_list = input(f'Create this list of spiders? Y/n : {", ".join(map(str, check))}')
        return check