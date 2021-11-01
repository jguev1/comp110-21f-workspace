"""Demonstrations of dic capabilities"""

# Declaring the type of a dictionary
schools: dict[str, int]

# Initialize to an empty dictionary
schools = dict()

# Set a key-value pairing
schools["UNC"] = 19400
schools["Duke"] = 6717
schools["NCSU"] = 26150

print(schools)

#Access a value by its key -- lookup

print(f" UNC has {schools['UNC']} students")

# Remove a key-value pair from a dictionary
schools.pop("Duke")

# test for the existence of a key
is_duke_present: bool = "Duke" in schools

# Demonstration of dictionary literals

#Empty dictionary literal
schools = {} #same as doing schools = dict()

# Alternitively initizalize key-value pairs

schools = {"UNC": 19400, "Duke": 6717, "NCSU": 26150}

for school in schools:
    print(f" Key: {school} -> Value: {schools[school]}")
