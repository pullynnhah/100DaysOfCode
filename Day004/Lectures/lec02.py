states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia",
                     "Connecticut", "Massachusetts", "Maryland",
                     "South Carolina", "New Hampshire", "Virginia", "New York",
                     "North Carolina", "Rhode Island", "Vermont", "Kentucky",
                     "Tennessee", "Ohio", "Louisiana", "Indiana",
                     "Mississippi", "Illinois", "Alabama", "Maine", "Missouri",
                     "Arkansas", "Michigan", "Florida", "Texas", "Iowa",
                     "Wisconsin", "California", "Minnesota", "Oregon",
                     "Kansas", "West Virginia", "Nevada", "Nebraska",
                     "Colorado", "North Dakota", "South Dakota", "Montana",
                     "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma",
                     "New Mexico", "Arizona", "Alaska", "Hawaii"]

print(states_of_america[0])
print(states_of_america[1])
print(states_of_america[2])
print()

print(states_of_america[-1])
print(states_of_america[-2])
print(states_of_america[-3])
print()

states_of_america[2] = "Pencilvania"
print(states_of_america)
print()

states_of_america.append("Angelaland")
print(states_of_america)
print()

states_of_america.extend(["Paulaland", "Jack Bauer Land"])
print(states_of_america)
print()
