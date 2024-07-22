def play_quiz(questions):
    score = 0
    for question, info in questions.items():
        print(question)
        for idx, option in enumerate(info['options'], 1):
            print(f"{idx}. {option}")
        answer = input("답을 입력하세요 (번호로 입력): ")
        if int(answer) == info['answer']:
            print("정답입니다!")
            score += 1
        else:
            print("틀렸습니다!")
    return score

def main():
    questions = {
        "파이썬은 어떤 종류의 언어입니까?": {
            "options": ["프로그래밍 언어", "마크업 언어", "스타일 시트 언어"],
            "answer": 1
        },
        "HTML은 무엇의 약자입니까?": {
            "options": ["Hyper Text Markup Language", "Home Tool Markup Language", "Hyperlinks and Text Markup Language"],
            "answer": 1
        },
        "인터넷에서 가장 많이 사용되는 프로토콜은 무엇입니까?": {
            "options": ["HTTP", "FTP", "SMTP"],
            "answer": 1
        }
    }

    total_score = play_quiz(questions)
    print(f"퀴즈 종료! 당신의 점수는 {total_score}/{len(questions)}입니다.")

if __name__ == "__main__":
    main()
