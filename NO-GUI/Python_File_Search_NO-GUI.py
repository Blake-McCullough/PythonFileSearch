#Made By Blake McCullough
#Discord - Spoiled_Kitten#4911
#Github - https://github.com/Blake-McCullough/
#Email - privblakemccullough@protonmail.com


#Importing the module 
import json

#Shows the name of the key
def matchingKeys(dictionary, searchString):
    return [key for key,val in dictionary.items() if any(searchString in s for s in val)]

#Show the name of the string
def matchingStrings(dictionary, searchString):
    return [s for val in dictionary.values() for s in val if searchString in s]

#Loads data from file
def loadData():
  with open('data.json') as json_file: 
    return json.load(json_file)
#Saves data to file
def saveData(data):
  with open('data.json', 'w') as f:
    json.dump(data, f, sort_keys=True, indent=4)
#Adds data to the file
def addData(data, newData):
  for key, items in newData.items():
    if key in data:
      data[key] +=items
    else:
      data[key] = items
  return data
#removes data from file
def removeData(data, removeData):
  for key, items in removeData.items():
    if key in data:
        data[key] = [items for items in data[key] if items not in removeData[key]]
    else:
        #You'll have to remove the item from all boxes if no box is specified
        #Or ask for usr to specify which box to remove said item from
        return NotImplemented
  return data
run = "true"
while run == "true":
    choice = input("What would you like to do?\n 1:Search for an item \n 2:Add an item \n 3:remove an item\n")
    storage = {}

    storage = loadData()

    #print(storage)

    new_dict = {"box1":["item1","item2"],"box3":["item1" ,"item2"]}
    #search
    if choice == "1":
        print(storage)
        value = input("Search for an item\n")
        value = value.lower()
        boxes = matchingKeys(storage,value)
        print(matchingStrings(storage,value))
        #Checks if result is empty
        if [] == boxes:
          print("The item could not be found in any box")
        #If result is not empty then looks for which box it is in
        else:
          if "box1" in boxes:
            print("In Box 1")
          if "box2" in boxes:
            print("In Box 2")
          if "box3" in boxes:
            print("In Box 3")


        
    #add data
    elif choice == "2":
        #Displays the storage for the user to add to
        print(storage)
        box="box"+input("select a box")
        add=input("Please select an item to add")
        new_dict={box:[add]}
        storage = addData(storage, new_dict)
        saveData(storage)
        print("Storage has been updated")
        print("Updated storage system is\n",storage)

        
    #REMOVE DATA
    elif choice == "3":
        print(storage)
        box="box"+input("select a box")
        remove=input("Please select an item to remove")
        remove_dict={box:[remove]}
        storage = removeData(storage, remove_dict)
        saveData(storage)
        print("Storage has been updated")
        print("Updated storage system is\n",storage)


