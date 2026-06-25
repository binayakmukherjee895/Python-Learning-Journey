def is_armstrong_number(number):

    """ okah so here i will describe what i have done :
    1. the function is_armstrong_number has a parameter i.e. number , so i have taken a variable and typecasted the number variable into a string so that i can take the length of the number (eg. 153= 3,9474=4) with the help of len()
    2. then declared a variable original_number = number as number will get truncated in the next few steps...
    3.now initialized sum_of_digits= 0 , then started the loop , loops does its job ... then implemented the logic to check whether its armstrong or not
    4. declared new variable digit which holds all the last digit of the number (number%10) followed by truncating last digit with // 10.
    5.checked whether sum_of_digits==original_number or not ... and then HERE U GOOO 
    
    """
    n=str(number)
    power=len(n)

    original_number=number
    sum_of_digits=0
    while number>0:
        digit=number%10
        sum_of_digits=sum_of_digits+digit**power
        number=number//10
    if sum_of_digits==original_number:
        return True
    else:
        return False

   

     
        