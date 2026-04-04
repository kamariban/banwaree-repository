import random

player_score = 0
computer_score = 0

rounds = int(input("How many rounds do you want to play? "))

for i in range(rounds):
    input("\nPress Enter to roll...")

    player_roll = random.randint(1, 6)
    computer_roll = random.randint(1, 6)

    print(f"You rolled: {player_roll}")
    print(f"Computer rolled: {computer_roll}")

    if player_roll > computer_roll:
        print("You win this round!")
        player_score += 1
    elif computer_roll > player_roll:
        print("Computer wins this round!")
        computer_score += 1
    else:
        print("It's a tie!")

print("\n--- Final Score ---")
print(f"You: {player_score}")
print(f"Computer: {computer_score}")

if player_score > computer_score:
    print("🎉 You win the game!")
elif computer_score > player_score:
    print("💻 Computer wins the game!")
else:
    print("🤝 It's a draw!")