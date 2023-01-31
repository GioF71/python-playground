crazy_tuple = (["x", "y"], )
#print(crazy_tuple)
#print(crazy_tuple[0])
crazy_tuple[0] = crazy_tuple[0].__iadd__(["z"])
