with open("기사.txt", "r", encoding="utf-8") as file:
    content = file.read()

if "조코비치" in content:
    print("O")
else:
    print("X")