import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog

root = tk.Tk()
root.title("MonsterCardCatalouge.exe")
root.geometry("600x500") 

root.configure(bg="grey")

names_ofmonsters = [
    "dfkjgmdfg", "xlcfkinlsuf", "otigjbsmh", "sicrmdfjm", 
    "rtvuidyms", "tjmcrjbfm", "kcvniycdo", "bcvfkjgld", 
    "ois8frnmf", "yvnumsg"
]
stats_ofmonsters = [
    [23, 12, 14, 18], [1, 1, 2, 1], [1, 2, 3, 4], 
    [4, 3, 2, 1], [21, 21, 21, 21], [12, 12, 12, 12], 
    [22, 22, 22, 22], [11, 11, 11, 11], [18, 18, 18, 18], 
    [23, 23, 23, 23]
]

names_for_new_monsters = []
stats_for_new_monsters = []

def main_program_menuforcards():
    for widget in root.winfo_children():
        widget.destroy()

    title = tk.Label(root, text="Monster Cards Menu")
    title.pack(pady=20)

    search_button = tk.Button(root, text="Search for monster card", command=monstercard_search)
    search_button.pack(pady=20)

    viewing_ofcatalogue_button = tk.Button(root, text="Look at catalogue", command=viewing_ofcatalogue)
    viewing_ofcatalogue_button.pack(pady=20)

    inputprocess_fornewcards_button = tk.Button(root, text="Enter New Card", command=inputprocess_fornewcards)
    inputprocess_fornewcards_button.pack(pady=20)

    exit_button = tk.Button(root, text="EXIT", command=root.quit)
    exit_button.pack(pady=30, padx=15, anchor='se')

def monstercard_search():
    name = simpledialog.askstring("Search Card", "Please enter monter name:")
    if name:
        if name in names_ofmonsters or name in names_for_new_monsters:
            if name in names_ofmonsters:
                index = names_ofmonsters.index(name)
                stats = stats_ofmonsters[index]
            else:
                index = names_for_new_monsters.index(name)
                stats = stats_for_new_monsters[index]
            display_monster_info(name, stats)
        else:
            messagebox.showerror("Problem / error", "This monster cannot be found!")

def display_monster_info(name, stats):
    for widget in root.winfo_children():
        widget.destroy()

    title = tk.Label(root, text=f"Monster: {name}")
    title.pack(pady=10)

    stats_text = f"Strength: {stats[0]}\nSpeed: {stats[1]}\nCunning: {stats[2]}\nStealth: {stats[3]}"
    stats_label = tk.Label(root, text=stats_text)
    stats_label.pack(pady=10)

    back_button = tk.Button(root, text="Back to Menu", command=main_program_menuforcards)
    back_button.pack(pady=20)

def viewing_ofcatalogue():
    for widget in root.winfo_children():
        widget.destroy()

    title = tk.Label(root, text="Viewing Card Catalogue:")
    title.grid(row=0, column=0, columnspan=6, pady=10)

    headers = ["Name", "Strength", "Speed", "Cunning", "Stealth"]
    for col, text in enumerate(headers):
        tk.Label(root, text=text, padx=10).grid(row=1, column=col, sticky='nsew')

    for i in range(len(names_ofmonsters)):
        name_label = tk.Label(root, text=names_ofmonsters[i], padx=10)
        name_label.grid(row=i + 2, column=0)

        for j in range(4):
            stat_label = tk.Label(root, text=f"{stats_ofmonsters[i][j]:02}", padx=10)
            stat_label.grid(row=i + 2, column=j + 1)

    for i in range(len(names_for_new_monsters)):
        name_label = tk.Label(root, text=names_for_new_monsters[i], padx=10)
        name_label.grid(row=len(names_ofmonsters) + i + 2, column=0)

        for j in range(4):
            stat_label = tk.Label(root, text=f"{stats_for_new_monsters[i][j]:02}", padx=10)
            stat_label.grid(row=len(names_ofmonsters) + i + 2, column=j + 1)

    menu_button = tk.Button(root, text="Menu", command=main_program_menuforcards, width=10)
    menu_button.grid(row=len(names_ofmonsters) + len(names_for_new_monsters) + 2, column=0, pady=10)

    delete_button = tk.Button(root, text="Delete", command=card_deletionprocess, width=10)
    delete_button.grid(row=len(names_ofmonsters) + len(names_for_new_monsters) + 2, column=1, pady=10)

    edit_button = tk.Button(root, text="Edit", command=card_editorprocess, width=10)
    edit_button.grid(row=len(names_ofmonsters) + len(names_for_new_monsters) + 2, column=2, pady=10)

    print_button = tk.Button(root, text="Print cards", command=cardprinting_process, width=10)
    print_button.grid(row=len(names_ofmonsters) + len(names_for_new_monsters) + 2, column=3, pady=10)

    exit_button = tk.Button(root, text="Exit", command=root.quit, width=10)
    exit_button.grid(row=len(names_ofmonsters) + len(names_for_new_monsters) + 2, column=5, pady=10)

