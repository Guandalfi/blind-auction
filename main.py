from replit import clear
import art
#HINT: You can call clear() to clear the output in the console.

active_bidders = []

def add_bidders(name, bid):
  bidder = {
    "name": name,
    "bid": bid
  }
  active_bidders.append(bidder)



continue_bidding = True

def find_highest_bidder():
  highest_bid = 0
  highest_bidder = ''
  for value in active_bidders:
    if value["bid"] > highest_bid:
        highest_bid = value["bid"]
        highest_bidder = value["name"]
  print(f"The winner is {highest_bidder} with a bid of R${highest_bid}")
  
print(art.logo)
while continue_bidding == True:
  name = input("What's your name: ")
  bid = int(input("What's your bid R$: "))
  add_bidders(name, bid)
  more_bidders = input("Is the any more bidders ? type 'yes' or 'no':")
  clear()
  if more_bidders == 'no':
    continue_bidding = False


find_highest_bidder()
#print(active_bidders)
  
  
  