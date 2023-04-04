import unittest
from index import UI
import tkinter


class Test_ui(unittest.TestCase):
    def setUp(self):
        #test_ui = UI()
        self.root=tkinter.Tk()
    
    def test_new_user(self):
        test_ui = UI(self.root)
        new_user = test_ui.new_user_click(self.root) 
        print(new_user)
        
    #def test_if_class_exists(self):
    #    test_ui = UI()
    #    if self.assertEqual(self.test_ui):
    #        return True
    #    else:
    #        print("UI class does not exist")
    #        return False
