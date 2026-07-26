import customtkinter as ctk

def ask_sr_change(title):
    dialog = ctk.CTkInputDialog(
        text="Combien de SR ?",
        title=title
    )

    value = dialog.get_input()

    if value is None:
        return None

    try:
        return int(value)
    except ValueError:
        return None