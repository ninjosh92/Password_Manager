import sys
#sys.path.insert(0, 'C:/Users/rafme/dev/Password_Manager/windows')
import PySimpleGUI as sg
import validators
import DB_interface
import DB_object
from AddPasswordWindow import AddPasswordWindow
from GetPasswordWindow import GetPasswordWindow
from ManagePasswordsWindow import ManagePasswordsWindow
from TestWindow import TestWindow

#sys.path.insert(0, 'C:/Users/rafme/dev/Password_Manager/windows')
my_DB_interface = DB_interface.DB_interface("Keys")
sg.theme('DarkAmber')

def main():

	text_layout_side = [
		[
			sg.Text("Image Folder"),
		]
	]
	button_layout_side = [[sg.Text('Input a url (www.example.com)'), sg.Text(size=(15,1), key='-OUTPUT_URL-')],	          
	        	[sg.Button('Test Window')],
				[sg.Button('Get Password')],
	        	[sg.Button('Manage Passwords')],
	        	[sg.Button('Add Password')],
	        	[sg.Button('Exit')]
	        	]


	

	main_layout = [[sg.VPush()],
          [
          	sg.Column(text_layout_side, key = 'Status'),
			sg.VSeperator(),
			sg.Column(button_layout_side)],
          [sg.VPush()]
          ]


	main_window = sg.Window('Pattern 2B', main_layout, resizable =True, element_justification='c', size = (500, 500))
	#main_window.bind('<Configure>', "Configure")
	#status = main_window['Status']

	while True:  # Event Loop
		main_window_event, main_window_values = main_window.read()
		print(main_window_event, main_window_values)
	    
		if main_window_event == 'Test Window':
			#open_add_password_window()
			testWindow = TestWindow.TestWindow("my test window")
			print("Add Password Button works.")

		if main_window_event == 'Add Password':
			#open_add_password_window()
			print("Kirby da best")
			addPasswordWindow = AddPasswordWindow(my_DB_interface)
			print("Add Password Button works.")

		if main_window_event == 'Get Password':
			#open_get_password_window()
			getPasswordWindow = GetPasswordWindow(my_DB_interface)
			print("Get Password Button works.")

		if main_window_event == 'Manage Passwords':
			#open_manage_passwords_window()
			managePasswordsWindow = ManagePasswordsWindow(my_DB_interface)
			print("Manage Passwords Button works.")

		if main_window_event == sg.WIN_CLOSED or main_window_event == 'Exit':
			break
		

		if main_window_event == 'Show':
			isUrlValid = check_url_input_valid(main_window_values)
			if isUrlValid:
				print('pass')
				main_window['-OUTPUT_URL-'].update(main_window_values['-URL-'])
				main_window['-OUTPUT_USERNAME-'].update(main_window_values['-USERNAME-'])
				main_window['-PASSWORD-'].update(main_window_values['-PASSWORD-'])
			else:
				print('no pass')
				main_window['-OUTPUT_URL-'].update('Bad url/domain')
				main_window['-OUTPUT_USERNAME-'].update(main_window_values['-USERNAME-'])
				main_window['-PASSWORD-'].update(main_window_values['-PASSWORD-'])
			isInputAvailable = check_input_available(main_window_values)

			if isInputAvailable:
				#add the row
				True
			else:
				main_window['-OUTPUT_URL-'].update('Unavailable with this url/username')
				main_window['-OUTPUT_USERNAME-'].update('Unavailable with this url/username')
				main_window['-PASSWORD-'].update(main_window_values['-PASSWORD-'])
	main_window.close()


def check_url_input_valid(main_window_values):
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

def check_input_available(main_window_values):
	#checks if the input is available
	print("inside check_input_available")
	URL = main_window_values['-URL-']
	USERNAME = main_window_values['-USERNAME-']
	PASSWORD = main_window_values['-PASSWORD-']

	my_DB_object = DB_object.DB_object(URL, USERNAME, PASSWORD)

	checkThisEntry = [URL, USERNAME] 
	isNotAvailable = my_DB_interface.isPresent(checkThisEntry)
	#wasAdded = my_DB_interface.addRecord(my_DB_object)

	if isNotAvailable:
		
		return False
	else:
		print("Is available:" + str(isNotAvailable) + "")
		return True

def open_add_password_window():
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
			isUrlValid = check_url_input_valid(addPasswordValues)
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
			isInputAvailable = check_input_available(addPasswordValues)

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

def open_get_password_window():
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
				open_present_password_window(recordToEditKey)
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


def open_present_password_window(passwordToRetrieveKey):
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


def open_manage_passwords_window():
	print("open_manage_passwords_window")
	#TODO get all the DB entries
	my_DB_interface = DB_interface.DB_interface("Keys")
	listOfRecords = my_DB_interface.getAllKeys()
	choices = ('Red', 'Green', 'Blue', 'Yellow', 'Orange', 'Purple', 'Chartreuse')
	text_layout_side = [
		[
			sg.Text("Displaying Websites and Usernames..."),
		],
		[sg.Listbox(listOfRecords, size=(30, 4), key='-RECORDS-', horizontal_scroll=True,enable_events=True, no_scrollbar = False)],
		[sg.Button('Exit')]
	]
	button_layout_side = [[sg.Button('Edit')],
	          [sg.Button('Delete')]]


	main_layout = [[sg.VPush()],
    [
          	sg.Column(text_layout_side, key = 'Status'),
			sg.VSeperator(),
			sg.Column(button_layout_side)],
          [sg.VPush()]
          ]


    #main_window = sg.Window('Pattern 2B', main_layout, resizable =True, element_justification='c', size = (300, 300))
	window = sg.Window("Manage Passwords", main_layout, resizable =True, element_justification='c', modal=True, size = (500, 300))
	choice = None
	while True:
		event, values = window.read()
		if event == "Edit":
			print("Edit Button Selected")
			if values['-RECORDS-']:
				recordToEdit = values['-RECORDS-'][0]
				recordToEditKey = recordToEdit[0:2]
				print("Record key to be deleted: ")
				open_edit_password_window(recordToEditKey)
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


def open_edit_password_window(recordToEditKey):
	print("inside open_edit_password_window")
	my_DB_interface = DB_interface.DB_interface("Keys")
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


main()

