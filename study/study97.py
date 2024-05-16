def are_permutations(str1, str2):
    if len(str1) != len(str2):
        return False
    return sorted(str1) == sorted(str2)

if __name__ == "__main__":
    str1 = "listen"
    str2 = "silent"
    if are_permutations(str1, str2):
        print(f"'{str1}'과(와) '{str2}'은(는) 순열 관계입니다.")
    else:
        print(f"'{str1}'과(와) '{str2}'은(는) 순열 관계가 아닙니다.")