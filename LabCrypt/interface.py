import os


def display_menu(mapping):
    print("Выберите номер программы для запуска:")
    for num, (description, file) in mapping.items():
        print(f"{num}. {description}")
    print("0. Выход")
    print()


def get_choice(valid_choices):
    while True:
        try:
            choice = int(input("Введите номер программы: "))
            if choice in valid_choices:
                return choice
            else:
                print("Пожалуйста, введите корректный номер программы.")
        except ValueError:
            print("Пожалуйста, введите номер программы.")


def main():
    # Сопоставление номеров с описаниями и файлами программ
    mapping = {
        1: ("Шифр АТБАШ", "atbash.py"),
        2: ("Шифр Цезаря", "cesar.py"),
        3: ("Шифр Полибия", "polibia.py"),
        4: ("Шифр Тритемия", "Tritemia.py"),
        5: ("Шифр Белазо", "belazo.py"),
        6: ("Шифр Виженера", "vizhinera.py"),
        7: ("Матричный шифр", "matrichniy.py"),
        8: ("Шифр Плейфера", "Pleyfera.py"),
        9: ("Вертикальная перестановка", "vertikalnaya_perestanovka.py"),
        10: ("Одноразовый блокнот К.Шеннона", "bloknot.py"),
        11: ("А5/1", "A51.py"),
        12: ("МАГМА", "MAGMA SHIFR.py"),
        13: ("RSA", "RSA.py"),
        14: ("Elgamal", "Elgamal.py"),
        15: ("ECC", "ECC.py"),
        16: ("RSA Цифровой подписи", "RSA DS.py"),
        17: ("Elgamal Цифровой подписи", "Elgamal DS.py"),
        18: ("ГОСТ Р 34.10-94", "ГОСТ Р 34.10-94.py"),
        19: ("ГОСТ Р 34.10-2012", "ГОСТ Р 34.10-2012.py"),
        20: ("Diffie-Hellman", "Diffie-Hellman.py")
    }

    while True:
        display_menu(mapping)
        choice = get_choice(set(mapping.keys()).union({0}))

        if choice == 0:
            print("Выход из программы.")
            break
        else:
            description, selected_file = mapping[choice]
            print(f"Запуск {description} ({selected_file})...")
            print()
            os.system(f"python {selected_file}")
            print()
            input("Нажмите Enter, чтобы вернуться к меню...")
            print()


if __name__ == "__main__":
    main()
