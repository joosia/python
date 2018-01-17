testDict = {}

testName = "li1"

testElement = "el1"

# function takes a dict, a list name and the element
def add_to_list_in_dict(thedict, listname, element):
    # Check if list exists...
    try:
        l = thedict[listname]
    # If the list doesn't exist, create one and prompt user
    except KeyError:
        thedict[listname] = []
        print("Created %s." % listname)
    # ... and print the lenght of it
    else:
        print("%s already has %d elements." % (listname, len(l)))
    # Add element and prompt user
    finally:
        thedict[listname].append(element)
        print("Added %s to %s." % (element, listname))

add_to_list_in_dict(testDict, testName, testElement)
