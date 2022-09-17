dict1={"key1":1,"key2":"value2",3:"value3"}
#print(dict1.keys())  # all the keys are printed
#@print(dict1.values()) # all the values are printed
dict1["key1"]="replace_one"  # value assigned to key1 is replaced
#print(dict1)
print(dict1["key2"])
print(type(dict1["key2"]))