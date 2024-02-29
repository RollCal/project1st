import random

def main():
    print("start")
    best_attempt = float('inf')
    play_again = True

    while play_again:
        random_number = random.randint(1, 100)
        attempts = 0

        while True:
            guess = input("숫자를 입력하세요:")

            if not guess.isdigit():
                print("숫자를 입력해주세요")

                continue

            elif int(guess) > 100 or int(guess) < 1:
                print("1~100사이의 숫자를 입력해주세요")

                continue

            guess = int(guess)
            attempts += 1

            if guess < random_number:
                print("Up")
            elif guess > random_number:
                print("Down")
            else:
                print("정답입니다.")
                print(f"시도하신 횟수는 {attempts}입니다.")

                if attempts < best_attempt:
                    print("최고기록입니다.")
                    best_attempt = attempts
                else:
                    print(f"이전 최고 기록은 {best_attempt}입니다.")

                break

        play_again = input("다시 시작하시겠습니까? (y/n)").lower() == "y"

if __name__ == "__main__":
    main()

