def is_valid_ip(s):
	if s.isalpha():
		return False
	ldot = s.split(".")
	false_cases = [
	s.count(".") != 3,
	s.startswith("."), 
	s.endswith("."),
	not ("".join(ldot)).isdigit(),
	max([int(i) for i in ldot]) > 255,
	min([int(i) for i in ldot]) < 0,
	len([i for i in ldot if i.startswith("0") and len(i)>2]) > 1,
	len(s)>15,
	len(s)<4,
	]

	return not True in false_cases

print is_valid_ip("")