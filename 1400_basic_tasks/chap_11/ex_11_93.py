def cars_bikes_mean(prices:list) -> bool:
    cars = [x for x in prices if x > 5000]
    bikes = [x for x in prices if x <= 5000]
    cars_mean = sum(cars) / len(cars)
    bikes_mean = sum(bikes) / len(bikes)
    return(cars_mean / bikes_mean > 3)