def encrypt(text, shift):
    result = ""

    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            if char.islower():
                start = ord('a')
            else:
                start = ord('A')

            result += chr((ord(char) - start + shift_amount) % 26 + start)
        else:
            result += char

    return result

def decrypt(encrypted_text, shift):
    return encrypt(encrypted_text, -shift)

def main():
    print("간단한 시저 암호 프로그램에 오신 것을 환영합니다.")
    text = input("암호화할 텍스트를 입력하세요: ")
    shift = 3 

    encrypted = encrypt(text, shift)
    print(f"암호화된 텍스트: {encrypted}")

    decrypted = decrypt(encrypted, shift)
    print(f"복호화된 텍스트: {decrypted}")

if __name__ == "__main__":
    main()
