def speeding_ticket (speed, limit):
    noFine = 0;
    fine1 = 100
    fine2 = 500

    if speed >= limit + 5 and speed < limit + 20:
        boolean = False
        return (fine1, boolean)
    elif speed >= limit + 20:
        boolean = True
        return (fine2, boolean)
    else:
        boolean = False
        return (noFine, boolean)
