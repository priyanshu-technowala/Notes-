notes = []

while True:
    note = input("Enter your note (or 'q' to quit): ")
    
    if note == "q":
        break
    
    notes.append(note)

print("Physics")
for note in notes:
    print("- " + note)
