import tkinter as tk

def calculation():
    mile = float(entry.get())
    km = mile * 1.609
    km_round = round(km, 2)
    result_label.config(text=f'{km_round}')

# GUI Window
window = tk.Tk()
window.title('Mile to Km Converter')
window.config(padx=20, pady=20)

# Entry
entry = tk.Entry(width=7)
entry.grid(column=1, row=0)

# Labels
miles = tk.Label(text='Miles')
miles.grid(column=2, row=0)

equal_label = tk.Label(text='is equal to')
equal_label.grid(column=0, row=1)

result_label = tk.Label(text='0')
result_label.grid(column=1, row=1)

km_label = tk.Label(text='Km')
km_label.grid(column=2, row=1)

# Button
button = tk.Button(text='Calculate', command=calculation)
button.grid(column=1, row=3)

window.mainloop()