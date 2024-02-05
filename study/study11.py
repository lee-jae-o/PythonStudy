text = input("텍스트를 입력하세요: ")


words = text.lower().split()


word_count = {}
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1


print("단어 빈도수:")
for word, count in word_count.items():
    print(f"{word}: {count}회")