import customtkinter as ctk

# -----------------------
# Configuration
# -----------------------
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

# -----------------------
# Fenêtre
# -----------------------
app = ctk.CTk()
app.title("RankFlow")
app.geometry("1200x700")

# -----------------------
# Barre du haut
# -----------------------
header = ctk.CTkFrame(app, height=70)
header.pack(fill="x")

title = ctk.CTkLabel(
    header,
    text="🎮 RankFlow",
    font=("Arial", 30, "bold")
)
title.pack(pady=15)

# -----------------------
# Contenu principal
# -----------------------
content = ctk.CTkFrame(app)
content.pack(fill="both", expand=True, padx=20, pady=20)

# Carte SR
sr_frame = ctk.CTkFrame(content)
sr_frame.pack(side="left", fill="both", expand=True, padx=10)

ctk.CTkLabel(sr_frame, text="🏆 SR Actuel", font=("Arial", 22)).pack(pady=20)

sr_entry = ctk.CTkEntry(sr_frame, width=200, justify="center")
sr_entry.insert(0, "6875")
sr_entry.pack()

ctk.CTkLabel(sr_frame, text="🎯 Objectif", font=("Arial", 22)).pack(pady=20)

goal_entry = ctk.CTkEntry(sr_frame, width=200, justify="center")
goal_entry.insert(0, "7000")
goal_entry.pack()

# Boutons
buttons = ctk.CTkFrame(sr_frame, fg_color="transparent")
buttons.pack(pady=30)

ctk.CTkButton(buttons, text="🟢 WIN", width=180).grid(row=0, column=0, padx=10)
ctk.CTkButton(buttons, text="🔴 LOSS", width=180).grid(row=0, column=1, padx=10)

# Carte statistiques
stats = ctk.CTkFrame(content)
stats.pack(side="right", fill="both", expand=True, padx=10)

ctk.CTkLabel(stats, text="📊 Session", font=("Arial", 24, "bold")).pack(pady=20)

ctk.CTkLabel(stats, text="📈 +0 SR", font=("Arial", 18)).pack(pady=8)
ctk.CTkLabel(stats, text="✅ 0 Victoire", font=("Arial", 18)).pack(pady=8)
ctk.CTkLabel(stats, text="❌ 0 Défaite", font=("Arial", 18)).pack(pady=8)
ctk.CTkLabel(stats, text="🔥 Winstreak : 0", font=("Arial", 18)).pack(pady=8)

app.mainloop()