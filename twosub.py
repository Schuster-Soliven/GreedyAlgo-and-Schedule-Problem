# Schuster Soliven
# 24/02/2023
# Solving Hamiliton Problem using greedy approach and matching group schedules 

from datetime import datetime

# Given city_distances, fuel, and mpg, find optimal start position
# returns an index to optimal starting city
def greedyCity(city_distances = [], fuel = [], mpg = 0) :
    count = 0
    current_index = 0
    index = 0
    curr_fuel = 0
    max_fuel = -100
    best_index = -1
    first_correct = False
    while index <= len(fuel) - 1:
        # keeps track of city start
        count = 0
        print("\nRunning index of city: " + str(index))
        while count < len(fuel) - 1:
            # iterate route for starting city until it passes through n number of cites
            # or runs out of gas. Not constrained by index.
            count += 1
            print("iteration: " + str(count))
            curr_fuel += (fuel[current_index] * mpg)
            # fueling up
            print("Adding fuel, current fuel status: " + str(curr_fuel))
            if curr_fuel <= 0:
                # If refueling isn't enough, move to next best index
                print("Not enough fuel to attempt drive, current fuel status: " + str(curr_fuel))
                if current_index + 1 == len(fuel):
                    # break loop (out of bounds case)
                    curr_fuel = 0
                    current_index = 0
                    break
                else:
                    # break loop
                    curr_fuel = 0
                    current_index += 1
                    break
            else:
                # proceed with drive
                curr_fuel -= city_distances[current_index]
                # calculating gas needed to get to the city
                print("Attempting to go to the next city, fuel status after drive: " + str(curr_fuel))
                if count == len(fuel):
                    # reached starting city
                    first_correct = True
                    break
                elif current_index + 1 == len(fuel):
                    # continue loop (out of bounds case)
                    current_index = 0
                else:
                    # continue loop
                    current_index += 1
            # end of inner loop
        if max_fuel < curr_fuel:
            # compare best options and take best index as best starting city
            max_fuel = curr_fuel
            print("Max fuel is: " + str(max_fuel))
            best_index = index
            print("Best index is: " + str(best_index))
            curr_fuel = 0
        count = 0
        
        curr_fuel = 0
        index += 1
        current_index = index
        if first_correct:
            # instance of first city viable city, break
            break
        # end of outer loop
    return best_index
    #end of function    

#################################################################

# Given 2 people, each with an array of what time they cannot meet up and a range
# of time of earliest to latest to meet up. A minimum duration is given. A list of 
# possible time ranges is returned   
def MatchScedules(p1_sched = [], p1_schedAct = [], p2_sched = [], p2_schedAct = [], duration = 0) :
    # define range (bounds) (Proven)
    bounds = []
    if (p1_schedAct[0] > p2_schedAct[0]):
        bounds.append(p1_schedAct[0])
    else:
        bounds.append(p2_schedAct[0])
    if (p1_schedAct[1] < p2_schedAct[1]):
        bounds.append(p1_schedAct[1])
    else:
        bounds.append(p2_schedAct[1])
    print("Updated Bounds: " + str(bounds))

    # Sort schedule (Proven)
    updated_sched = []
    for i in p1_sched:
        updated_sched.append(i)
    for i in p2_sched:
        updated_sched.append(i)
    updated_sched = sorted(updated_sched, key=lambda d: tuple(map(int, d[1].split(":"))))
    updated_sched = sorted(updated_sched, key=lambda d: tuple(map(int, d[0].split(":"))))
    print("Combined sorted schedule: " + str(updated_sched))

    # Optimizing sorted schedule (Not sure if it'll go out of bounds if not careful)
    index = 0
    max_size = len(updated_sched)
    while index < max_size - 1 :
        if updated_sched[index][1] >= updated_sched[index + 1][0]:
        # compare two values
            #print(str(updated_sched[index]) + " " + str(updated_sched[index + 1]))
            #print(str(updated_sched[index][0]) + " " + str(updated_sched[index + 1][1]))
            temp = [updated_sched[index][0], updated_sched[index + 1][1]]
            updated_sched.insert(index, temp)
            # combine the times
            updated_sched.remove(updated_sched[index+1])
            updated_sched.remove(updated_sched[index+1])
            # remove old time frames
            max_size -= 1
            # removed two time frames, added updated time range
            # will not move to the next index, so as to check again
        else:
            # next index is valid 
            index += 1
    print("Ordered sorted schedule: " + str(updated_sched))
    
    # create a new list but with bounds and accessible times
    inv_schedule = []
    # Inversed of sorted schedule
    bmin = datetime.strptime(bounds[0], '%H:%M')
    bmax = datetime.strptime(bounds[1], '%H:%M')
    for i in range(len(updated_sched)):
        min = datetime.strptime(updated_sched[i][1], '%H:%M')
        if (i == len(updated_sched) - 1):
            if min < bmax:
                inv_schedule.append([updated_sched[i][1], bounds[1]])
                break
        if i != len(updated_sched) - 1:
            max = datetime.strptime(updated_sched[i + 1][0], '%H:%M')
        #print("Min and max: " + str(min) + str(max))
            if min > bmin and max < bmax :
                #print(updated_sched[i][0])
                #print(updated_sched[i + 1][0])
                inv_schedule.append([updated_sched[i][1], updated_sched[i + 1][0]])
    
    # duration implementation
    # tbd

    print("Inversed schedule: " + str(inv_schedule))
    return inv_schedule
    # end of function