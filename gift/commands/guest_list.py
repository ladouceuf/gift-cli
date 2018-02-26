"""The guest_list command."""

import pickle
from .base import Base

#This class inherit from the Base class
class GuestList(Base):
    """Print out the guest list"""
    
    #this method is run when the command "guest_list" is parsed
    def run(self):
	
	#load the guest list from memory
	guests=dict()
	with open('gift/obj/guests.pkl', 'rb') as f:
            guests=pickle.load(f)
	
	print("\nHere is the guest list:")
	for item in guests.items():
	    print("->Guest: " +  item[0] + "\t\t\tPartner: " + str(item[1]))
	print("\n")