"""The login command."""

import pickle
from .base import Base
import random


#This class inherit from the Base class
class Login(Base):
    """Login to the gift exchange event"""
    
    #this method is run when the command "login" is parsed
    def run(self):
        
        #read the guest list stored in memory
	guests=dict()
	with open('gift/obj/guests.pkl', 'rb') as f:
            guests=pickle.load(f)

	recipients=dict()
	with open('gift/obj/recipients.pkl', 'rb') as f:
            recipients=pickle.load(f)
	
	#this block of code runs when the option '--admin' is parsed
	if self.options['--admin']==True:
	    
	    exit=0
	    while(not exit):
	    	is_launch=raw_input('\n[ADMIN MENU]\nDo you want to... \n 1. launch a new exchange? \n 2. view the results of the previous exchange? \n 3. exit this menu? \n')
	    
	        if is_launch=='1':
                    recipients=launch_exchange(guests)
		    with open('gift/obj/recipients.pkl', 'wb') as f:
		        pickle.dump(recipients,f, pickle.HIGHEST_PROTOCOL)
    	        elif is_launch=='2':
		    with open('gift/obj/recipients.pkl', 'rb') as f:
          	        recipients=pickle.load(f)
		    print("\nHere are the exhange results: \n")
		    for key, value in recipients.items():
		        print("->Donor: "+key+"\t\t\tRecipient: "+value+"\n")
		elif is_launch=='3':
		    exit=1
	        else:
	    	    print("Please answer with '1', '2' or '3'.")
		print('\n')

	#this block of code runs when the option '--user' is parsed
	elif self.options['--user']==True:
	    name=raw_input("\nWhat is your name? ")
	    if(name in guests.keys()):
		if(name in recipients.keys()):
		    print("Your recipient is " + recipients[name]+".\n")
		else:
		    print("Sorry " + name+ ", we are still waiting for the organizer to launch the gift exchange")
	    else:
		print("Your name is not on the guest list, please register and wait for the gift exchange to be launched. \n")
	
	#user typed in an invalid option to the command "login" (This is just precaution, the program should raise an error before that)    
	else: 
	    raise ValueError("The login option should be '--admin' or '--user'")

#this function launches the random gift exchange and return a dictionary where the key is the donor and the value is the recipient
def launch_exchange(guests):
    recipients = dict()
    
    #I dont want to be deleting items from a dict as I iterate through it
    guests_copy=list(guests.keys())
    for (key, value) in guests.items():
	incorrect_draw=1
	while incorrect_draw:
	    draw=random.choice(guests_copy)
	    if (draw!=key) and (draw!=value):
	        incorrect_draw=0
	    	recipients[key]=draw
	    	guests_copy.remove(draw)
    return recipients
