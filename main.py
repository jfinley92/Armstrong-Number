def armstrong():
    while True:
        number = input("Please enter a number to see if it's an Armstrong number.\nType 'q' to quit. \n")
        if number == 'q':
            break
        number_str = str(number)
        n = len(number_str)
        numbers = []
        total = 0
        for num in number_str:
            numbers.append(int(num))
        for i in numbers:
            total = total + int(i) ** int(n)
        if total == int(number_str):
            print(number_str + " is an Armstrong number!\n")
        else:
            print(number_str + " is not an Armstrong number!\n")


armstrong()
