def walmart_saving():
    savings = 0.03
    return savings


def credit_card_benefits(price):
    price = price * .05
    return price


def distance(price):

    distance = float(input(""))

    price_distance = distance * price
    return price_distance


def complete_gas_price():
    input_first_gas = float(input("First gas price?: "))
    input_second_gas = float(input("Second gas price?: "))
    WM_gas = input("Are either gas stations walmart? (yes/no): ")
    while WM_gas != "yes" and WM_gas != "no":
        WM_gas = input("Please try again (yes/no): ")

    if WM_gas == "yes":
        which_gas = input("What gas station is it? (1, 2, both)")
        which_gas = which_gas.lower()
        while which_gas == "1" and which_gas != "2" and which_gas != "both":
            which_gas = input("Please try again (1, 2, both): ")
            which_gas = which_gas.lower()
        if which_gas == "1":
            first_gas = input_first_gas - walmart_saving() - credit_card_benefits(input_first_gas)
        elif which_gas == "2":
            second_gas = input_second_gas - walmart_saving() - credit_card_benefits(input_second_gas)
        else:
            first_gas = input_first_gas - walmart_saving() - credit_card_benefits(input_first_gas)
            second_gas = input_second_gas - walmart_saving() - credit_card_benefits(input_second_gas)
    else:
        first_gas = input_first_gas - credit_card_benefits(input_first_gas)
        second_gas = input_second_gas - credit_card_benefits(input_second_gas)  # Credit card benefits
    print("Distance to first gas station: ")
    gas1_distance_price = first_gas * 10 + distance(first_gas)
    print("Distance to second gas station: ")
    gas2_distance_price = second_gas* 10 + distance(second_gas)
    print("First station is :", f"${gas1_distance_price:.2f}")
    print("Second station is :", f"${gas2_distance_price:.2f}")

def main():
    complete_gas_price()

main()