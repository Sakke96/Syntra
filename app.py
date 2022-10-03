# print('')
# x = '5'
# y = 5
# z = 5.0

# leeftijd = int(input('leeftijd: '))

# def print_leeftijd():
#     leeftijd = int(input('leeftijd: '))
#     print(leeftijd)

# # def print_leeftijd(a):
#     #leeftijd = int(input('leeftijd: '))
#     print(a)
# leeftijd = int(input('leeftijd: '))
# print_leeftijd(leeftijd)

# def old_enough_to_drive(leeftijd):
#     if leeftijd >= 18:
#         print("oud genoeg om te rijden")
#     else:
#         print("mag nog niet rijden")

# import math

# def calculate_square(getal):
#     square = math.sqrt(getal)
#     print(square)

lijst = [1,2,3,4,5,6,7,8,9]

def aantal_kleiner_dan_vijf(lijst):
    kleiner = 0
    for i in lijst:
        if i < 5:
            kleiner += 1
    print(kleiner)
aantal_kleiner_dan_vijf(lijst)
            