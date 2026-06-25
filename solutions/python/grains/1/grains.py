def square(number):
    if number>=1 and number<=64:
        grain=2**(number-1)
        return grain 
    else:
        raise ValueError("square must be between 1 and 64")
    
def total():
    totalgrain=0
    square=1
    while square <=64:
        totalgrain=totalgrain+(2**(square-1))
        square=square+1
    return totalgrain