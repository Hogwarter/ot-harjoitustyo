from tkinter import ttk, constants
from services.collections_service import collections_service, UsernameExistsError

class NewUserView:
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

    