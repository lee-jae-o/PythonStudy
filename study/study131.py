import random
import string

def generate_password(length):
    if length < 4:  
        return "암호는 최소한 4자 이상이어야 합니다."
    
    all_characters = string.ascii_letters + string.digits + string.punctuation
    password = []


    password.append(random.choice(string.ascii_uppercase))
    password.append(random.choice(string.ascii_lowercase))
    password.append(random.choice(string.digits))
    password.append(random.choice(string.punctuation))


    password += random.choices(all_characters, k=length-4)


    random.shuffle(password)
    
    return ''.join(password)

if __name__ == "__main__":
    while True:
        print("\n암호 생성기")
        length = input("원하는 암호 길이를 입력하세요 (종료하려면 '종료'를 입력하세요): ").strip()

        if length.lower() == "종료":
            break

        try:
            length = int(length)
            password = generate_password(length)
            print(f"생성된 암호: {password}")
        except ValueError:
            print("잘못된 입력입니다. 숫자를 입력하세요.")
