def find_duplicates(s):
	"""
	The function takes a string and returns a list of all repeated characters 
	in the string. 
	"""
	duplicates = set()
	duplicates_list = []
	string = set(s)
	for letter in s:
		if letter in string:
			string.remove(letter)
		else:
			duplicates.update(letter)
	
	for duplicate in duplicates:
		duplicates_list.append(duplicate)
		
	return duplicates_list

	# Example test, this does not count as one of your tests
print(find_duplicates("HelloWorld"))
assert find_duplicates("HelloWorld") == (["l", "o"] or ["o", "l"])
	# Write tests below this line. Do not remove.
    # Follow the indent for this comment
assert find_duplicates("MickMiller") == ["M", "i", "l"] or ["M", "l", "i"] or ["i", "M", "l"] or ["i", "l", "M"] or ["l", "M", "i"] or ["l", "i", "M"]
assert find_duplicates("Andrade") == ["d"]
assert find_duplicates("HiGuys") == []
	# Write tests above this line. Do nost remove.

