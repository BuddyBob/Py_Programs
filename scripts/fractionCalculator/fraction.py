import re
def string(string):
    string = re.split('\/|\+',string)
    den1 = int(string[1])
    den2 = int(string[3])
    nume1 =int(string[0])
    nume2 = int(string[2])
    lcm = None
    count = 1
    while True:
        if count % den1 == 0 and count % den2 == 0:
            lcm = count
            break
        count += 1
    nume1 = lcm/den1 * nume1
    nume2 = lcm/den2 * nume2
    print('Your Answer is: {}'.format(str(nume1-nume2)+' / '+str(lcm)))
    print('Your Answer is: {}'.format(str(nume1+nume2)+' / '+str(lcm)))
omg i MAAMMAMMAMAMAMAMAMAMAMAMAMMAMAMAMAMAM


