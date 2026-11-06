word = input("Enter a word: ")
reverse_word = word[::-1]
if word == reverse_word:
    print("Palindrome")
else:
    print("Not a palindrome")