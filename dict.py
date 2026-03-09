d={} #empty dictionary
marks = {
    "Ahmad" : 100,
    "yousaf": 99,
      "Ali" : 56
}
#print(marks, type(marks))
#print(marks.items())
#print(marks.keys())
marks.update({"Ali": 80, "Ahmad": 90, "yousaf": 70})
#print(marks)
print(marks.get("Ali")) #print none
print(marks["Ahmad"]) #print Error