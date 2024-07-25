def read_file_line_by_line(file_path):
    try:
        with open(file_path, 'r') as file:
            print("파일의 내용:")
            for line_number, line in enumerate(file, start=1):
                print(f"{line_number}: {line.strip()}")
    except FileNotFoundError:
        print(f"파일 '{file_path}'을(를) 찾을 수 없습니다.")
    except Exception as e:
        print(f"파일을 읽는 중 오류가 발생했습니다: {e}")

def main():
    file_path = input("읽고 싶은 파일의 경로를 입력하세요: ")
    read_file_line_by_line(file_path)

if __name__ == "__main__":
    main()
