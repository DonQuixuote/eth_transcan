#from web3 import web3 
#Call for ethereum address for tracking
wallet_input = input("Enter desired wallet: ")
#Require 42 characters (eth address length) else no tracking , should start with 0x also
if len(wallet_input) != 42:
    print (wallet_input)
else:

    print ("Tracking wallet trail")

