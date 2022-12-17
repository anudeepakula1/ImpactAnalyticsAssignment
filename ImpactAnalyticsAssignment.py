

def factorial(n):
    if n == 0:
        return 1
    fct = 1
    for i in range(2,n+1):
        fct*=i
    return fct

def ncr(n,r):
    return factorial(n)/(factorial(r)*factorial(n-r))


def numberOfWaysForGraduating(n):
    m = n//4
    sm = 1
    for i in range(1,n-m+1):
        sm+=ncr(n-m,i)
    return sm

def probabilityOfFailing(n):
    den = 1
    for i in range(1,n+1):
        den +=  ncr(n,i)
    
    num = den - numberOfWaysForGraduating(n)
    res = "{0}".format(num)+'/{0}'.format(den)
    return res



n = int(input("Enter total number of days : "))
print("Probability of failing : ",probabilityOfFailing(n))
print("Number of ways of Graduating : ",numberOfWaysForGraduating(n))