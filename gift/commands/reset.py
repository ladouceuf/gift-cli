"""The register command."""

import pickle
from .base import Base

#This class inherit from the Base class
class Reset(Base):
    """Reset the gift exchange data"""
    
    #this method is run when the command "reset" is parsed
    def run(self):
	empty=dict()
	with open('gift/obj/guests.pkl', 'wb') as f:
            pickle.dump(empty, f, pickle.HIGHEST_PROTOCOL)
	with open('gift/obj/recipients.pkl', 'wb') as f:
            pickle.dump(empty, f, pickle.HIGHEST_PROTOCOL)
	
