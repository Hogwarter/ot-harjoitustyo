from tkinter import ttk, constants 
from services.collections_service import collections_service, InvalidCredentialsError

class LoginView:
    def __init__(self, root, handle_login, handle_new_user_view):
        self._root = root
        self._handle_login = handle_login
        self._handle_new_user_view = handle_new_user_view
        self._frame = None
        self._username_entry = None
        self._password_entry = None
        self._error_msg_variable = None
        self._error_msg_label = None
        self._initialize()
    
    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _login_handler(self):
        username = self._username_entry.get()
        password = self._password_entry.get()
        try:
            collections_service.login(username, password)
            self._handle_login()
        except InvalidCredentialsError:
            self._show_message("Please input a valid username and password")

    def _show_error(self, message):
        self._error_variable.set(message)
        self._error_label.grid()

    def _initialize_unp_fields(self):
        _username_label = ttk.Label(master=self._root_view, text="Username")
        _username = ttk.Entry(master=self._root_view)
        _username_label.grid(row=1, column=0, padx=5, pady=5)
        _username.grid(row=1, column=1, padx=5, pady=5, sticky=(constants.E, constants.W))
        
        _password_label = ttk.Label(master=self._root_view, text="Password")
        _password = ttk.Entry(master=self._root_view)
        _password_label.grid(row=2, column=0, padx=5, pady=5)
        _password.grid(row=2, column=1, padx=5, pady=5,sticky=(constants.E, constants.W))


    def initialize(self):
        self._root_view = ttk.Entry(master=self._root)

        self._initialize_unp_fields()
        
        _login_button = ttk.Button(
            master=self._root_view, text="Login", command=self.login_click)
        _new_user_button = ttk.Button(
            master=self._root_view, text="New user", command=self.new_user_click)
        
        _login_button.grid(row=3, column=0, columnspan=1, padx=5, pady=5)
        _new_user_button.grid(
            row=3, column=0, columnspan=3, padx=5, pady=5, sticky=(constants.E))

        self._root_view.grid_columnconfigure(1, weight=1, minsize=500)
        
        