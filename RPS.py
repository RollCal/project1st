import random


def rps():
    print("가위바위보게임을 시작합니다")
    options = ('rock', 'scissor', 'paper')
    win = 0
    draw = 0
    lose = 0
    play_again = True

    while play_again:
        computer = random.choice(options)

        while True:
            you = input("rock...scissor...paper!!")

            if you not in options:
                print("rock/scissor/paper 중 하나를 입력해 주세요.")

                continue

            if you == computer:
                print("Draw")
                draw += 1
            elif you == "rock" and computer == "scissor" or (you == "scissor" and computer == "paper") or (
                    you == "paper" and computer == "rock"):
                print("Win")
                win += 1
            else:
                print("Lose")
                lose += 1

            print(f"현재까지 당신의 전적은 {win}승, {draw}무, {lose}패입니다.")

            break

        play_again = input("다시 시작하시겠습니까? y/n").lower() == 'y'

    print("게임 끝")


if __name__ == "__main__":
    rps()
