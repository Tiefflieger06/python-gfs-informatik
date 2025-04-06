import os
import shutil
import string

def is_valid_foldername(name):
    # Check if name is empty
    if not name:
        return False
    # Check for valid characters (ASCII letters, numbers, underscore, hyphen)
    valid_chars = set(string.ascii_letters + string.digits + '_-')
    return all(char in valid_chars for char in name)

def main():
    # Create arbeitsmappen directory if it doesn't exist
    if not os.path.exists('./arbeitsmappen'):
        os.makedirs('./arbeitsmappen')

    # Get folder name from user
    while True:
        folder_name = input("Ordnernamen eingeben: ").strip()
        target_path = os.path.join('./arbeitsmappen', folder_name)
        
        if not is_valid_foldername(folder_name):
            print("Ungültiger Name. Nur Buchstaben, Zahlen, Unterstriche oder Bindestriche sind erlaubt.")
            continue
            
        if os.path.exists(target_path):
            print("Dieser Name existiert bereits. Bitte einen anderen Namen eingeben.")
            continue
            
        break

    # Create target path
    target_path = os.path.join('./arbeitsmappen', folder_name)

    # Copy directory
    if os.path.exists('./2_tasks'):
        shutil.copytree('./2_tasks', target_path)
        print(f"Erfolgreich erstellt: {target_path}")
    else:
        print("Error: Source directory './2_tasks' not found")

if __name__ == "__main__":
    main()
