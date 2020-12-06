import tkinter as tk

import fc


def set_program_name(event):
    print("program name is ", event)
    print(program_name.get())
    print(output_name.get())

    Alert.set("Compiling you program...")
    fc.start(program_name.get(), output_name.get())
    Alert.set("check generated output file. Thanks!")


if __name__ == '__main__':
    window = tk.Tk(className="FlipBook Generator")
    window.geometry("400x400")

    label_enter_program_fname = tk.Label(text="Enter relative path to .flip program file")
    program_name = tk.Entry(width=100)

    label_enter_program_fname.pack()
    program_name.pack()

    label_enter_output_fname = tk.Label(text="Enter name of output file")
    output_name = tk.Entry(width=100)

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

    Alert = tk.StringVar()
    alert_label = tk.Label(textvariable=Alert)
    alert_label.pack()

    window.mainloop()
