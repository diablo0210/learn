# Silent auction Programme

data_bids = {}

bidding_finished = False


def highest_bidder(bid_record):
    max_bid = 0
    winner = ""
    for i in bid_record:
        bid_amt = bid_record[i]
        if bid_amt > max_bid:
            max_bid = bid_amt
            winner = i
    print(f"The winner of this Silent Auction is {winner.upper()} with a bid amount of {bid_amt}.")


while bidding_finished is False:
    name_input = input("Enter your name: ")
    bid_input = int(input("Enter your bid amount: "))
    data_bids[name_input] = bid_input
    to_continue = input("Are there any other bidders? Yes or No: ").lower()
    if to_continue == "no":
        bidding_finished = True
        highest_bidder(data_bids)
    # elif to_continue == "yes":
    #     bidding_finished = False


