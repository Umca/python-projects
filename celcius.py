temperatures=[10,-20,-289,100]

def convert(celsius):
    if celsius < -273.15:
        res = 'It is not possible'
    else:
        fahrenheit = celsius * 1.8 + 32
        res = fahrenheit
    return res

def print_results():
    for temp in  temperatures:
        print(convert(temp))
