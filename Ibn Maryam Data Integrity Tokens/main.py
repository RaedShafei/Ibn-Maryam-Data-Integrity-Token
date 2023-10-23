import hashlib
import piexif
from docx import Document

##############################################################################
#                                   NOTE:                                    #
# This is a test for The Ibn Maryam Data Integrity Token.                    #
# This is not the final Version since it is under development.               #
# Designed and Developed by Raed Omar Shafei.                                #
# Please feel free to tell me your thoughts & suggestions.                   #
# For further questions you can find me at:                                  #
# Twitter: @JustRaed0 email: rshafei@stetson.edu or IbnOmarShafei@gmail.com  #
# Linked in: Raed Shafei                                                     #
##############################################################################

# The way Ibn Maryam Data Integrity Token works is by generating a public token,
# and a private token. The public token includes the hash of the file, the authors name,
# and the date. on the other hand the private token is the hash of the public token.
# As mentioned earlier we are still working on developing it.

fileName = input("Enter file name: ") # Make sure that the file is in the same Dir
author = input("Enter Authors name: ")
fileDate = input("Enter the date: ")
file = fileName
file1 = file.encode("UTF-8")
file2 = file1
print(file2)

hfile = hashlib.sha256(file2).hexdigest() # hashes the file for the first part of the token


author = str(author) # 2nd part of the token AUTHOR
fileDate = str(fileDate) # 3rd part of the token DATE
PubT = hfile + author + fileDate
PubT = PubT.encode("UTF-8")
PriT = hashlib.sha256(PubT).hexdigest()

print('Your public token: ', PubT)
print('Your private token: ',PriT)



