import random

lowest_num = 1
highest_num = 200
answer = random.randint(lowest_num, highest_num)
guesses = 0
is_running = True

print("Number Guessing Game")
print("How this game work :")
print(f"Select a number between {lowest_num} and {highest_num}")

while is_running:
    guess = input("Enter your guess: ")

    if guess.isdigit():
        guess = int(guess)#ใส่ int ตรงนี้ไม่ได้ใส่ค่าข้างบนเพราะเราต้องการเช็คว่าผู้ใช้ป้อนตัวเลขมาไหมแล้วถ้ามาเป็น float ค่อยมาเปลี่ยนตรงนี้
        guesses += 1

        if guess < lowest_num or guess > highest_num:
            print("That number is out of range")
            print(f"Please select a number between {lowest_num} and {highest_num}")
        elif guess < answer:
            print("Too low! Try again!")
            lowest_num = guess
            print(f"Please select a number between {lowest_num} and {highest_num}")
        elif guess > answer:
            print("Too high! Try again!")
            highest_num = guess
            print(f"Please select a number between {lowest_num} and {highest_num}")
        else:
            print(f"Correct!!! The answer was {answer}")
            print(f"Number of guesses : {guesses}")
            print("Thankyou For Playing!!")
            is_running = False

    else:
        print("Invalid guess")
        print(f"Please select a number between {lowest_num} and {highest_num}")