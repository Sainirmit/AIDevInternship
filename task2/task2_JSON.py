import json

def create_json_data():
    print("Enter a new entry")
    new_name = input("Enter name: ")
    new_age = input("Enter age: ")
    new_email = input("Enter email: ")

    json_data = read_json_data('task2/task2.json')

    for entry in json_data:
        if entry['name'] == new_name:
            print(f"Error: Entry for {new_name} already exists")
            return     
    new_entry = {
        "name": new_name,
        "age": int(new_age),
        "email": new_email
    }
    json_data.append(new_entry)
    with open('task2/task2.json', 'w') as f:
        json.dump(json_data, f, indent=4)
    print(f"Entry for {new_name} created successfully")
      
def read_json_data(file_path):
    with open(file_path) as f:
        data = json.load(f)
    return data


def update_json_data():
    nameToUpdate = input("Enter the name of the entry to update: ")
    json_data = read_json_data('task2/task2.json')
    for entry in json_data:
        if entry['name'] == nameToUpdate:
            print(f"current entry: {entry}")
            new_name = input(f"Enter the new name for {nameToUpdate}: ")
            new_age = int(input(f"Enter the new age for {nameToUpdate}: "))
            new_email = input(f"Enter the new email for {nameToUpdate}: ")

            if new_age or new_email or new_name:
                entry['age'] = new_age
                entry['email'] = new_email
                entry['name'] = new_name
            print(f"updated entry: {entry}")
            break;
    else:
        print(f"No entry found with name: {nameToUpdate}")

    with open('task2/task2.json', 'w') as f:
        json.dump(json_data, f)

def delete_json_data():
    nameToDelete = input("Enter the name of the entry to delete: ")
    json_data = read_json_data('task2/task2.json')
    for entry in json_data:
        if entry['name'] == nameToDelete:
            json_data.remove(entry)
            print(f"Entry for {nameToDelete} deleted successfully")
            break
    else:
        print(f"No entry found with name: {nameToDelete}")

    with open('task2/task2.json', 'w') as f:
        json.dump(json_data, f)
            
def main():
    json_data = read_json_data('task2/task2.json')
    print(f"The current JSON data is: {json_data}")
    print("Enter 1 to create a new entry")
    print("Enter 2 to update an entry")
    print("Enter 3 to delete an entry")
    print("Enter 4 to exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        create_json_data()
        print(f"The current JSON data is: {json_data}")
        main()
    elif choice == 2:
        update_json_data()
        print(f"The current JSON data is: {json_data}")
        main()
    elif choice == 3:
        delete_json_data()
        print(f"The current JSON data is: {json_data}")
        main()
    elif choice == 4:
        print("Exiting the program")
    else:
        print("Invalid choice. Please enter a valid option.")
    

if __name__ == "__main__":
    main()
