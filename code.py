#lost and found system

import json
import os
import datetime

DATA_FILE = "lost_found_data.json"

def now():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def load_data():
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            print("Couldn't read data file — starting fresh.")
    return {"lost": [], "found": []}

def save_data(d):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(d, f, indent=2, ensure_ascii=False)

def prompt(text, example=None, allow_empty=False):
    if example:
        q = f"{text} (e.g. {example}) "
    else:
        q = f"{text}  "
    while True:
        val = input(q).strip()
        if val:
            return val
        if example is not None and val == "":
            return example
        if allow_empty:
            return ""
        print("Please type something or provide input.")

def yes_no(text, default=False):
    suf = " [Y/n]: " if default else " [y/N]: "
    while True:
        r = input(text + suf).strip().lower()
        if r == "" and default is not None:
            return default
        if r in ("y", "yes"):
            return True
        if r in ("n", "no"):
            return False
        print("Please answer 'y' or 'n'.")

def next_id(items):
    if not items:
        return 1
    return max(i.get("id", 0) for i in items) + 1

def show_item_short(it):
    contact = f" | contact: {it['contact']}" if it.get("contact") else ""
    print(f"ID:{it['id']} | {it['item']} @ {it['place']} | status: {it['status']}{contact}")


data = load_data()
_last_deleted = None  

def add(kind):
    print(f"\nRecording a {kind} item — short questions, press Enter to accept examples.")
    if not yes_no("Continue?", default=True):
        print("Okay, returning to menu.")
        return
    ex_item = "black wallet" if kind == "lost" else "silver watch"
    item = prompt("Item name", example=ex_item)
    place = prompt("Where (be specific)", example="Library — 2nd floor, near entrance")
    contact = prompt("Contact (phone/email) — optional", example="555-0123", allow_empty=True) or None
    notes = prompt("Notes (color, brand) — optional", example="Levi's logo", allow_empty=True) or None

    entry = {
        "id": next_id(data[kind]),
        "item": item,
        "place": place,
        "contact": contact,
        "notes": notes,
        "status": kind,
        "reported_at": now()
    }
    data[kind].append(entry)
    save_data(data)
    print("\nSaved! Here’s the summary:")
    show_item_short(entry)
    print()

def list_kind(kind):
    items = data.get(kind, [])
    if not items:
        print(f"\nNo {kind} items found.\n")
        return
    print(f"\n--- {kind.upper()} ({len(items)}) ---")
    for it in items:
        show_item_short(it)
    print()

def mark_claimed():
    list_kind("lost")
    if not data["lost"]:
        return
    try:
        idx = int(prompt("Enter lost item ID to mark as claimed", example="1"))
    except ValueError:
        print("Invalid number.")
        return
    it = next((x for x in data["lost"] if x["id"] == idx), None)
    if not it:
        print("ID not found.")
        return
    if it["status"] == "claimed":
        print("Already claimed.")
        return
    if yes_no(f"Mark ID {idx} ('{it['item']}') as claimed?", default=True):
        it["status"] = "claimed"
        save_data(data)
        print("Marked as claimed.\n")
    else:
        print("Not changed.\n")

def mark_returned():
    list_kind("found")
    if not data["found"]:
        return
    try:
        idx = int(prompt("Enter found item ID to mark as returned", example="1"))
    except ValueError:
        print("Invalid number.")
        return
    it = next((x for x in data["found"] if x["id"] == idx), None)
    if not it:
        print("ID not found.")
        return
    if it["status"] == "returned":
        print("Already returned.")
        return
    if yes_no(f"Mark ID {idx} ('{it['item']}') as returned?", default=True):
        it["status"] = "returned"
        save_data(data)
        print("Marked as returned.\n")
    else:
        print("Not changed.\n")

