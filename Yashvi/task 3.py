word = input("Enter a word:")
upper = word.upper()
reverse = word[::-1]
length = len(word)
if word.lower() == reverse.lower():
    palindrome = True
else:
    palindrome = False
code = (ord(word[0]))
middle = length//2
middle_letter = word[middle]

print (word)
print (upper)
print (palindrome)
print (length)
print (code)
print (middle_letter)