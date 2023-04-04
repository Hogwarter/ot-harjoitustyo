import unittest, time, tkinter
from index import UI
from tkinter import Tk


class TestUI(unittest.TestCase):
    def setUp(self):
        #test_ui = UI()
        self.root=Tk()
        self.ui = UI(self.root)
    
    def test_login(self):
        self.ui.make_login_view()
        self.ui_username.focus_set()
        self.root.update()
        for ch in "Nimi":
            self.ui._username.event_generate(ch)
            self.root.update()
            time.sleep(0.2)
        self.ui._password.focus_set()
        self.root.update()
        for ch in "Salasana":
            self.ui._username.event_generate(ch)
            self.root.update()
            time.sleep(0.2)
        print(self.ui._username.get())
        
    
    # Todo:
    #def test_new_user(self):
    #    test_ui = UI(self.root)
    #    new_user = test_ui.new_user_click(self.root) 
    #    print(new_user)
        
    #def test_if_class_exists(self):
    #    test_ui = UI()
    #    if self.assertEqual(self.test_ui):
    #        return True
    #    else:
    #        print("UI class does not exist")
    #        return False
