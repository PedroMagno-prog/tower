import json
import os
from core.models.models import Save
from core.colors import RED, RESET, LIGHTBLUE

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CORE_DIR = os.path.dirname(BASE_DIR)

SAVES_FILE = os.path.join(CORE_DIR, "saves", "saves.json")

# Will be populated with 
save = []

# --- Nested Classes  ---
def custom_serializer(obj):
    """Fallback for objects json module does not know how to serialize."""
    if hasattr(obj, '__dict__'):
        return obj.__dict__
    # If it's an Enum, you can return obj.name or obj.value here
    return str(obj)

def save_game():
    # Save lists created during runtime to JSON files
    print("Saving data...")
    # Transforms objects from models classes into dictionaries
    save_data = [save.__dict__ for save in save]

    # Dump the dictionaries into JSON files
    with open(SAVES_FILE, 'w', encoding='utf-8') as f:
        json.dump(save_data, f, indent=4, ensure_ascii=False, default=custom_serializer)

    print("Data saved successfully!")
    pass


# --- Loads ---

def load_save_data(return_list=False):
    """Loads data from JSON files into memory list."""
    global save

    if os.path.exists(SAVES_FOLDER):
        with open(SAVES_FOLDER, 'r', encoding='utf-8') as f:
            # Read raw data (list of dictionaries)
            saves_data = json.load(f)
            if saves_data == []:
                print("None game saved.")
                return
            
            save = [Save(**data) for data in saves_data]
    if return_list:
        return save
    else:
        print(f"{RED}Function: load_save_data{RESET}")
        print(f"{LIGHTBLUE}Data loaded: {len(save)} saves{RESET}\n")


def load_all_saves():
    
    
    pass


def view_saves():
    print("\n--- List of Registered Saves ---")
    if not save:
        print("(No saves registered)")
        return

    for s in save:
        print(f"- {s}")
