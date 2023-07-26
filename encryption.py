def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            is_uppercase = char.isupper()
            alphabet_start = ord('A' if is_uppercase else 'a')
            shifted_char = chr((ord(char) - alphabet_start + shift) % 26 + alphabet_start)
            result += shifted_char.upper() if is_uppercase else shifted_char
        else:
            result += char
    return result

def main():
    choice = input("Выберите действие: 1 - Зашифровать, 2 - Расшифровать: ")
    if choice not in ["1", "2"]:
        print("Некорректный выбор.")
        return

    text = input("Введите текст: ")
    shift = int(input("Введите сдвиг: "))

    if choice == "1":
        encrypted_text = caesar_cipher(text, shift)
        print(f"Зашифрованный текст: {encrypted_text}")
    elif choice == "2":
        decrypted_text = caesar_cipher(text, -shift)
        print(f"Расшифрованный текст: {decrypted_text}")

if __name__ == "__main__":
    main()
