from localWeather import LocalWeather

def main():
    '''
    invoke the LocalWeather class to create instances of local weather reports
    '''
    # if there are any weather reports in the text file, then print them out
    try:
        fin = open('weather.txt', 'rt') # read text
        old_weather = fin.read()
        print('Old Weather Reports:')
        print(old_weather)
    except Exception as err:
        pass
    w_edi = LocalWeather('Belfast', 'uk', 'rainy', -3.7)
    w_gal = LocalWeather('Athlone', 'ie', 'humid', 5)
    w_kt = LocalWeather('Kingston', 'jm', 'sunny', 32)
    w_default = LocalWeather('Utopia', '__', True)
    # lets see the instances
    print(w_edi)
    print(w_gal)
    print(w_kt)
    print(w_default)
    # also write the instances to a text file
    fout = open('weather.txt', 'at') # append text
    print(w_edi, file=fout)
    print(w_gal, file=fout)
    print(w_kt, file=fout)
    print(w_default, file=fout)
    fout.close()

if __name__ == '__main__':
    main()

