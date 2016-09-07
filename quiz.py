
def has_teen(a, b, c):
	return (a >= 13 and a <= 19) or (b >= 13 and b <= 19) or (c >= 13 and c <= 19)

print has_teen(11, 14, 18)
print has_teen(12, 2, 19)
print has_teen(12, 2, 11)

def not_string(str):
	if str.startswith("Not") or str.startswith("not"):
		return str + "Not"
	else: return "Not" + str

print not_string(" welcome here.")
print not_string("Not welcome here? ")

def icy_hot(temp1, temp2):
	return (temp1 > 100 or temp2 > 100) or (temp1 < 0 or temp2 < 0)

print icy_hot(-1, 112)
print icy_hot(1, 99)
print icy_hot(-1, 99)
print icy_hot(101, 1)

# TODO - write closer_to

# TODO - write two_as_one

# TODO - write pig_latinify
