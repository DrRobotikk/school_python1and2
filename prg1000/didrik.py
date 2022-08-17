from tkinter import *

window = Tk()


def rulett():
    # Be om input fra bruker
    tall = float(tallRulett.get())

    # Bruke if statements for å finne korrekt respons
    if tall < 0:
        farge.set('Tall for lavt')
    else:
        if tall == 0:
            farge.set('Grønn')
        else:
            if tall > 36:
                farge.set('Tall for høyt')
            else:
                if tall >= 29:
                    if tall % 2 == 0:
                        farge.set('Rød')
                    else:
                        farge.set('Svart')
                else:
                    if tall >= 19:
                        if tall % 2 == 0:
                            farge.set('Svart')
                        else:
                            farge.set('Rød')
                    else:
                        if tall >= 11:
                            if tall % 2 == 0:
                                farge.set('Rød')
                            else:
                                farge.set('Svart')
                        else:
                            if tall >= 1:
                                if tall % 2 == 0:
                                    farge.set('Svart')
                                else:
                                    farge.set('Rød')


window.title = ('Rulett')


# Første rad
lblTall = Label(window, text='Oppgi tall')
lblTall.grid(row=0, column=0, padx=100, pady=15)

tallRulett = StringVar()
entTall = Entry(window, width=2, textvariable=tallRulett)
entTall.grid(row=0, column=1, padx=100, pady=15)

# Tredje rad
lblFarge = Label(window, text='Farge på lomme')
lblFarge.grid(row=2, column=0, padx=100, pady=15)

farge = StringVar()
entFarge = Entry(window, width=12, state='readonly', textvariable=farge)
entFarge.grid(row=2, column=1, padx=100, pady=15)

# Knapp
btnRulett = Button(window, text='Vis farge på lomme', command=rulett)
btnRulett.grid(row=1, columnspan=2, pady=15)

window.mainloop()
