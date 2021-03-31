import json
import tkinter
from tkinter import *
  




#Made By Blake McCullough
#Discord- Spoiled_Kitten#4911
#Github- https://github.com/Blake-McCullough/


def raise_frame(frame):
    frame.tkraise()


root = Tk()
root.title("You're a Nice Person")
root.geometry("1280x500")
#CODE GOES UNDER HERE
f1 = Frame(root)
f2 = Frame(root)
f3 = Frame(root)
f4 = Frame(root)
text_box = tkinter.StringVar()

#Shows the name of the key
def matchingKeys(dictionary, searchString):
    return [
        key for key, val in dictionary.items()
        if any(searchString in s for s in val)
    ]


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
            data[key] += items
        else:
            data[key] = items
    return data


#removes data from file
def removeData(data, removeData):
    for key, items in removeData.items():
        if key in data:
            data[key] = [
                items for items in data[key] if items not in removeData[key]
            ]
        else:
            #You'll have to remove the item from all boxes if no box is specified
            #Or ask for usr to specify which box to remove said item from
            return NotImplemented
    return data


#Importing the module
storage = {}

storage = loadData()

new_dict = {"box1": ["item1", "item2"], "box3": ["item1", "item2"]}




#CANNOT REMOVE THE TEXT AFTER ONE SEARCH IS DONE
def search_input():
    text_box.set("loading...")
    boxes = "-----------------------------------------"
    Item = "-----------------------------------------"
    l2=Label(f2, text=boxes)
    l2.grid(row=15, column=5)
    l1=Label(f2, text=Item)
    l1.grid(row=12, column=5)
    search_result = searchbox.get()
    print("Button Pressed")
    #Displays the storage for the user to add to
    #print(storage)
    boxes = matchingKeys(storage, search_result)
    Label(f2, text=text_box).grid(row=13, column=5)

    if [] == boxes:
      print("The item could not be found in any box")
      boxes = "-----------------------------------------"
      Item = "-----------------------------------------"
      l2=Label(f2, text=boxes)
      l2.grid(row=15, column=5)
      l1=Label(f2, text=Item)
      l1.grid(row=12, column=5)



      # SET THE BOX VARIABLE
      text_box.set("The item could not be found in any box")
    #If result is not empty then looks for which box it is in
    else:
        text_box.set("The item could be found")
        l2=Label(f2, text=boxes)
        l2.grid(row=15, column=5)
        Item = matchingStrings(storage, search_result)
        l1=Label(f2, text=Item)
        l1.grid(row=12, column=5)

        
        
        if "box1" in boxes:
            print("In Box 1")
        if "box2" in boxes:
            print("In Box 2")
        if "box3" in boxes:
            print("In Box 3")
    l3=Label(f2, textvariable=text_box)
    l3.grid(row=13, column=5)
    #l3.delete()
    root.update_idletasks()
    
    
def remove_items():
    #Loads Storage Data
    storage = {}
    storage = loadData()
    box = search1.get()
    remove = search3.get()
    remove_dict = {box: [remove]}
    storage = removeData(storage, remove_dict)
    saveData(storage)
    Label(f4, text=remove_dict).grid(row=12, column=5)
    Label(f4, text="Was removed sucessfully").grid(row=13, column=5)


def add_items():
    #Loads storage Data
    storage = {}
    storage = loadData()
    box = search1.get()
    add = search3.get()
    new_dict = {box: [add]}
    storage = addData(storage, new_dict)
    saveData(storage)

    Label(f3, text=new_dict).grid(row=12, column=5)
    Label(f3, text="Was added sucessfully").grid(row=13, column=5)


for frame in (f1, f2, f3, f4):
    frame.grid(row=0, column=0, sticky='news')

#Home Page
Label(f1, text='Home').pack()
Button(f1, text='Search', command=lambda: raise_frame(f2)).pack()
Button(f1, text='Add', command=lambda: raise_frame(f3)).pack()
Button(f1, text='Remove', command=lambda: raise_frame(f4)).pack()





#Search Page
Label(f2, text='Search').grid(row=1, column=5)
Button(f2, text='Back', command=lambda: raise_frame(f1)).grid(row=1, column=1)

search = Label(f2, text="Enter item you wish to search for")
search.grid(row=4, column=5)

searchbox = Entry(f2, bd=5)
searchbox.grid(row=5, column=5)

Button(f2, text='search', command=search_input).grid(row=6, column=5)















#Add Page
Label(f3, text='Add').grid(row=1, column=5)
Button(f3, text='Back', command=lambda: raise_frame(f1)).grid(row=1, column=1)
#Search Box Text
search = Label(f3, text="Enter box you wish to add to")
search.grid(row=4, column=5)

#First Search Box
search1 = Entry(f3, bd=5)
search1.grid(row=5, column=5)

#Search Box Text
search2 = Label(f3, text="Enter item you wish to add")
search2.grid(row=6, column=5)

#Second Search Box
search3 = Entry(f3, bd=5)
search3.grid(row=7, column=5)

Button(f3, text='add', command=add_items).grid(row=8, column=5)

#Remove Page
Label(f4, text='Remove').grid(row=1, column=5)
Button(f4, text='Back', command=lambda: raise_frame(f1)).grid(row=1, column=1)
search = Label(f4, text="Enter box you wish to remove from")
search.grid(row=4, column=5)

#First Search Box
search1 = Entry(f4, bd=5)
search1.grid(row=5, column=5)

#Search Box Text
search2 = Label(f4, text="Enter item you wish to remove")
search2.grid(row=6, column=5)

#Second Search Box
search3 = Entry(f4, bd=5)
search3.grid(row=7, column=5)

Button(f4, text='Remove', command=remove_items).grid(row=8, column=5)

raise_frame(f1)

#KEEP CODE ABOVE HERE
root.mainloop()
