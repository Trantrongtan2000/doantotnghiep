import sys

if sys.version_info[0] == 3:
    import tkinter as tk
    import tkinter.ttk as ttk
else:
    import Tkinter as tk
    import ttk

blood_types = {
    #   Anti-A, Anti-B, Anti-D, : RESULT
    (False, False, True): "O-POSITIVE",
    (False, False, False): "O-NEGATIVE",
    (True, False, True): "A-POSITIVE",
    (True, False, False): "A-NEGATIVE",
    (False, True, True): "B-POSITIVE",
    (False, True, False): "B-NEGATIVE",
    (True, True, True): "AB-POSITIVE",
    (True, True, False): "AB-NEGATIVE",
}


class BloodTypeCalculator(ttk.Frame):
    def __init__(self, master):
        ttk.Frame.__init__(self, master)
        self.master.title("Blood-type Calculator")
        self.master.geometry("400x75+0+0")

        self.anti_a = tk.IntVar()
        self.anti_b = tk.IntVar()
        self.anti_d = tk.IntVar()
        self.control = tk.IntVar()
        self.result = tk.StringVar()
        self.result.set("UNKNOWN")

        self.build_frame()

        self.get_blood_type()

    def build_frame(self):
        anti_a = ttk.Label(self.master, text="ANTI-A")
        anti_a.grid(row=0, column=0)
        anti_a_check = ttk.Checkbutton(self.master, command=self.get_blood_type, variable=self.anti_a,
                                       text='Coagulated?')
        anti_a_check.grid(row=1, column=0)

        anti_b = ttk.Label(self.master, text="ANTI-B")
        anti_b.grid(row=0, column=1)
        anti_b_check = ttk.Checkbutton(self.master, command=self.get_blood_type, variable=self.anti_b,
                                       text="Coagulated?")
        anti_b_check.grid(row=1, column=1)

        anti_d = ttk.Label(self.master, text="ANTI-D")
        anti_d.grid(row=0, column=2)
        anti_d_check = ttk.Checkbutton(self.master, command=self.get_blood_type, variable=self.anti_d,
                                       text="Coagulated?")
        anti_d_check.grid(row=1, column=2)

        control = ttk.Label(self.master, text="CONTROL")
        control.grid(row=0, column=3)
        control_check = ttk.Checkbutton(self.master, command=self.get_blood_type, variable=self.control,
                                        text="Coagulated?")
        control_check.grid(row=1, column=3)

        blood_type = ttk.Label(self.master, text="BLOOD TYPE: ")
        blood_type.grid(row=2, column=0)

        self.blood_type_result = ttk.Label(self.master, textvariable=self.result)
        self.blood_type_result.grid(row=2, column=1, columnspan=4, sticky=(tk.W,))

    def get_blood_type(self):
        a = self.anti_a.get()
        b = self.anti_b.get()
        d = self.anti_d.get()
        c = self.control.get()

        if c == True:
            self.result.set("INVALID")
        else:
            try:
                selection = blood_types[(a, b, d)]
            except KeyError as e:
                print('ERROR: %r' % e)
                self.result.set("INVALID")
            else:
                self.result.set(selection)


def gui_main():
    root = tk.Tk()
    blood_gui = BloodTypeCalculator(root)
    root.mainloop()

''
if __name__ == '__main__':
    gui_main()