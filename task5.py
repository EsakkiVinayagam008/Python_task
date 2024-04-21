def reverse(word: str) -> str:
    return word[::-1]

user_value = input("Enter a word: ")
word = reverse(user_value)
print("Reversed word:", word)


