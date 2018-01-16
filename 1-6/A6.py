persons = {
    1 : "alice",
    2 : "bob",
    3 : "craig",
    4 : "dave",
    5 : "elisabeth",
    6 : "frank",
    7 : "george"
}

for index, name in persons.iteritems():
    if index % 2 == 0:
        print index, ":", name
