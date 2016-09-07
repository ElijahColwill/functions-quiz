
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
print not_string("Not cool? ")
print not_string("Cool. ")

# TODO - write icy_hot

# TODO - write closer_to

# TODO - write two_as_one

# TODO - write pig_latinify
