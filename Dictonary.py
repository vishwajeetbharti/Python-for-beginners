myDictionary={
    "Run": "Run away",
    "Come": "Going to near",
    "dictonary2": {
        "Vishwajeet": "The Coder"
    }
}
 
print(myDictionary["Run"])
print(myDictionary["dictonary2"])
print(myDictionary["dictonary2"]["Vishwajeet"])
myDictionary["dictonary2"]["Vishwajeet"]="Yukthi" #it will change the previous value
print(myDictionary["dictonary2"]["Vishwajeet"])

# Mathodes of Dictionary
print(myDictionary.keys())  #it will print all keys of dictionary in dict_key Data type
print(list(myDictionary.values()))#it will print all Value of dictionary in list data type
print(myDictionary.items())#it will print all Keys and value of dictionary

newDictionary={
    "chandan": "Freind",
    "subham":"Freind"
}
myDictionary.update(newDictionary) # it will update the key's value and also add new keys with value
print(myDictionary)

print("\n"+myDictionary.get("subham"))# it will print the value of the given key
print("\n"+myDictionary["subham"])# it will print the value of the given key

#print("\n"+myDictionary.get("subham1")) it will print the value of the given key,if key hasn't present in the dictioary then return none type
#print("\n"+myDictionary["subham1"]) it will print the value of the given key,if key hasn't present in the dictioary then throws an error 