import autoit
from autoit.autoit import Properties

from driver.DriverManager import DriverManager


class Notepad(DriverManager):

    def open_Notepad(self):
        autoit.run("notepad.exe",show_flag=Properties.SW_MAXIMIZE)
        autoit.win_wait_active("Untitled - Notepad", 5)

    def edit_Notepad(self, add_text):
        autoit.control_send("Untitled - Notepad", "Edit1", add_text)

    def save_and_close_Notepad(self):
        autoit.win_close("*Untitled - Notepad")
        autoit.control_click("Notepad", "Button1")
        autoit.win_wait_active("Save", 5)
        autoit.control_send("Save","Edit1","hello.txt")
        autoit.control_click("Save", "Button2",clicks=2)