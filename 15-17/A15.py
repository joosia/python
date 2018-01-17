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

# Testing
for code in codes:
    print code
for code, country in codemap.iteritems():
    print code, country
for country, info in countries.iteritems():
    print country, info
