#letter=''' dear <|name|>
#    You are selected.
#        <|date|>'''
#
#    print(letter.replace("<|name|>", "Ahmad").replace("<|date|>", "10 August 2025"))
#name = "Ahmad  Raza"
#print(name.replace("  ", " "))
letter="Dear Ahmad, \n You are selected. \n 10 August 2025"
print(letter.replace("Ahmad", "Ali").replace("10 August 2025", "11 August 2025"))