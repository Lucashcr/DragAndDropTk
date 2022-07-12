from sys import path; from pathlib import Path
file = Path(__file__).resolve(); path.append(str(file.parents[1]))

from tkinter import Tk
from draganddroptk import DragAndDropTk


class MainWindow(Tk):
    
    def __init__(self) -> None:
        super().__init__()
        self.title("Test Drag and Drop Widget")
        self.geometry(f"1280x720")
        
        self.dnd_widget = DragAndDropTk(self, width=100, height=50, bg="#002255")
        self.dnd_widget.pack()
        
        
MainWindow().mainloop()