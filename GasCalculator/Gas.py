def walmart_saving():
    savings = 0.03
    return savings


def credit_card_benefits(price):
    price = price * .05
    return price


def distance(price):

    distance = float(input(""))

    price_distance = distance * price
    return [price_distance]


def complete_gas_price():
    first_gas = float(input("Fisrt gas price?: "))
    second_gas = float(input("Second gas price?: "))
    WM_gas = input("Are either gas stations walmart? (yes/no): ")
    WM_gas = WM_gas.lower()
    while WM_gas is not "yes" or WM_gas is not "no":
        WM_gas = input("Please try again (yes/no): ")

    if WM_gas == "yes":
        which_gas = input("What gas station is it? (1, 2, both)")
        which_gas = which_gas.lower()
        while which_gas == "1" or which_gas != "2" or which_gas != "both":
            which_gas = input("Please try again (1, 2, both): ")
            which_gas = which_gas.lower()
        if which_gas == "1":
            first_gas = first_gas - walmart_saving() - credit_card_benefits(first_gas)
        elif which_gas == "2":
            second_gas = second_gas - walmart_saving() - credit_card_benefits(second_gas)
        else:
            first_gas = first_gas - walmart_saving() - credit_card_benefits(first_gas)
            second_gas = second_gas - walmart_saving() - credit_card_benefits(second_gas)
    else:
        first_gas = first_gas - credit_card_benefits(first_gas)
        second_gas = second_gas - credit_card_benefits(second_gas)  # Credit card benefits
    print("Distance to first gas station: ")
    gas1_distance_price = distance(first_gas)
    print("Distance to first gas station: ")
    gas2_distance_price = distance(second_gas)
    print("First station is :", f"${first_gas:.2f}")
    print("Second station is :", f"${second_gas:.2f}")

def main():
    complete_gas_price()

main()