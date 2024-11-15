import tkinter as tk
from tkinter import ttk

# Create the main window
root = tk.Tk()
root.title("Paramètres de la forme")
root.configure(bg="#e6f2ff")  # Light blue background for a soft look
root.geometry("400x600")
root.minsize(400, 600)  # Set minimum size to avoid shrinking too much

# Set a theme for a more modern look
style = ttk.Style(root)
style.theme_use("clam")
style.configure("TLabel", font=("Helvetica", 10), background="#e6f2ff", foreground="#004080")
style.configure("TCombobox", padding=6, relief="flat", background="#cce6ff")
style.configure("TEntry", padding=6, relief="solid", background="#cce6ff", borderwidth=1)
style.configure("TFrame", background="#cce6ff")
style.configure("TButton", background="#004080", foreground="white", font=("Helvetica", 10, "bold"), padding=6)

# Create a frame for better layout organization
form_frame = ttk.Frame(root, padding="15", style="TFrame")
form_frame.grid(row=0, column=0, sticky="nsew", padx=30, pady=20)

# Configure grid to make it resizable
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)
form_frame.grid_columnconfigure(1, weight=1)

# Title Label
ttk.Label(form_frame, text="Paramètres de la forme", font=("Helvetica", 14, "bold"), background="#99ccff", foreground="#004080").grid(
    column=0, row=0, columnspan=2, pady=(0, 15), sticky="ew"
)

# Polyhedron dropdown
ttk.Label(form_frame, text="Polyhedron").grid(column=0, row=1, sticky="w", pady=5)
polyhedron = ttk.Combobox(form_frame, values=["Icosahedron", "Dodecahedron", "Tetrahedron"], state="readonly", style="TCombobox")
polyhedron.set("Icosahedron")
polyhedron.grid(column=1, row=1, sticky="ew")

# Fréquence, V dropdown
ttk.Label(form_frame, text="Fréquence, V").grid(column=0, row=2, sticky="w", pady=5)
freq_v = ttk.Combobox(form_frame, values=[1, 2, 3, 4], state="readonly", style="TCombobox")
freq_v.set(3)
freq_v.grid(column=1, row=2, sticky="ew")

# Classe de subdivision dropdown
ttk.Label(form_frame, text="Classe de subdivision").grid(column=0, row=3, sticky="w", pady=5)
subdivision_class = ttk.Combobox(form_frame, values=["I", "II", "III"], state="readonly", style="TCombobox")
subdivision_class.set("I")
subdivision_class.grid(column=1, row=3, sticky="ew")

# Méthode de subdivision dropdown
ttk.Label(form_frame, text="Méthode de subdivision").grid(column=0, row=4, sticky="w", pady=5)
subdivision_method = ttk.Combobox(form_frame, values=["Cordes égales", "Autre méthode"], state="readonly", style="TCombobox")
subdivision_method.set("Cordes égales")
subdivision_method.grid(column=1, row=4, sticky="ew")

# Axe de symétrie dropdown
ttk.Label(form_frame, text="Axe de symétrie").grid(column=0, row=5, sticky="w", pady=5)
symmetry_axis = ttk.Combobox(form_frame, values=["Pentad", "Tetrad", "Hexad"], state="readonly", style="TCombobox")
symmetry_axis.set("Pentad")
symmetry_axis.grid(column=1, row=5, sticky="ew")

# Fullerène dropdown
ttk.Label(form_frame, text="Fullerène").grid(column=0, row=6, sticky="w", pady=5)
fullerene = ttk.Combobox(form_frame, values=["Aucune", "Option 1", "Option 2"], state="readonly", style="TCombobox")
fullerene.set("Aucune")
fullerene.grid(column=1, row=6, sticky="ew")

# Découpage de la sphère dropdown
ttk.Label(form_frame, text="Découpage de la sphère").grid(column=0, row=7, sticky="w", pady=5)
sphere_cut = ttk.Combobox(form_frame, values=["7/12", "5/12", "3/12"], state="readonly", style="TCombobox")
sphere_cut.set("7/12")
sphere_cut.grid(column=1, row=7, sticky="ew")

# Aligner le bas checkbox
align_bottom_var = tk.IntVar()
align_bottom = ttk.Checkbutton(form_frame, text="Aligner le bas", variable=align_bottom_var)
align_bottom.grid(column=1, row=8, sticky="w", pady=5)

# Divider Label for "Caractéristiques du matériel"
ttk.Label(form_frame, text="Caractéristiques du matériel", font=("Helvetica", 10, "bold"), background="#99ccff", foreground="#004080").grid(
    column=0, row=9, columnspan=2, pady=(20, 10), sticky="ew"
)

# Rayon de la sphère input
ttk.Label(form_frame, text="Rayon de la sphère, m").grid(column=0, row=10, sticky="w", pady=5)
sphere_radius = ttk.Entry(form_frame, style="TEntry")
sphere_radius.insert(0, "10")
sphere_radius.grid(column=1, row=10, sticky="ew")

# Divider Label for "Taille des montants"
ttk.Label(form_frame, text="Taille des montants", font=("Helvetica", 10, "bold"), background="#99ccff", foreground="#004080").grid(
    column=0, row=11, columnspan=2, pady=(20, 10), sticky="ew"
)

# Largeur input
ttk.Label(form_frame, text="Largeur, mm").grid(column=0, row=12, sticky="w", pady=5)
width_entry = ttk.Entry(form_frame, style="TEntry")
width_entry.insert(0, "120")
width_entry.grid(column=1, row=12, sticky="ew")

# Épaisseur input
ttk.Label(form_frame, text="Épaisseur, mm").grid(column=0, row=13, sticky="w", pady=5)
thickness_entry = ttk.Entry(form_frame, style="TEntry")
thickness_entry.insert(0, "40")
thickness_entry.grid(column=1, row=13, sticky="ew")

# Submit Button
submit_button = ttk.Button(form_frame, text="Submit", style="TButton")
submit_button.grid(column=0, row=14, columnspan=2, pady=(20, 10), sticky="ew")

# Start the application
root.mainloop()
