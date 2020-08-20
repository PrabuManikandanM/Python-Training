def first_prime (number_1, number_2) :
    
    if(number_1>1):
        for i in range(number_1,number_2):
            if(i==2):
                i=2
                print(i)
                break
            elif(i==3):
                i=3
                print(i)
                break
            elif(i%2==0) or (i%3==0):
                continue
            else:
                break
    return i 
print(first_prime(29,58))