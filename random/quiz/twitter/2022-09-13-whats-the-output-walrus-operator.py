number = 10
lots_of_numbers = [number for x in
                   range(5, 100, 2)
                   if (number := x)]

print(lots_of_numbers)
print(number)
