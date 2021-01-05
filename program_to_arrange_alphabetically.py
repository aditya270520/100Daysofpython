my_str = "Aditya Bhushan Sharma is the king and being champion"

words = [word.lower() for word in my_str.split()]

words.sort()

print("The sorted words are:")
for word in words:

  print(word)