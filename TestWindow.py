import PySimpleGUI as sg
import validators
import DB_interface
import DB_object

class TestWindow:
    #creates the window object
    #params: url, the username, and the password
    #return: true if successful, flase otherwise
    def __init__(self, name):
        self._name = name
        self.creatWindow()

    #getUrl
    #params: none
    #returns: url stringx
    def getName(self):
        return self._name

    #TODO setters for the members
    #setUrl
    #params: none
    #returns: url stringx
    def setUrl(self, name):
        self._name = name

    def creatWindow(self):
        layout = [[sg.Text('Input a url (www.example.com)'), sg.Text(size=(15,1), key='-OUTPUT_URL-')],
	          [sg.Input(key='-URL-')],
              [sg.Button('Exit')]
              ]

        test_window = sg.Window("Test Window", layout, modal=True)
        while True:
            event, addPasswordValues = test_window.read()
            if event == "Exit" or event == sg.WIN_CLOSED:
                break
                

        test_window.close()