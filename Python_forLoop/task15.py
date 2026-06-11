#15. Highest Temperature
"""
Create a list of temperatures recorded during the week and find the highest temperature.
"""
temperatures = [30, 32, 28, 35, 31, 29, 33]

for x in  temperatures :
    if x == max(temperatures) :
        print("Maximum temprature during the week is :",x)