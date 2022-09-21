#!/usr/bin/env python3

"""

__author__ = 'rohkoder'
__version__ = '0.1.0'
__license__ = 'MIT'
"""

import tkinter as tk


class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        # <create the rest of your GUI here >


if __name__ == "__main__":
    root = tk.Tk()
    MainApplication(root).pack(side="top", fill="both", expand=True)
    root.mainloop()
