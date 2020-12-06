import tkinter as tk

import fc


def set_program_name(event):
    print("program name is ", event)
    print(program_name.get())
    print(output_name.get())

    fc.start(program_name.get(), output_name.get())


if __name__ == '__main__':
    window = tk.Tk()

    label_enter_program_fname = tk.Label(text="Enter name of .flip program file")
    program_name = tk.Entry()

    label_enter_program_fname.pack()
    program_name.pack()

    label_enter_output_fname = tk.Label(text="Enter name of output file")
    output_name = tk.Entry()

    label_enter_output_fname.pack()
    output_name.pack()

    button = tk.Button(
        text="Proceed",
        width=5,
        height=1,
        bg="cyan",
        fg="black"
    )

    button.bind("<Button-1>", set_program_name)
    button.pack()

    window.mainloop()
