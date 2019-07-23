##########################################################################################################
# Libraries
##########################################################################################################


import tkinter # To import library so that i can work with gui.
import tkinter
from tkinter import * 
from tkinter import messagebox


##########################################################################################################
# GLOBAL VARIABLES
##########################################################################################################

top = tkinter.Tk()

mine_reward = 100

generic_block =	{
					"previous_hash" : "XYX",
					"index" : 0,
					"transaction" : []
	 			}

block_chain = [generic_block]
open_transactions = []

owner    = "OM DEV SINGH"
participants = {"OM DEV SINGH"}
userauth = "admin"
passauth = "admin@123"


##########################################################################################################
# TEST FUNCTIONS FOR TKINTER
##########################################################################################################


def donothing():
   filewin = Toplevel(top)
   button = Button(filewin, text="Do nothing button")
   button.pack()


##########################################################################################################
# UI IMPROVEMENT PRINT FUNCTIONS
##########################################################################################################


def sp():
	print(" ")


def fl():
	print("#"*100)


def dl():
	print("."*100)


def kl():
	print("="*100)


def pl():
	print("+"*100)


def print_users_available_options():
	pl()
	print("TO PROCEED SELECT FROM THE LISTED OPTIONS")
	pl()
	sp()
	print("1.) To Print Last Transaction")
	print("2.) To Create Open Transactions")
	print("3.) To print Open Transactions")
	print("4.) To Mine A New Block")
	print("5.) Run crack")
	print("6.) To Print A participants")
	print("7.) Exit")	
	pl()
	sp()
	sp()
	sp()


def choice_input():
	dl()
	user_choice = input("Select : ")
	return user_choice


def success_transaction():
	print("Transaction Completed")


def Failed_transaction():
	print("Transaction Failed")


def block_chain_print():	
	print(block_chain)


def open_transactions_print():	
	print(open_transactions)


def access_deny():	
	print("Access Deny")


def access_grant():	
	print("Access Granted")
	

def block_chain_elements_print():
	for block in block_chain:
		print('Outputting Blocks')
		print(block)
	else:
		print('!'*40)


##########################################################################################################
# SECURITY RELATED FUNCTIONS
##########################################################################################################


def hash_block(block):
	return '-'.join([str(block[key]) for key in block])    #


def crack_test():
	block_chain[0] = {
						"previous_hash" : " ",
						"index" : 0,
						"transaction" : [{'sender' : 'JOHN', 'recipient' : 'SNOW', 'amount' : '55555'}]
	 				}


def user_login_in():
	while True:
		""" 
			:username: username enter by the user for login.
			:password: password entered by the user for login.
		"""
		sp()
		kl()
		username = input("Enter UserName : ")
		password = input("Enter Password : ")
		kl()
		sp()
		if userauth == username and password == passauth:
			access_grant()
			break
		else:
			access_deny()
			continue


def crack_detection_system():	
	for (index, block) in enumerate(block_chain):  # enumerate will generate a tuple with index and block value which are unpacked here.
		if index == 0:
			continue
		if block['previous_hash'] != hash_block(block_chain[index - 1]):
			return False
	return True


##########################################################################################################
# FUNCTIONS
##########################################################################################################


def user_input_to_open_a_transaction():
	""" 
		:tx_sender:    who will send coins for now set to default ie OM.
		:tx_recipient: who will get coins.
		:tx_amount:    no. of coins send in a transaction.
	"""
	tx_sender    = owner
	tx_recipient = input("Enter Recipients Name : ")
	tx_amount    = float(input("Enter Transaction Amount : "))
	return (tx_sender, tx_recipient, tx_amount)	   # sending data in tuple.


def get_last_block_chain_amount():
	return block_chain[-1]


def adding_value_to_open_transactions(this):
	open_transactions.append(this)


def verify_transaction(transaction):
	sender_balance = get_balance(transaction["sender"])
	return  sender_balance>= transaction["amount"]


