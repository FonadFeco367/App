import tkinter as tk
from tkinter import ttk, messagebox
import csv

class FFD_FlottaKezelo:
    def __init__(self, root):
        self.root = root
        self.root.title("Céges Flotta Olajcsere Nyilvántartó")
        self.root.geometry("650x450")
        self.adatok = []

        self.ffd_elem_letrehozas()

    def ffd_elem_letrehozas(self):
        self.cim_label = ttk.Label(self.root, text="Céges Flotta Olajcsere Nyilvántartó", font='Arial 14 bold')
        self.cim_label.grid(row=0, column=0, columnspan=3, pady=15)

        self.rendszam_label = ttk.Label(self.root, text="Rendszám:")
        self.rendszam_label.grid(row=1, column=0, sticky='w', padx=20, pady=5)
        self.rendszam_be = ttk.Entry(self.root, width=20)
        self.rendszam_be.grid(row=1, column=1, padx=10, pady=5)

        self.km_label = ttk.Label(self.root, text="Aktuális KM:")
        self.km_label.grid(row=2, column=0, sticky='w', padx=20, pady=5)
        self.km_be = ttk.Entry(self.root, width=20)
        self.km_be.grid(row=2, column=1, padx=10, pady=5)

        self.datum_label = ttk.Label(self.root, text="Olajcsere Dátuma:")
        self.datum_label.grid(row=3, column=0, sticky='w', padx=20, pady=5)
        self.datum_be = ttk.Entry(self.root, width=20)
        self.datum_be.grid(row=3, column=1, padx=10, pady=5)

        self.hozzaad_gomb = ttk.Button(self.root, text="Olajcsere Rögzítése", command=self.ffd_olajcsere_hozzaad)
        self.hozzaad_gomb.grid(row=4, column=0, columnspan=2, pady=15)

        self.lista_box = tk.Listbox(self.root, width=60, height=8)
        self.lista_box.grid(row=5, column=0, columnspan=3, padx=20, pady=10)

        self.mentes_gomb = ttk.Button(self.root, text="Mentés CSV-be", command=self.ffd_mentes_csv)
        self.mentes_gomb.grid(row=6, column=0, pady=10)

        self.kilepes_gomb = ttk.Button(self.root, text="Kilépés", command=self.root.destroy)
        self.kilepes_gomb.grid(row=6, column=2, pady=10)

    def ffd_olajcsere_hozzaad(self):
        rendszam = self.rendszam_be.get().strip()
        km_szoveg = self.km_be.get().strip()
        datum = self.datum_be.get().strip()

        if not rendszam or not km_szoveg or not datum:
            messagebox.showerror('Hiba', 'Minden mezőt ki kell tölteni!')
            return

        try:
            km = int(km_szoveg)
        except ValueError:
            messagebox.showerror('Hiba', 'A kilométerállás csak szám lehet!')
            return

        sor = f"Rendszám: {rendszam} | KM: {km} km | Dátum: {datum}"
        self.adatok.append((rendszam, km, datum))
        self.lista_box.insert(tk.END, sor)

        self.rendszam_be.delete(0, tk.END)
        self.km_be.delete(0, tk.END)
        self.datum_be.delete(0, tk.END)

    def ffd_mentes_csv(self):
        if not self.adatok:
            messagebox.showwarning('Figyelmeztetés', 'Nincs mit menteni!')
            return

        try:
            with open('flotta_olajcsere.csv', mode='w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow(['Rendszám', 'Kilométeróra', 'Dátum'])
                for adat in self.adatok:
                    writer.writerow(adat)
            messagebox.showinfo('Siker', 'A mentés sikeresen megtörtént!')
        except OSError:
            messagebox.showerror('Hiba', 'Nem sikerült a fájlba mentés!')