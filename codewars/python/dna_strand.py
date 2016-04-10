def toggle(N):
	if N=="A":
		return "T"
	elif N=="C":
		return "G"
	elif N=="T":
		return "A"
	elif N=="G":
		return "C"
	return None

def dna_strand(dna):
	return "".join(map(toggle, dna))

print dna_strand("AGCTAAA")
