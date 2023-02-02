from random import randint 






def basic(cards):
    
    card_vals = []
    for i in cards:
        if (i >= 10) and (i != 11):
            card_vals.append(10)
        elif i == 1:
            card_vals.append(11)
        else:
            card_vals.append(i)

#could recursively go through
    total = sum(card_vals)
    while (total > 21) and (11 in card_vals):
        if (total > 21) and (11 in card_vals):
            for j,i in enumerate(card_vals):
                if i == 11:
                    card_vals[j] = 1
                    total = sum(card_vals)
                    break
    for i in cards:
        print(i,end=', ')
    print()
    print('total = ', total)
        
    return 



for j in range(100):
    vals = []
    for i in range(5):
        vals.append(randint(1,11))
        if (11 in vals) or (1 in vals):
            basic(vals)



