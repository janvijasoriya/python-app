def print_table(number):
    print(f"Table of {number}:")
    for i in range(1, 11):
        print(f"{number} x {i} = {number * i}")

if __name__ == "__main__":
    try:
        num = int(input("Enter a number: "))
        print_table(num)
    except ValueError:
        print("Please enter a valid number!")
