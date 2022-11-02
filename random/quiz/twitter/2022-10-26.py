letters = ["a"]

class Character:
    letters = ["b"]
    letters = letters + ["c"]

print(letters[0], Character.letters)
