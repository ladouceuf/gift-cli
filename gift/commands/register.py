"""The register command."""

import pickle
from .base import Base

#This class inherit from the Base class
class Register(Base):
    """Register to the gift exchange event"""

    #this method is run when the command "register" is parsed
    def run(self):

	#warning for user
	print("\n**********************************************************************************************************\nWARNING\nAny changes to the guest list performed after the draw will not be taken into account until the next draw.\nThe changes (add/removal of a name) will appear on the results of the next gift exchange.\n**********************************************************************************************************\n")
	#read the guest list stored in memory
	guests=dict()    
   	with open('gift/obj/guests.pkl', 'rb') as f:
            guests=pickle.load(f)
	
	#this block of code runs when the option '--add_name' is parsed
	if(self.options['--add_name']):
	    name=raw_input('\nWhat is your name? ') 
	    while True:
		is_partner=raw_input('Do you have a partner? [Y/n] ')
		is_partner=is_partner.lower()
	    	if is_partner=='y' or is_partner=='yes':
	            partner=raw_input('What is his/her name? ')
		    print('\n')
	            guests[name]=partner
		    print("Please make sure that your partner registers too.\n")
		    break
    	        elif is_partner=='n' or is_partner=='no':    
	           print('No worries, there are plenty of fishes in the sea!\n')
	           guests[name]=None
		   break	
	        else:
	            print("You must answer by 'Y' or 'n'")
	
	
	#this block of code runs when the option '--remove_name' is parsed
	elif(self.options['--remove_name']):
	    name=raw_input('\nWhat is your name? ')
	    if name in guests.keys():
    	        del guests[name]
		print("Your name has been removed from the guest list.\n")
	    else: 
		print("Could not remove your name, it does not appear on the guest list.\n")

	#user typed in an invalid option to the command "register" (This is just precaution, the program should raise an error before that)    
	else:
	    raise ValueError("The register option should be '--add_name' or '--remove_name'")
	
	#write the guest list back to memory	
	with open('gift/obj/guests.pkl', 'wb') as f:
            pickle.dump(guests, f, pickle.HIGHEST_PROTOCOL)
