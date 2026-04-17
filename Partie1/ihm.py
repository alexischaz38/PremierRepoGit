import csv
import os
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class CSVViewer:
    def __init__(self, root):
        self.root = root
        self.root.title("Lecteur CSV")
        self.root.geometry("1200x700")
        self.root.configure(bg="#f0f0f0")
        
        # Configurer les styles
        self.setup_styles()
        
        # Titre avec fond coloré
        title_frame = tk.Frame(root, bg="#2c3e50", height=80)
        title_frame.pack(fill=tk.X)
        
        title_label = tk.Label(title_frame, text="📊 Affichage des données CSV", 
                               font=("Arial", 20, "bold"), bg="#2c3e50", fg="white")
        title_label.pack(pady=15)
        
        # Frame pour le tableau avec bordures
        frame_tableau = tk.Frame(root, bg="white", relief=tk.RIDGE, bd=2)
        frame_tableau.pack(fill=tk.BOTH, expand=True, padx=15, pady=15)
        
        # Créer un Treeview avec style personnalisé
        self.tree = ttk.Treeview(frame_tableau, style="Treeview", height=25)
        self.tree.pack(fill=tk.BOTH, expand=True, padx=1, pady=1)
        
        # Scrollbars
        vsb = ttk.Scrollbar(frame_tableau, orient=tk.VERTICAL, command=self.tree.yview)
        hsb = ttk.Scrollbar(frame_tableau, orient=tk.HORIZONTAL, command=self.tree.xview)
        self.tree.configure(yscroll=vsb.set, xscroll=hsb.set)
        vsb.pack(side=tk.RIGHT, fill=tk.Y)
        hsb.pack(side=tk.BOTTOM, fill=tk.X)
        
        # Charger les données
        self.load_csv()
    
    def setup_styles(self):
        """Configure les styles TTK pour le tableau"""
        style = ttk.Style()
        style.theme_use('clam')
        
        # Style pour Treeview
        style.configure('Treeview', 
                       rowheight=30,
                       font=("Arial", 10),
                       borderwidth=1,
                       relief="solid")
        
        style.configure('Treeview.Heading',
                       font=("Arial", 11, "bold"),
                       background="#34495e",
                       foreground="white",
                       borderwidth=1,
                       relief="solid")
        
        # Couleurs alternées
        style.map('Treeview',
                 background=[('selected', '#3498db')],
                 foreground=[('selected', 'white')])
    
    def load_csv(self):
        try:
            # Chemin du fichier CSV
            script_dir = os.path.dirname(os.path.abspath(__file__))
            csv_file = os.path.join(script_dir, "testCSV.csv")
            
            with open(csv_file, mode='r', encoding='utf-8') as file:
                csv_reader = csv.reader(file, delimiter=';')
                
                # Lire l'en-tête
                header = next(csv_reader)
                
                # Configurer les colonnes du Treeview
                self.tree['columns'] = header
                self.tree.column('#0', width=0, stretch=tk.NO)
                
                # Dimensionner les colonnes de manière automatique
                col_width = max(100, int(1100 / len(header)))
                
                for col in header:
                    self.tree.column(col, anchor=tk.CENTER, width=col_width, minwidth=80)
                    self.tree.heading(col, text=col, anchor=tk.CENTER)
                
                # Ajouter les lignes avec alternance de couleurs
                row_index = 0
                for row in csv_reader:
                    self.tree.insert(parent='', index='end', iid=row_index, values=row)
                    row_index += 1
                

        
        except FileNotFoundError:
            messagebox.showerror("Erreur", "❌ Fichier testCSV.csv non trouvé!")
        except Exception as e:
            messagebox.showerror("Erreur", f"❌ Une erreur s'est produite: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = CSVViewer(root)
    root.mainloop()
