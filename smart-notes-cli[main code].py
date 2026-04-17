import json
import datetime
import os

FILE = "notes.json"
# Load notes
def load_notes():
    if not os.path.exists(FILE):
        return []
    with open(FILE, "r") as f:
        return json.load(f)

# Save notes
def save_notes(notes):
    with open(FILE, "w") as f:
        json.dump(notes, f, indent=4)

# Add note
def add_note():
    text = input("Enter note: ")
    tag = input("Enter tag: ")
    time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    notes = load_notes()
    notes.append({"text": text, "tag": tag, "time": time})
    save_notes(notes)
    print("✅ Note added!")

# View notes
def view_notes():
    notes = load_notes()
    if not notes:
        print("No notes found.")
        return

    for i, note in enumerate(notes):
        print(f"\n[{i}] {note['text']}")
        print(f"   Tag: {note['tag']} | Time: {note['time']}")

# Delete note
def delete_note():
    view_notes()
    notes = load_notes()

    try:
        index = int(input("\nEnter index to delete: "))
        notes.pop(index)
        save_notes(notes)
        print("🗑️ Note deleted!")
    except:
        print("Invalid index!")

# Search notes
def search_notes():
    keyword = input("Enter keyword: ").lower()
    notes = load_notes()

    found = False
    for note in notes:
        if keyword in note["text"].lower():
            print(f"\n{note['text']} ({note['tag']})")
            found = True

    if not found:
        print("No matching notes.")

# Menu
def main():
    while True:
        print("\n--- Smart Notes CLI ---")
        print("1. Add Note")
        print("2. View Notes")
        print("3. Delete Note")
        print("4. Search Notes")
        print("5. Exit")

        choice = input("Choose: ")

        if choice == "1":
            add_note()
        elif choice == "2":
            view_notes()
        elif choice == "3":
            delete_note()
        elif choice == "4":
            search_notes()
        elif choice == "5":
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
