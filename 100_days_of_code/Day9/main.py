from art import logo

print(logo)
print("Welcome to the secret auction program.")

bids = {}
should_continue = True


def do_bid():
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))
    bids[name] = bid


def show_result():
    winner = ''
    temp_bid = 0
    for key in bids:
        if bids[key] > temp_bid:
            temp_bid = bids[key]
            winner = key
    print(f"The winner is {winner} with a bid or ${bids[winner]}.")


while should_continue:
    do_bid()

    keep_going = input("Are there any other bidders? Type 'yes' or 'no.\n")
    if keep_going == 'no':
        should_continue = False

show_result()
