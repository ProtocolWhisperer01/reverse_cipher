############################################################################
## 									   ##
##	Title : Reverse Cipher 						   ## 	
##									   ##
##	Author : Ernest Odhiambo Elnino					   ##
##									   ##
##	Github : https://github.com/ProtocolWhisperer01 		   ##
#############################################################################

# A simple reverse cipher.
# Simpler ways I could have used are the reverse() method and string[::-1] :smiley:

word = input(" I do reversals, enter something 😐️ : ")

num = len(word)

while num > 0:
	letter = word[num-1]
	num -= 1
	print(letter, end="")
	
	
