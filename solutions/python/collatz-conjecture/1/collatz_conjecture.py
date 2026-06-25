def steps(number):
    if number<=0:
        raise ValueError("Only positive integers are allowed")
    else:
        steps_taken=0
        while number!=1:
            if number%2==0:
                number=int(number/2)
            else:
                number=(number*3)+1
            steps_taken=steps_taken+1
        return steps_taken
            
