# map()
f = lambda x: x*x
args = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
result = map(f, args)
print(list(result))

# filter()
args = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
f = lambda x: x % 2 == 0  # True/False returning function
result = filter(f, args)
print(list(result))