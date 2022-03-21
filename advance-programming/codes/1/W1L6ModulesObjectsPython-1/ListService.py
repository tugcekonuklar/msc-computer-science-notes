#This module is the start of useful list manipulation functions

# 1. generates a list of indices that are 
# the postions in the list toSearch of every instance
# of the given ftoFind object
# Returns a list on indices or a list containing
# -1 if no instaces are found
def find (toSearch, toFind):
    found = []
    index = 0
    count= 0
    
    while index < len(toSearch):
        if toSearch[index] == toFind:
            found.append(index)
            count += 1
        index += 1
    if count == 0:
        found.append(-1)
    return found
    

#2. Converts any sting that is a value to 
# an integer representation of that value
# returns a new list object, the object passed into 
# the function is untouched
# If there is a string that cannot be converted
# or any other object returns a list containing -1
def convertToInts(convert):
    allInts = []
    for i in convert:
        if type(i) == str:
            try:
                allInts.append(int(i))
            except ValueError:
                allInts = [-1]
                break
        elif type(i) == int:
            allInts.append(i)
        else:
            allInts = [-1]
            break
    return allInts 



#3. Removes all instances of a given object.
# If the object is not found simply returns a copy of 
# the original list   
def clean(toClean, toRemove):
  cleaned = toClean
  indexes = find(toClean, toRemove)
  removed = 0 ;
  if indexes[0] != -1:
      for i in indexes:
          print(i)
          cleaned.pop(i-removed)
          removed =+ 1
  return cleaned
              
