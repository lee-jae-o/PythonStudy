import sys

def calculate_square(number):
    return str(number * number)  

if __name__ == "__main__":
    if len(sys.argv) > 1:
        number = int(sys.argv[1])
    else:
        number = int(input("Enter a number: "))

    print(calculate_square(number)) 