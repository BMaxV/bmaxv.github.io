

import random

i_series = [("simple I","ji-"),("me","-"),("you","qa-"),("he it","vi-"),("us","-"),("plural you","Sa-"),("them","vi-")]

you_series = [("simple you","bi"),("me","cho-"),("you","-"),("he it","Da-"),("us","ju-"),("plural you","-"),("them","Da-")]

hesheit_series = [("simple he","-"),("me","mu-"),("you","Du-"),("he","-"),("us","nu-"),("plural you","li-")("them","-")]

we_series = [("simple we","ma-"),("me","-"),("you","pI"),("he it","wI"),("we","-"),("plural you","re"),("them","DI")]

you_plural_series = [("simple plural you","Su-"),("me","tu-"),("you","-"),("he it","bo-"),("we","che-"),("plural you","-"),("them","bo-")]

they_series = [("simple they","-"),("me","mu-"),("you","nI-"),("he it","lu-"),("us","nu-"),("plural you","li-"),("them","-")]

all_series={
        "i series":i_series,
        "you_series":you_series,
        "hesheit_series":hesheit_series,
        "we_series":we_series,
        "you_plural_series":you_plural_series,
        "they_series":they_series,}


# while not passed
# only test one person.
# then periodically go back
# also repeat the rule
correct={}
active_series="i series"
while True:
    
    active_test=random.choice(all_series[active_series])

    a_list=[active_test]
    c = 0
    m= 3
    while c<m:
        other_test=random.choice(all_series[active_series])
        if other_test not in a_list:
            a_list.append(other_test)
            c+=1

    random.shuffle(a_list)
    print(active_series)
    print(active_test[0])
    c=0
    for x in a_list:
        print(c,x[1])
        c+=1

    r=input("your answer:")
    try:
        r=int(r)
    except:
        continue

    if a_list[r][1] == active_test[1]:
        print("correct\n")
        if active_test not in correct:
            correct[active_test]={"correct":1,"wrong":0}
        else:
            correct[active_test]["correct"]+=1
    else:
        print("wrong\n")
        if active_test in correct:
            correct[active_test]["wrong"]+=1

    print(active_test)
    print("\n\n")






    

