import PySimpleGUI as sg
import validators
import DB_interface
import DB_object

class EditPasswordWindow:
    #creates the window object
    #params: url, the username, and the password
    #return: true if successful, flase otherwise
    def __init__(self, recordToEditKey, my_DB_interface):
        print("Inside edit passwords class")
        self.my_DB_interface = my_DB_interface
        self.open_edit_password_window(recordToEditKey, my_DB_interface)

    def check_input_available(self, main_window_values):
        #checks if the input is available
        print("inside check_input_available")
        URL = main_window_values['-URL-']
        USERNAME = main_window_values['-USERNAME-']
        PASSWORD = main_window_values['-PASSWORD-']

        my_DB_object = DB_object.DB_object(URL, USERNAME, PASSWORD)

        checkThisEntry = [URL, USERNAME] 
        isNotAvailable = self.my_DB_interface.isPresent(checkThisEntry)
        #wasAdded = my_DB_interface.addRecord(my_DB_object)

        if isNotAvailable:
            
            return False
        else:
            print("Is available:" + str(isNotAvailable) + "")
            return True

    def check_url_input_valid(self, main_window_values):
        #check if the main_window_values are valid
        #check if url is a valid url or doman
        URL = main_window_values['-URL-']
        USERNAME = main_window_values['-USERNAME-']
        PASSWORD = main_window_values['-PASSWORD-']

        print('inside check_input_valid')
        print(main_window_values['-URL-'])
        print(main_window_values['-USERNAME-'])
        print(main_window_values['-PASSWORD-'])
        print('inside check_input_valid')

        is_url = validators.url(URL)
        is_domain = validators.domain(URL)

        #check if the url/domain is valid
        if is_url or is_domain:
            print("The url is good")
            return True
        else:
            print("The url is bad")
            return False

    def open_present_password_window(self, passwordToRetrieveKey):
        print("inside open_present_password_window")
        my_DB_interface = DB_interface.DB_interface("Keys")
        record = my_DB_interface.getRecord(passwordToRetrieveKey)
        recordPassword = record[0][0]
        layout = [[sg.Text('Here is the password for url: '+  passwordToRetrieveKey[0] + " username: " + passwordToRetrieveKey[1]), sg.Text(size=(15,1), key='-INSTRUCTION_STRING-')],
                [sg.Text('password:'), sg.Text(size=(15,1), key='-PASSWORD-')],
                [sg.Multiline(recordPassword), sg.Text(size=(15,1), key='-PASSWORD-')],
                [sg.Button('Exit')]]

        present_password_window = sg.Window("Present Password", layout, modal=True)
        choice = None

        #my_DB_interface

        while True:
            event, newPasswordValues = present_password_window.read()
                        
            if event == "Exit" or event == sg.WIN_CLOSED:
                break

        present_password_window.close()

    def open_edit_password_window(self, recordToEditKey, my_DB_interface):
        print("inside open_edit_password_window")
        #my_DB_interface = DB_interface.DB_interface("Keys")
        layout = [[sg.Text('Input a new password for url: '+  recordToEditKey[0] + " username: " + recordToEditKey[1]), sg.Text(size=(15,1), key='-INSTRUCTION_STRING-')],
                [sg.Text('new password: '+  recordToEditKey[1]), sg.Text(size=(15,1), key='-NEW_PASSWORD_INPUT_LABEL-')],
                [sg.Input(key='-NEW_PASSWORD-')],
                [sg.Button('Add'), sg.Button('Exit')]]

        open_edit_password_window = sg.Window("Edit Password", layout, modal=True)
        choice = None

        #my_DB_interface

        while True:
            event, newPasswordValues = open_edit_password_window.read()
            
            if event == "Add":
                print("Add button selected")
                print(newPasswordValues)
                
                my_DB_interface.editRecord(recordToEditKey, newPasswordValues['-NEW_PASSWORD-'])


                
            if event == "Exit" or event == sg.WIN_CLOSED:
                break

        open_edit_password_window.close()

    