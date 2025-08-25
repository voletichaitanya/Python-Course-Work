"""Fitness Tracker Application 🏋️

Classes: Person, User, Workout, Meal, FitnessApp.

Features: Register user, log workouts, track calories, show progress.

Pros: Health-related, simple math (calories, duration).

Cons: Not as “business-like” as hotel/car rental."""

# Fitness Tracker Application
# OOP Concepts: Encapsulation, Abstraction, Inheritance, Polymorphism, Class/Instance/Static Methods

class User:
    total_users = 0   # class attribute

    def __init__(self, name, age, weight, height):
        self.name = name
        self.age = age
        self.__weight = weight   # encapsulation
        self.__height = height
        self.workouts = []
        User.total_users += 1

    def add_workout(self, workout, calories):
        self.workouts.append((workout, calories))
        print(f"{self.name} did {workout} burning {calories} cal.")

    def calculate_bmi(self):   # abstraction
        return round(self.__weight / (self.__height ** 2), 2)

    @staticmethod
    def bmi_status(bmi):   # static method
        if bmi < 18.5: return "Underweight"
        elif bmi < 24.9: return "Normal"
        elif bmi < 29.9: return "Overweight"
        return "Obese"

    @classmethod
    def get_total_users(cls):   # class method
        return cls.total_users

    def display_info(self):     # base method
        print(f"Name: {self.name}, Age: {self.age}")


# Inheritance + Polymorphism
class RegularUser(User):
    def display_info(self):
        super().display_info()
        print("Type: Regular")


class PremiumUser(User):
    def __init__(self, name, age, weight, height, trainer):
        super().__init__(name, age, weight, height)
        self.trainer = trainer

    def display_info(self):
        super().display_info()
        print(f"Type: Premium, Trainer: {self.trainer}")


class FitnessTracker:
    def __init__(self):
        self.users = []

    def register_user(self, user):
        self.users.append(user)
        print(f"{user.name} registered!")

    def report(self):
        print("\n--- Report ---")
        print(f"Total Users: {User.get_total_users()}")
        total_wk = sum(len(u.workouts) for u in self.users)
        print(f"Total Workouts: {total_wk}")


def main():
    tracker = FitnessTracker()

    u1 = RegularUser("Chaitu", 22, 65, 1.75)
    u2 = PremiumUser("Sriram", 21, 55, 1.62, "Coach Arjun")

    tracker.register_user(u1)
    tracker.register_user(u2)

    u1.add_workout("Running", 200)
    u2.add_workout("Yoga", 100)

    for u in tracker.users:
        u.display_info()
        bmi = u.calculate_bmi()
        print(f"BMI: {bmi}, Status: {User.bmi_status(bmi)}\n")

    tracker.report()


if __name__ == "__main__":
    main()

