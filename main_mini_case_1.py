data = input('Введите объём бензина в галлонах: ')

coef_gallon_litre = 3.79
coef_barrel = 19.5
coef_co2 = 20
coef_petrol_BTU = 115000
coef_ethanol_BTU = 75700
petrol_price_dollars = 3
cars_per_men = 0.293
NSK_popul = 1618039
Russia_popul = 146780720
exchange_rate = 64.26
petrol_per_men_per_day = 0.8
year = 365

volume_petrol_litre = int(data) * coef_gallon_litre
barrels_needs = int(data) / coef_barrel
volume_co2 = int(data) * coef_co2
volume_ethanol = (coef_ethanol_BTU / coef_petrol_BTU) * int(data)
petrol_cost = int(data) * petrol_price_dollars
consumption_petrol_NSK_per_day = volume_petrol_litre * petrol_per_men_per_day * NSK_popul * cars_per_men
consumption_petrol_Russia_year = volume_petrol_litre * petrol_per_men_per_day * Russia_popul * year
petrol_cost_rub = petrol_cost * exchange_rate


print('Объем бензина в литрах составляет ' + str(volume_petrol_litre) + '.')
print('Кол-во баррелей для получения бензина равно ' + str(format(barrels_needs, '.2f')) + '.')
print('Выделяемое кол-во углекислого газа в двигателе, в фунтах, составляет ' + str(volume_co2) + '.')
print('Эквивалетный объём этанола в галлонах составляет ' + str(format(volume_ethanol, '.2f') + '.'))
print('Стоимость бензина в долларах США ' + str(petrol_cost) + ', а в рублях '
      + str(format(petrol_cost_rub, '.2f')) + '.')
print('В Новосибирске ежедневно потребляется ' + str(format(consumption_petrol_NSK_per_day, ',.0f'))
      + ' литров бензина ' + 'и ' + str(format(consumption_petrol_Russia_year, ',.0f'))
      + ' литров в год по России в целом.')
