from tkinter import Tk, ttk, constants, simpledialog
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import json
#import pygsheets
#import pandas as pd

scopes = [
'https://www.googleapis.com/auth/spreadsheets',
'https://www.googleapis.com/auth/drive'
]

credentials = ServiceAccountCredentials.from_json_keyfile_name("src/users_sheets_key.json", scopes) #access the json key you downloaded earlier 
file = gspread.authorize(credentials) # authenticate the JSON key with gspread
sheet = file.open("ot-h-tyo_users_and_passwords") #open sheet
user_sheet = sheet.sheet_name 

class UI:
    def __init__(self, root, user_sheet):
        self._root = root
        self._view = None
        self.user_sheet = user_sheet
        #self.users_file = open(r"repositories/users.txt", "r+")
        #self.user_sheet = pygsheets.authorize(service_file='src/users_sheets_key.json')
        #self.df = pd.DataFrame()

    def _hide_view(self):
        if self._view:
            self._view.destroy()
        self._view = None

    def start(self):
        self._view = ttk.Entry(master=self._root)

        self._login_button = ttk.Button(
            master=self._root, text="Log in", command=self.login_click)
        self._new_user_button = ttk.Button(
            master=self._root, text="New user", command=self.new_user_click)

        self._username_label = ttk.Label(master=self._root, text="Username")
        self._username = ttk.Entry(master=self._root)
        self._password_label = ttk.Label(master=self._root, text="Password")
        self._password = ttk.Entry(master=self._root)
        # login = ttk.Button(master=self._root, text="Login")
        self._new_user = ttk.Button(master=self._root, text="Create new user")

        self._username_label.grid(row=1, column=0, padx=5, pady=5)
        self._username.grid(row=1, column=1, padx=5, pady=5,
                            sticky=(constants.E, constants.W))

        self._password_label.grid(row=2, column=0, padx=5, pady=5)
        self._password.grid(row=2, column=1, padx=5, pady=5,
                            sticky=(constants.E, constants.W))

        self._login_button.grid(row=3, column=0, columnspan=1, padx=5, pady=5)
        self._new_user_button.grid(
            row=3, column=0, columnspan=3, padx=5, pady=5, sticky=(constants.E))

        self._root.grid_columnconfigure(1, weight=1, minsize=500)

    def login_click(self):
        #entry_value = self._entry.get()
        for line in self.user_sheet:
            #r = line.split(",")
            username = self.user_sheet(line, 1).value
            password = self.user_sheet(line, 2).value
            # lastchar = len(password)-1
            # password = password[0:lastchar]
            print(username, password)
            if self._username == username and self._password == password:
                print("Hello", username)
                break
        self.choose_collection()

    def new_user_click(self):
        new_username = simpledialog.askstring(
            title="Username", prompt="Input new username")
        new_password = simpledialog.askstring(
            title="Password", prompt="Input new password")
        self.user_sheet.update_acell(new_username)
        #self.user_sheet.write(",")
        self.user_sheet.update_acell(new_password)
        #self.user_sheet.write("\n")
        #sheet.append_row(vals)
        print(f"Username: {new_username}")
        print(f"Password: {new_password}")


# tästä tiedosto collections view
#    def choose_collection(self):
#        self._view =
#
#        return

# tuleva tiedosto new user view loppuu tähän
if __name__ == "__main__":
    window = Tk()
    # window.geometry("750x270")
    window.title("App")

    ui = UI(window)
    ui.start()
    window.mainloop()
