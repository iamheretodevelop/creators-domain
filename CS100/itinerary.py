def flights(itinerary):
    journey = []
    for flight in range(len(itinerary)):
        start = itinerary[flight][0]
        is_start = True
        for place in range(len(itinerary)):
            if start == itinerary[place][1]:
                is_start = False
        if is_start == True:
            break
    
    journey.append(start)
    next_start = start
    for j in range(len(itinerary)):
        for i in range(len(itinerary)):
                if itinerary[i][0] == next_start:
                    next_start = itinerary[i][1]
                    journey.append(next_start)
    
    return journey

a = [['HNL', 'AKL'], ['AKL', 'ORD'], ['SFO', 'HNL']]
print(flights(a))