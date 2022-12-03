import PySimpleGUI as sg
import validators
import DB_interface
import DB_object
from PresentPasswordWindow import PresentPasswordWindow

class GetPasswordWindow:
    #creates the window object
    #params: url, the username, and the password
    #return: true if successful, flase otherwise
    def __init__(self, my_DB_interface):
        print("Inside get password class")
        self.my_DB_interface = my_DB_interface
        self.open_get_password_window(my_DB_interface)

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

    def open_get_password_window(self, recordToEditKey):
        print("open_get_password_window")
        #TODO get all the DB entries
        my_DB_interface = DB_interface.DB_interface("Keys")
        listOfRecords = my_DB_interface.getAllKeys()
        
        text_layout_side = [
            [
                sg.Text("Make a Selection to retrieve a password."),
            ],
            [sg.Listbox(listOfRecords, size=(30, 4), key='-RECORDS-', horizontal_scroll=True,enable_events=True)],
            [sg.Button('Exit')]
        ]
        button_layout_side = [[sg.Button('Select')]]
	          


        main_layout = [[sg.VPush()],
        [
                sg.Column(text_layout_side, key = 'Status'),
                sg.VSeperator(),
                sg.Column(button_layout_side)],
            [sg.VPush()]
            ]


        #main_window = sg.Window('Pattern 2B', main_layout, resizable =True, element_justification='c', size = (300, 300))
        window = sg.Window("Get Password Window", main_layout, resizable =True, element_justification='c', modal=True, size = (500, 300))
        choice = None
        while True:
            event, values = window.read()
            if event == "Select":
                print("Select Button Selected")
                if values['-RECORDS-']:
                    recordToRetreave = values['-RECORDS-'][0]
                    recordToEditKey = recordToRetreave[0:2]
                    print("Record key to be recordToEditKey: ", recordToEditKey)
                    #self.open_present_password_window(recordToEditKey)
                    presentPasswordWindow = PresentPasswordWindow(recordToEditKey, my_DB_interface)
            if event == "Delete":
                print("Delete button selected")
                if values['-RECORDS-']:
                    recordToDelete = values['-RECORDS-'][0]
                    recordToDeleteKey = recordToDelete[0:2]
                    print("Record key to be deleted: ")
                    print(recordToDeleteKey)
                    my_DB_interface.deleteRecord(recordToDeleteKey)
            if event == "Exit" or event == sg.WIN_CLOSED:
                break
        window.close()