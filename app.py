import json
from difflib import SequenceMatcher


data = json.load(open('data.json', 'r'))

def search_in_data(w):
	w = w.lower()
	if w in data:
		for i in data[w]:
			print("Meaning: "+i)
		return
	else:
		for k in data:
			if SequenceMatcher(None, w, k).ratio()>0.85:
				yesno = input("Word not found. Do you mean '" + k + "'?" +
				"\n Please Enter y/n: ")
				if yesno.lower() == 'y' :
					for i in data[k]:
						print("Meaning: "+i)
				elif yesno.lower() == 'n' :
					print("The given word '" + w + "' does not exist. Please check again.")
				else:
					print ("Wrong Input")
				return
		print("The given word '" + w + "' does not exist. Please check again.")
		return
	
word = input("Enter Word: ")

search_in_data(word)