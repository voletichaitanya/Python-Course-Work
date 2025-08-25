# Movie ticket booking system
Movies = ["Interstellar","Avengers","Avatar","Oppenheimer","Pushpa","Bahubali"]



# Normal For loop using to printing available movies
print("Available Movies are : ")
for movie in Movies:
    print("-",movie)

# For loop with else block
print("Choose the movie to watch : ")
choosen_movie = input()
for movie in Movies:
    if choosen_movie.lower() == movie.lower():
        print("Movie is available to watch")
        break
else:
    print("Movie is not available for now")
    exit()

# While loop For checking payment pin checking

print("Enter your payment pin : ")
correct_pin = "1234"
attempts = 0
while attempts < 3 :
    pin = input("Enter the pin : ")
    if pin == correct_pin:
        print("payment successful you can watch the movie")
        break
    else:
        print("Incorrect pin try again")
        attempts += 1
else:
    print("payment is not successfull unable to watch the movie")