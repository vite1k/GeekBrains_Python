from contact import add_contact, show_all_contacts, search_contact, delete_contact, update_contact

def main():
    while True:
        print("Выберите действие:")
        print("1) Добавить новый контакт.")
        print("2) Показать все контакты.")
        print("3) Поиск контакта по фамилии.")
        print("4) Удалить контакт.")
        print("5) Изменить конакт.")
        print("6) Выход.")
        choice = input("> ")
        if choice == "1":
            add_contact()
        elif choice == "2":
            show_all_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            delete_contact()
        elif choice == "5":
            update_contact()
        elif choice == "6":
            break
        else:
            print("Некорректный выбор.")

if __name__ == '__main__':
    main()
