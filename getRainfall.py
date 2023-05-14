def get_rainfall():

    records = {}
    while True:
        
        city = input("Enter a city. ")
        if not city:
            break
        
        rainfall = int(input("How much rain in mm has fallen in that city? "))
        records[city] = records.get(city, 0) + rainfall # .get(city, 0) sets default city value to zero

    # print report - total rainfall in each city
    for city, rain in records.items():
        print(f'{city}: {rain}')
        

get_rainfall()

        


