# Task 1
def sum_of_number(number):
    if number > 0:
        return sum_of_number(number // 10) + number % 10
    else:
        return 0


print(sum_of_number(5103))


# Task 2
def show_n(to_num, from_num):
    print(from_num)
    if from_num >= to_num:
        return
    else:
        return show_n(to_num, from_num + 1)


show_n(5, 0)
