def display_main_menu():
    print("Enter some numbers seperated by commas (e.g. 5, 67, 32)")

def get_user_input():
    user_input = input()                    # 1. read what the user types (always TEXT)
    str_list = user_input.split(",")        # 2. "5, 67, 32" → ['5', ' 67', ' 32']
    float_list = []
    for item in str_list:                   # 3. convert each piece to a number
        float_list.append(float(item))
    return float_list

def calc_average(num_list):
    return sum(num_list) / len(num_list)

def find_min_max(num_list):
    return [min(num_list), max(num_list)]

def sort_temperature(num_list):
    return sorted(num_list)

def calc_median_temperature(num_list):
    s = sorted(num_list)                          # 1. sort first
    n = len(s)
    mid = n // 2                                  # // = whole-number division (7 // 2 = 3)
    if n % 2 == 1:                                # % = remainder → odd count?
        return s[mid]                             #    odd: the middle one
    return (s[mid - 1] + s[mid]) / 2              #    even: average of the middle two

def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    num_list = get_user_input()
    print("Average = " + str(calc_average(num_list)))
    print("Min, Max = " + str(find_min_max(num_list)))
    print("Sorted = " + str(sort_temperature(num_list)))
    print("Median = " + str(calc_median_temperature(num_list)))

if __name__ == "__main__":
    main()