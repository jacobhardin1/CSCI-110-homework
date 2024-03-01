## Strings are text-based
## Strings can be numbers, letters, special characters, etc
## COmmon methods: upper, lower, swapcase, capitalize, endswith,
## isdigit, etc

##string = "hellp world".capitalize()
##print(string)

##string = string.upper()
##print(string)

##string = string.swapcase()
##print(string)

ss = "Name Here"
a, b = ss.split()
print(a)
print(b)

last_first = f"{b}, {a}"

print(last_first)


## Slicing

s = "pie rats of the carry bean"
s[len(s)-1]
print(len(s))
print(s[::-1])
print(s[5:1:-1])
