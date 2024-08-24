class Validation():

    def __init__(self):
        
        self.main_file_path = '~/code_projects/'
        self.directory_name = input('What do you want to name the directory?: ')
        self.spyder_list = input("Please list the name of spyder(s) you would like to create (please separate each name with a comma ','): ")

        self.initialize()
    def initialize(self):
        check = self.get_spyder_list()
        if check == 'None':
            print('Please re-enter your list of spyders.')
            self.get_spyder_list()
        else:
            directory_name = self.directory_name()
            return (directory_name, check)


    def spyder_list_check(self, spyder_list):
        clean_list = spyder_list.split(',')
        return clean_list
    
    def get_spyder_list(self):
        spy_list = self.spyder_list
        check = self.spyder_list_check(spy_list)
        confirm_list = input(f'Create this list of spiders? Y/n : {", ".join(map(str, check))}')
        if confirm_list == 'n':
            return None
        else:
            return check