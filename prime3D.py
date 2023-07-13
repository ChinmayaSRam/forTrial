
def check_prime(num):
    if num < 2:
        return False
	
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False

    return True

def prime_composite_list(inp):
    prime = []
    nonp = []
    dList = []
    for x in inp:
        if check_prime(x):
            prime.append(x)
        else:
            nonp.append(x)
    
    dList.append(prime)
    dList.append(nonp)
    return dList
    

if __name__=='__main__':
    inp=[]
    count=int(input())
    for i in range(count):
        inp.append(int(input()))
    #print(check_prime(inp[i]))
    result = prime_composite_list(inp)
    print(result)