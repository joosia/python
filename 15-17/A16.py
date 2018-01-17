codes = ["fi", "se", "no"]

codemap = {
    "fi": "finland",
    "se": "sweden",
    "no": "norway"
}

countries = {
    "finland": {
        "head honcho": ("Juha Sipila", 54),
        "population": 5.439
    },
    "sweden": {
        "head honcho": ("Stefan Lofven", 58),
        "population": 9.593
    },
    "norway": {
        "head honcho": ("Erna Solberg", 54),
        "population": 5.084
    }
}

# Loop 3 times
for code in codes:
    # Print Country with key
    print codemap[code] + ":\n", "\t",
    # Print keys and values from inner dictionary
    for key, val in countries[codemap[code]].iteritems():
        # If key is "head honcho" iterate through tuple
        if key == "head honcho":
            for info in countries[codemap[code]]["head honcho"]:
                # If next item is name print 'item + who is', if not print 'item + years old'
                if type(info) == str:
                    print key + ":", info, "who is",
                else:
                    print info, "years old"
        else:
            print "\t", key + ":", val, "million"


            