def edit(kind):
    list_kind(kind)
    if not data[kind]:
        return
    try:
        idx = int(prompt("Enter ID to edit", example="1"))
    except ValueError:
        print("Invalid number.")
        return
    it = next((x for x in data[kind] if x["id"] == idx), None)
    if not it:
        print("ID not found.")
        return
    print("Press Enter to keep current value.")
    it["item"] = prompt(f"Item name [{it['item']}]", example=it["item"], allow_empty=True) or it["item"]
    it["place"] = prompt(f"Place [{it['place']}]", example=it["place"], allow_empty=True) or it["place"]
    it["contact"] = prompt(f"Contact [{it.get('contact') or ''}]", example=it.get("contact") or "", allow_empty=True) or it.get("contact")
    it["notes"] = prompt(f"Notes [{it.get('notes') or ''}]", example=it.get("notes") or "", allow_empty=True) or it.get("notes")
    save_data(data)
    print("Saved changes.\n")

def delete(kind):
    global _last_deleted
    list_kind(kind)
    if not data[kind]:
        return
    try:
        idx = int(prompt("Enter ID to delete", example="1"))
    except ValueError:
        print("Invalid number.")
        return
    it = next((x for x in data[kind] if x["id"] == idx), None)
    if not it:
        print("ID not found.")
        return
    print(f"You are about to delete: ID {idx} — {it['item']} @ {it['place']}")
    if yes_no("Type 'yes' to confirm deletion", default=False):
        _last_deleted = (kind, it)
        data[kind] = [x for x in data[kind] if x["id"] != idx]
        save_data(data)
        print("Deleted. You can undo the last delete from the menu.\n")
    else:
        print("Deletion cancelled.\n")

def undo():
    global _last_deleted
    if not _last_deleted:
        print("Nothing to undo.\n")
        return
    kind, item = _last_deleted
    if any(x["id"] == item["id"] for x in data.get(kind, [])):
        print("Can't undo — an item with that ID already exists.\n")
        _last_deleted = None
        return
    data[kind].append(item)
    data[kind].sort(key=lambda x: x["id"])
    save_data(data)
    print(f"Restored ID {item['id']} — {item['item']}\n")
    _last_deleted = None

def search():
    q = prompt("Search term (item name or place)", example="wallet")
    ql = q.lower()
    results = []
    for kind in ("lost", "found"):
        for it in data[kind]:
            if ql in it["item"].lower() or ql in it["place"].lower():
                results.append((kind, it))
    if not results:
        print("No matches found.\n")
        return
    print("\nMatches:")
    for kind, it in results:
        print(f"[{kind.upper()}] ", end="")
        show_item_short(it)
    print()

def show_all():
    list_kind("lost")
    list_kind("found")

# ---------- menu ----------
def menu():
    print("Lost & Found — Menu")
    print("1) Report lost")
    print("2) Report found")
    print("3) View lost")
    print("4) View found")
    print("5) Mark lost as claimed")
    print("6) Mark found as returned")
    print("7) Search")
    print("8) Edit")
    print("9) Delete")
    print("10) Undo last delete")
    print("11) Show all details")
    print("12) Exit")
    print()

def main():
    while True:
        menu()
        choice = input("Choose (1-12) ▶ ").strip()
        if choice == "1":
            add("lost")
        elif choice == "2":
            add("found")
        elif choice == "3":
            list_kind("lost")
        elif choice == "4":
            list_kind("found")
        elif choice == "5":
            mark_claimed()
        elif choice == "6":
            mark_returned()
        elif choice == "7":
            search()
        elif choice == "8":
            which = prompt("Edit which list? [lost/found]", example="lost").lower()
            if which in ("lost", "found"):
                edit(which)
            else:
                print("Please choose 'lost' or 'found'.")
        elif choice == "9":
            which = prompt("Delete from which list? [lost/found]", example="found").lower()
            if which in ("lost", "found"):
                delete(which)
            else:
                print("Please choose 'lost' or 'found'.")
        elif choice == "10":
            undo()
        elif choice == "11":
            show_all()
        elif choice == "12":
            print("Bye — take care!")
            break
        else:
            print("That choice wasn't recognized. Try again.\n")

if __name__ == "__main__":
    main()
