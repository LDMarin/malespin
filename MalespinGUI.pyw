import MalespinCLI as ms
from tkinter import *


class MalespinGUI(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        master.title("Malespin Translator")
        master.resizable(False, False)
        master.geometry("300x150")

        self.text_variable = ""

        self.main_frame = Frame(master)
        self.entry_label = Label(self.main_frame, text="Enter text here:")
        self.text_entry = Entry(
            self.main_frame, textvariable=self.text_variable)
        self.action_button = Button(
            self.main_frame, text="Translate", command=self.translate, height=2)

        # Layout

        self.main_frame.pack(padx=20, pady=20, expand=True, fill="x")
        self.entry_label.pack()
        self.text_entry.pack(fill="x", pady=20)
        self.action_button.pack()

    def translate(self):
        self.word = self.text_entry.get()
        self.text_entry.delete(0, END)
        self.new_word = ms.translate(self.word)
        self.text_entry.insert(0, self.new_word)


def main():
    root = Tk()
    my_gui = MalespinGUI(root)
    my_gui.mainloop()


if __name__ == "__main__":
    main()
