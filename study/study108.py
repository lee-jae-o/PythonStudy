def calculate_xp_for_next_level(level):
   
    return 100 + (level - 1) * 50

def calculate_total_xp(current_level, target_level):
    total_xp = 0
    for level in range(current_level, target_level):
        total_xp += calculate_xp_for_next_level(level)
    return total_xp

if __name__ == "__main__":
    current_level = 5
    target_level = 10

    total_xp_needed = calculate_total_xp(current_level, target_level)

    print(f"현재 레벨: {current_level}")
    print(f"목표 레벨: {target_level}")
    print(f"총 필요 경험치: {total_xp_needed} XP")