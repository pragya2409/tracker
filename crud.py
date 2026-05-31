items=[]
def addItem(name):
    items.append(name)
    return f"{name} added"
def deleteItem(index):
    items.pop(index)
    return "deleted"
def updateItem(index,n_name)
    items[index] = n_name
    return f"{n_name} updated"
def readItems():
    return items