def add_transactions(sender, recipient, amount=1.0):
	""" 
		:sender:    who will send coins.
		:recipient: who will get coins.
		:amount:    no. of coins send in a transaction default is set to 1.0.
	"""
	transaction =   { 
						'sender':    sender,
						'recipient': recipient,
						'amount':    amount
					}
	if verify_transaction(transaction):
		adding_value_to_open_transactions(this = transaction)
		participants.add(sender)
		participants.add(recipient)
		return True
	return False

def mine_block():
	last_block = block_chain[-1]	# from block chain we took out last element and assigned to last_block.
	hashed_block = hash_block(last_block)
	print(hashed_block)
	min_reward_transaction = {
								'sender':    "SYSTEM",
								'recipient': owner,
								'amount':    mine_reward
	                         }
	copied_open_transactions = open_transactions[:]
	copied_open_transactions.append(min_reward_transaction)
	block =	{
				"previous_hash": hashed_block,
				"index": len(block_chain),
				"transaction" : copied_open_transactions
	 		}
	block_chain.append(block)
	return True		 


def get_balance(participants):
	tx_sender = [[tx["amount"] for tx in block["transaction"] if tx["sender"] == participants] for block in block_chain]
	open_tx_sender = [tx["amount"] for tx in open_transactions if tx["sender"]]
	tx_sender.append(open_tx_sender)
	amount_sent = 0 
	for tx in tx_sender:
		if len(tx) > 0:
			amount_sent += tx[0]
	tx_recipient = [[tx["amount"] for tx in block["transaction"] if tx["recipient"] == participants] for block in block_chain]
	amount_recieved = 0 
	for tx in tx_recipient:
		if len(tx) > 0:
			amount_recieved += tx[0]
	return (amount_recieved - amount_sent)


##########################################################################################################
# MAIN PROGRAM
##########################################################################################################


user_login_in()

sp()
sp()
fl()
fl()
print("                      WELCOME TO YOUR BIT-COIN TRANSFER PORTAL")
fl()
sp()
sp()

# START OF WHILE LOOP.
while True:
	print_users_available_options()
	user_choice_is = choice_input()

	if user_choice_is == "1":
		kl()
		sp()
		block_chain_print()
		sp()
		kl()
		dl()
		sp()
		sp()
		sp()

	elif user_choice_is == "2":
		kl()
		print("Make Your Transaction")
		kl()
		sp()
		tx_data = user_input_to_open_a_transaction()	# imported tuple here which contain multiple dats.
		tx_sender , tx_recipient, tx_amount = tx_data	# opened tupled and used its data
		print("Senders Name   : ",tx_sender)
		print("Recipient Name : ",tx_recipient)
		print("Amount Entered : ", tx_amount)
		if add_transactions(sender=tx_sender, recipient=tx_recipient, amount=tx_amount):		
			success_transaction()
		else:
			Failed_transaction()
		sp()
		kl()
		dl()
		sp()
		sp()
		sp()

	elif user_choice_is == "3":
		kl()
		sp()
		open_transactions_print()
		sp()
		kl()
		dl()
		sp()
		sp()
		sp()
	
	elif user_choice_is == "4":
		kl()
		sp()
		if mine_block():
			open_transactions = []
		sp()
		kl()
		dl()
		sp()
		sp()
		sp()

	elif user_choice_is == "5":
		kl()
		sp()
		crack_test()
		print("CRACKRD")
		sp()
		kl()
		dl()
		sp()
		sp()
		sp()

	elif user_choice_is == "6":
		kl()
		sp()
		print(participants)
		sp()
		kl()
		dl()
		sp()
		sp()
		sp()

	elif user_choice_is == "7":
		kl()
		sp()
		print("Exit")
		sp()
		kl()
		dl()
		sp()
		sp()
		sp()
		break

	else:
		kl()
		sp()
		print("Invalid Input")
		sp()
		kl()
		dl()
		sp()
		sp()
		sp()
	
	if not crack_detection_system():
		block_chain_elements_print()
		print('Invalid Block Chain')
		break

	print(get_balance("OM DEV SINGH"))

else:
    	print('User Left')		
# END OF WHILE LOOP.

print("All Transactions Saved")
sp()
sp()
fl()
fl()


##########################################################################################################
# END OF PROGRAM
##########################################################################################################