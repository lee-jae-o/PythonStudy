class VotingSystem:
    def __init__(self):
        self.candidates = {}
    
    def add_candidate(self, candidate_name):
        if candidate_name in self.candidates:
            print(f"{candidate_name}은(는) 이미 후보 목록에 있습니다.")
        else:
            self.candidates[candidate_name] = 0
            print(f"{candidate_name}을(를) 후보 목록에 추가했습니다.")

    def vote(self, candidate_name):
        if candidate_name in self.candidates:
            self.candidates[candidate_name] += 1
            print(f"{candidate_name}에게 투표했습니다.")
        else:
            print(f"{candidate_name}은(는) 후보 목록에 없습니다.")

    def show_results(self):
        if not self.candidates:
            print("후보자가 없습니다.")
        else:
            print("투표 결과:")
            for candidate, votes in self.candidates.items():
                print(f"{candidate}: {votes}표")

if __name__ == "__main__":
    voting_system = VotingSystem()

    while True:
        print("\n간단한 투표 시스템")
        print("1. 후보 추가")
        print("2. 투표하기")
        print("3. 투표 결과 보기")
        print("4. 종료")

        choice = input("메뉴를 선택하세요: ").strip()

        if choice == "1":
            candidate_name = input("추가할 후보 이름을 입력하세요: ").strip()
            voting_system.add_candidate(candidate_name)

        elif choice == "2":
            candidate_name = input("투표할 후보 이름을 입력하세요: ").strip()
            voting_system.vote(candidate_name)

        elif choice == "3":
            voting_system.show_results()

        elif choice == "4":
            print("프로그램을 종료합니다.")
            break

        else:
            print("잘못된 입력입니다. 메뉴를 다시 선택하세요.")
