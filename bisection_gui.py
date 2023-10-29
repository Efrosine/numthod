import tkinter as tk
from tkinter import ttk

class TableBisectionGUI:
    """
    A class to create a GUI table to display numerical method results.

    Attributes:
    -----------
    results : list
        A list of tuples containing the numerical method results.

    Methods:
    --------
    create_table()
        Creates a table using the tkinter Treeview widget and populates it with the numerical method results.
    run()
        Runs the tkinter mainloop to display the GUI table.
    """

    def __init__(self, results):
        self.results = results
        self.root = tk.Tk()
        self.root.title("Results Table")
        self.create_table()

    def create_table(self):
        """
        Creates a table using the tkinter Treeview widget and populates it with the numerical method results.
        """
        table = ttk.Treeview(self.root)
        table["columns"] = ("xl", "xu", "fa", "fb", "xm", "fc", "error")
        table.heading("xl", text="xl")
        table.heading("xu", text="xu")
        table.heading("fa", text="f(xl)")
        table.heading("fb", text="f(xu)")
        table.heading("xm", text="xm")
        table.heading("fc", text="f(xm)")
        table.heading("error", text="error")

        for i, result in enumerate(self.results):
            table.insert(parent="", index=i, iid=i, values=(result[0], result[1], result[2], result[3], result[4], result[5], result[6]))

        table.pack()

    def run(self):
        """
        Runs the tkinter mainloop to display the GUI table.
        """
        self.root.mainloop()