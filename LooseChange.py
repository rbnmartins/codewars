def loose_change(cents):
    dic = {'Nickels':0, 'Pennies':0, 'Dimes':0, 'Quarters':0}
    if cents <= 0:
        return dic
    else:
        cents = int(cents)
        dic['Quarters'] = cents // 25
        cents -= cents // 25 * 25
        dic['Dimes'] = cents // 10
        cents -= cents // 10 * 10
        dic['Pennies'] = cents // 5
        cents -= cents // 5 * 5
        dic['Nickels'] = cents // 1
        return dic
