from celcius import convert, temperatures

def create_file():
    file = open('convert_results.txt', 'w')
    for temp in temperatures:
        res = convert(temp)
        if(type(res) != str):
            file.write(str(res)+'\n')

    file.close()

create_file()
