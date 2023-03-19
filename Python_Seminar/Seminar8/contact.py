def add_contact():
    with open('contacts.txt', 'a') as f:
        last_name = input("Введите фамилию: ")
        first_name = input("Введите имя: ")
        middle_name = input("Введите очество: ")
        phone_number = input("Введите номер телефона: ")
        f.write(f"{last_name}, {first_name}, {middle_name}, {phone_number}\n")
        print("Контакт успешно добавлен!")

def show_all_contacts():
    with open('contacts.txt', 'r') as f:
        contacts = [line.strip() for line in f]
        sorted_contacts = sorted(contacts, key=lambda x: x.split(',')[0])
        for contact in sorted_contacts:
            print(contact)


def search_contact():
    search_term = input("Введите фамилию для поиска: ")
    found = False
    with open('contacts.txt', 'r') as f:
        for line in f:
            if search_term.lower() in line.lower():
                print(line.strip())
                found = True
    if not found:
        print("Контактов не найдено\n")

def delete_contact():
    search_term = input("Введите фамилию контакта который хотите удалить: ")
    contacts = []
    found = False
    with open('contacts.txt', 'r') as f:
        for line in f:
            if search_term.lower() not in line.lower():
                contacts.append(line)
            else:
                found = True
    if not found:
        print("Контакт не найден.")
    else:
        with open('contacts.txt', 'w') as f:
            for contact in contacts:
                f.write(contact)
        print("Контакт успешно удалён!")

def update_contact():
    search_term = input("Введите фамилию контакта который хотите изменить: ")
    contacts = []
    found = False
    with open('contacts.txt', 'r') as f:
        for line in f:
            if search_term.lower() not in line.lower():
                contacts.append(line)
            else:
                found = True
                last_name, first_name, middle_name, phone_number = line.strip().split(", ")
                new_last_name = input(f"Введите новую фамилию для контакта {first_name} {middle_name}: ")
                new_first_name = input(f"Введите новое имя для контакта {new_last_name} {middle_name}: ")
                new_middle_name = input(f"Введите новое очество для контакта {new_last_name} {new_first_name}: ")
                new_phone_number = input(f"Введите новый номер телефона для контакта {new_last_name} {new_first_name} {new_middle_name}: ")
                contacts.append(f"{new_last_name}, {new_first_name}, {new_middle_name}, {new_phone_number}\n")
    if not found:
        print("Контакт не найден")
    else:
        with open('contacts.txt', 'w') as f:
            for contact in contacts:
                f.write(contact)
        print("Контакт успешно обнавлён!")
