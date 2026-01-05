from web3 import web3 
#Call for ethereum address for tracking
wallet_input = input("Enter desired wallet: ")
#Require 25 characters else no tracking
if wallet_input != range(0,26):
    print (wallet_input)
else:
    print ("Tracking wallet trail")