from twosub import *

city_distances_A = [5, 25, 15, 10, 15]
fuel_A = [1, 2, 1, 0, 3]
mpg_A = 10

print("Testing problem 1: Greedy Approach to Hamilton problem\n")
ans = greedyCity(city_distances_A, fuel_A, mpg_A)
print("The preferred starting city for the sample above is city " + str(ans))

#################################################################################

person1_Schedule =[[ '7:00', '8:30'], ['12:00', '13:00'], ['16:00', '18:00']]
person1_DailyAct = ['9:00', '19:00']

person2_Schedule = [[ '9:00', '10:30'], ['12:20', '14:30'], ['14:00', '15:00'], ['16:00', '17:00' ]]
person2_DailyAct = ['9:00', '18:30']
duration_of_meeting = 30

print("\nTesting problem 2: Group Schedule Problem\n")
ans = MatchScedules(person1_Schedule, person1_DailyAct, person2_Schedule, person2_DailyAct, duration_of_meeting)

print(ans)