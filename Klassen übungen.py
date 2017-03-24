class WindowProgram(Tkinter.Frame):
    """ This class creates a frame for my program window """
    def __init__(self, parent):
        Tkinter.Frame.__init__(self, parent)

class App(Tkinter.Tk):
    """ application constructor """
    def __init__(self):
        Tkinter.Tk.__init__(self)
        self.window_program = Window_Program(self)
