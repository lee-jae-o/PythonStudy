import os

def check_file_exists(file_path):
    if os.path.exists(file_path):
        print(f"파일 '{file_path}'은(는) 존재합니다.")
    else:
        print(f"파일 '{file_path}'은(는) 존재하지 않습니다.")

def main():
    file_path = input("확인하고 싶은 파일의 경로를 입력하세요: ")
    check_file_exists(file_path)

if __name__ == "__main__":
    main()
