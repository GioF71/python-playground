#https://www.linkedin.com/feed/update/urn:li:activity:7114004597790171136/#

a1 = 0.2
a2 = 0.1

expected = 0.3
actual = a1 + a2

if not expected == actual:
    print(f"{a1} + {a2} = {actual}, should have been {expected}, python sucks too.")
else:
    print("Python is awesome")

