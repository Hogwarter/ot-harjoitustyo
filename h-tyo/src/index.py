from tkinter import Tk, ttk, constants, simpledialog

class UI:
    def __init__(self, root):
        self._root = root
        self._entry = None

    def start(self):
        self._entry = ttk.Entry(master=self._root)
        
        login_button = ttk.Button(master=self._root, text="Log in", command=self.login_click)
        new_user_button = ttk.Button(master=self._root, text="New user", command=self.new_user_click)
        
        username_label = ttk.Label(master=self._root, text="Username")
        username = ttk.Entry(master=self._root)
        password_label = ttk.Label(master=self._root, text="Password")
        password = ttk.Entry(master=self._root)        
        login = ttk.Button(master=self._root, text="Login")
        new_user = ttk.Button(master=self._root, text="Create new user")
        
        username_label.grid(row=1, column=0, padx=5, pady=5)
        username.grid(row=1, column=1, padx=5, pady=5, sticky=(constants.E, constants.W))

        password_label.grid(row=2, column=0, padx=5, pady=5)
        password.grid(row=2, column=1, padx=5, pady=5, sticky=(constants.E, constants.W))

        login_button.grid(row=3, column=0, columnspan=1, padx=5, pady=5)
        new_user_button.grid(row=3, column=0, columnspan=3, padx=5, pady=5, sticky=(constants.E))
    
        
        self._root.grid_columnconfigure(1, weight=1, minsize=500)
        
    def login_click(self):
        entry_value = self._entry.get()
        print(f"Value of entry is: {entry_value}")
        
    def new_user_click(self):
        new_username = simpledialog.askstring(title="Username", prompt="Input new username")
        new_password = simpledialog.askstring(title="Password", prompt="Input new password")
        print(f"Username: {new_username}")
        print(f"Password: {new_password}")
        
     
# tästä tiedosto collections view   



# tuleva tiedosto new user view loppuu tähän

window = Tk()
#window.geometry("750x270")
window.title("App")

ui = UI(window)
ui.start()

window.mainloop()
