
a={"listed": "Harry" ,
"hardik":"me ",
}
print(a['hardik'])
print(a.keys()) #prints the keys of dictionary


print(type(list(a.keys())))


print(type(a.keys()))
print(a.values()) #prints the values of dictionary


# Printing a nested dictionary
b={"list": "Harry" ,
"hardik":"me ",
"anotherdict":{"aman":"dad"}
}
b["hardik"]=["Zad"] #Changing the values inide a dictionary
print(b["anotherdict"])
print(b["hardik"])

