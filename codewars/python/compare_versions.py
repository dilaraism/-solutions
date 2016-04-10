def compare_versions(ver1, ver2):
	return [int(i) for i in ver1.split(".")] >= [int(i) for i in ver2.split(".")]
	



print compare_versions("11.2", "10.4.3")
print compare_versions("11.2.10", "11.2.9")
print compare_versions("11.2.19", "11.2.19")