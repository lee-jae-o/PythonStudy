import re
from collections import Counter

def count_word_frequencies(text):

    words = re.findall(r'\b\w+\b', text.lower())

    frequencies = Counter(words)
    return frequencies

def display_most_common_words(frequencies, num_words=5):

    most_common = frequencies.most_common(num_words)
    if most_common:
        print("가장 자주 등장한 단어:")
        for word, freq in most_common:
            print(f"{word}: {freq}번")
    else:
        print("텍스트에 단어가 없습니다.")

def main():
    print("텍스트를 입력하세요 (여러 줄 가능, 입력을 종료하려면 빈 줄에서 엔터를 두 번 누르세요):")
    lines = []
    while True:
        line = input()
        if line:
            lines.append(line)
        else:
            break
    text = " ".join(lines)
    frequencies = count_word_frequencies(text)
    display_most_common_words(frequencies, 5)

if __name__ == "__main__":
    main()
