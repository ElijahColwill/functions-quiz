
def has_teen(a, b, c):
	return (a >= 13 and a <= 19) or (b >= 13 and b <= 19) or (c >= 13 and c <= 19)

print has_teen(11, 14, 18)
print has_teen(12, 2, 19)
print has_teen(12, 2, 11)

def not_string(str):
	if str.startswith("Not") or str.startswith("not"):
		return str + "not"
	else: return "not" + str

print not_string(" welcome here.")
print not_string("Not welcome here? ")

def icy_hot(temp1, temp2):
	return temp1 > 100 or temp2 > 100 or temp1 < 0 or temp2 < 0

print icy_hot(-1, 112)
print icy_hot(1, 99)
print icy_hot(-1, 99)
print icy_hot(101, 1)
print icy_hot(-1, -2)
print icy_hot(101, 101)

def closer_to(g, a, b):
	if abs(a) > abs(g) or abs(b) > abs(g):
		if abs(g) - abs(a) > abs(g) - abs(b):
			return a
		if abs(g) - abs(b) > abs(g) - abs(a):
			return b
	if abs(a) < abs(g) or abs(b) < abs(g):
		if abs(g) - abs(a) < abs(g) - abs(b):
			return a
		if abs(g) - abs(b) < abs(g) - abs(a):
			return b
	else: return 0

print closer_to(5, 6, 10)
print closer_to(6, 10, 5)
print closer_to(-7, -8, -8)
print closer_to(-7, -8, -11)

def two_as_one(a, b, c):
	return (a + b) == c or (a + c) == b or (c + b) == a

print two_as_one(4, 3, 7)
print two_as_one(7, 4, 3)
print two_as_one(4, 7, 3)
print two_as_one(1, 7, 11)
print two_as_one(-4, -1, -5)
