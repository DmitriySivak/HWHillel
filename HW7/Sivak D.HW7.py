def get_season(month):
    if month < 3 or month  == 12:
        return "Winter"
    if 3 <= month < 6:
        return "Spring"
    if 6 <= month < 9:
        return "Summer"
    if 9 <= month < 12:
        return "Autumn"
counting = 1
while counting<13:
    print(counting)
    print(get_season (counting))
    counting+=1