def card_deletionprocess():
    global names_ofmonsters, stats_ofmonsters, names_for_new_monsters, stats_for_new_monsters
    names_ofmonsters = []  
    stats_ofmonsters = []  
    names_for_new_monsters = []  
    stats_for_new_monsters = []  
    messagebox.showinfo("Delete Cards", "All cards have been deleted.")
    viewing_ofcatalogue()  

def card_editorprocess():
    name = simpledialog.askstring("Edit Card", "Please enter name of monster:")
    if name in names_for_new_monsters:
        index = names_for_new_monsters.index(name)
        stats = stats_for_new_monsters[index]
        edit_window = tk.Toplevel(root)
        edit_window.title("Edit Monster Card")

        tk.Label(edit_window, text="Monster Name:").grid(row=0, column=0, padx=10, pady=5)
        name_entry = tk.Entry(edit_window)
        name_entry.insert(0, name)  
        name_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(edit_window, text="Strength:").grid(row=1, column=0, padx=10, pady=5)
        strength_entry = tk.Entry(edit_window)
        strength_entry.insert(0, stats[0])  
        strength_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(edit_window, text="Speed:").grid(row=2, column=0, padx=10, pady=5)
        speed_entry = tk.Entry(edit_window)
        speed_entry.insert(0, stats[1])  
        speed_entry.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(edit_window, text="Cunning:").grid(row=3, column=0, padx=10, pady=5)
        cunning_entry = tk.Entry(edit_window)
        cunning_entry.insert(0, stats[2])  
        cunning_entry.grid(row=3, column=1, padx=10, pady=5)

        tk.Label(edit_window, text="Stealth:").grid(row=4, column=0, padx=10, pady=5)
        stealth_entry = tk.Entry(edit_window)
        stealth_entry.insert(0, stats[3])  
        stealth_entry.grid(row=4, column=1, padx=10, pady=5)

        def savecard_changes():
            new_name = name_entry.get()
            new_strength = int(strength_entry.get())
            new_speed = int(speed_entry.get())
            new_cunning = int(cunning_entry.get())
            new_stealth = int(stealth_entry.get())

            names_for_new_monsters[index] = new_name
            stats_for_new_monsters[index] = [new_strength, new_speed, new_cunning, new_stealth]
            edit_window.destroy()
            messagebox.showinfo("Success", "Monster card updated successfully!")
            viewing_ofcatalogue()

        save_button = tk.Button(edit_window, text="Save Changes", command=savecard_changes)
        save_button.grid(row=5, columnspan=2, pady=10)

    else:
        messagebox.showerror("Error", "Monster not found or can't be edited!")

def inputprocess_fornewcards():
    new_card_window = tk.Toplevel(root)
    new_card_window.title("Input New Monster Card")

    tk.Label(new_card_window, text="Monster Name:").grid(row=0, column=0, padx=10, pady=5)
    name_entry = tk.Entry(new_card_window)
    name_entry.grid(row=0, column=1, padx=10, pady=5)

    tk.Label(new_card_window, text="Strength (1-25):").grid(row=1, column=0, padx=10, pady=5)
    strength_entry = tk.Entry(new_card_window)
    strength_entry.grid(row=1, column=1, padx=10, pady=5)

    tk.Label(new_card_window, text="Speed (1-25):").grid(row=2, column=0, padx=10, pady=5)
    speed_entry = tk.Entry(new_card_window)
    speed_entry.grid(row=2, column=1, padx=10, pady=5)

    tk.Label(new_card_window, text="Cunning (1-25):").grid(row=3, column=0, padx=10, pady=5)
    cunning_entry = tk.Entry(new_card_window)
    cunning_entry.grid(row=3, column=1, padx=10, pady=5)

    tk.Label(new_card_window, text="Stealth (1-25):").grid(row=4, column=0, padx=10, pady=5)
    stealth_entry = tk.Entry(new_card_window)
    stealth_entry.grid(row=4, column=1, padx=10, pady=5)

    def savethe_newmonstercards():
        name = name_entry.get()
        strength = int(strength_entry.get())
        speed = int(speed_entry.get())
        cunning = int(cunning_entry.get())
        stealth = int(stealth_entry.get())

        names_for_new_monsters.append(name)
        stats_for_new_monsters.append([strength, speed, cunning, stealth])
        messagebox.showinfo("YaY", "The card has been added.")
        new_card_window.destroy()

    save_button = tk.Button(new_card_window, text="Add a Card", command=savethe_newmonstercards)
    save_button.grid(row=5, columnspan=2, pady=10)

def cardprinting_process():
    with open("monster_cards.txt", "w") as file:
        file.write("Monster Card Catalogue\n\n")

        for i in range(len(names_ofmonsters)):
            file.write(f"{names_ofmonsters[i]}: {stats_ofmonsters[i]}\n")

        for i in range(len(names_for_new_monsters)):
            file.write(f"{names_for_new_monsters[i]}: {stats_for_new_monsters[i]}\n")

    messagebox.showinfo("Print Cards", "The cards have been printed into a txt file.")

main_program_menuforcards()
root.mainloop()