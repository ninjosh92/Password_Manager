import PySimpleGUI as sg
import validators
import DB_interface
import DB_object

class AddPasswordWindow:
    #creates the window object
    #params: url, the username, and the password
    #return: true if successful, flase otherwise
    def __init__(self, my_DB_interface):
        print("Inside add password class")
        self.my_DB_interface = my_DB_interface
        self.open_add_password_window(my_DB_interface)

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

    def open_add_password_window(self, my_DB_interface):
        print("inside open_add_password_window")
        layout = [[sg.Text('Input a url (www.example.com)'), sg.Text(size=(15,1), key='-OUTPUT_URL-')],
                [sg.Input(key='-URL-')],
                [sg.Text('Input a username (big_example)'), sg.Text(size=(15,1), key='-OUTPUT_USERNAME-')],
                [sg.Input(key='-USERNAME-')],
                [sg.Text('Input a password (password12345)'), sg.Text(size=(15,1), key='-OUTPUT_URL-')],
                [sg.Input(key='-PASSWORD-')],
                [sg.Button('Add'), sg.Button('Exit')]]

        password_window = sg.Window("Add Password", layout, modal=True)
        #choice = None
        while True:
            event, addPasswordValues = password_window.read()
            if event == "Exit" or event == sg.WIN_CLOSED:
                break
            if event == "Add":
                print("Add button selected")
                print(addPasswordValues)
                isUrlValid = self.check_url_input_valid(addPasswordValues)
                if isUrlValid:
                    print('pass')
                    password_window['-OUTPUT_URL-'].update(addPasswordValues['-URL-'])
                    password_window['-OUTPUT_USERNAME-'].update(addPasswordValues['-USERNAME-'])
                    password_window['-PASSWORD-'].update(addPasswordValues['-PASSWORD-'])
                else:
                    print('no pass')
                    password_window['-OUTPUT_URL-'].update('Bad url/domain')
                    password_window['-OUTPUT_USERNAME-'].update(addPasswordValues['-USERNAME-'])
                    password_window['-PASSWORD-'].update(addPasswordValues['-PASSWORD-'])
                isInputAvailable = self.check_input_available(addPasswordValues)

                if isInputAvailable:
                    #add the row
                    my_DB_object = DB_object.DB_object(addPasswordValues['-URL-'], addPasswordValues['-USERNAME-'], addPasswordValues['-PASSWORD-'])
                    wasAdded = my_DB_interface.addRecord(my_DB_object)
                    break
                else:
                    password_window['-OUTPUT_URL-'].update('Unavailable with this url/username')
                    password_window['-OUTPUT_USERNAME-'].update('Unavailable with this url/username')
                    password_window['-PASSWORD-'].update(password_window['-PASSWORD-'])
                

        password_window.close()