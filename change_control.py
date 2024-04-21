import requests
from tkinter import *
from tkinter import messagebox

# Trello configuration
API_KEY = 'api_key'
TOKEN = 'token'
BOARD_ID = 'board_id'

def create_trello_card(name, desc):
    """Create a Trello card on a specific board."""
    url = "https://api.trello.com/1/cards"
    query = {
        'key': API_KEY,
        'token': TOKEN,
        'idList': BOARD_ID,
        'name': name,
        'desc': desc
    }
    response = requests.request("POST", url, params=query)
    return response.json()

def submit_change_request():
    """Submit a new CAD file change request."""
    name = f"Change Request: {entry_file_name.get()} Revision {entry_revision.get()}"
    desc = f"Details: {text_description.get('1.0', END)}"
    result = create_trello_card(name, desc)
    if result.get('id'):
        messagebox.showinfo("Success", "Change request submitted successfully.")
    else:
        messagebox.showerror("Error", "Failed to submit change request.")

# GUI setup
root = Tk()
root.title("CAD File Change Control System")

Label(root, text="File Name:").grid(row=0, column=0, padx=10, pady=10)
entry_file_name = Entry(root, width=50)
entry_file_name.grid(row=0, column=1, padx=10, pady=10)

Label(root, text="Revision:").grid(row=1, column=0, padx=10, pady=10)
entry_revision = Entry(root, width=50)
entry_revision.grid(row=1, column=1, padx=10, pady=10)

Label(root, text="Description:").grid(row=2, column=0, padx=10, pady=10)
text_description = Text(root, height=10, width=38)
text_description.grid(row=2, column=1, padx=10, pady=10)

Button(root, text="Submit Change Request", command=submit_change_request).grid(row=3, column=1, padx=10, pady=10, sticky=E)

root.mainloop()
