
def smpTotal(rolls,choices):
    if type(rolls) != int or type(choices) != list:
        print('arguments (x,y) must be (str,int)')
        exit()
    sample_space = rolls * len(choices)
    return 'Sample Space:{}'.format(sample_space)
def smpAnd(rolls,choices,):
    sample_space = rolls * len(choices)
    return('{}'.format('1/'+str(sample_space))) 