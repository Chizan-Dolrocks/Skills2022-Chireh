def factors(n):
    p = 2
    fact = list()
    while n >= p*p :
        if n % p == 0:
            fact.append(p)
            n = int(n / p)
        else:
            p = p + 1
            fact.append(n)
    return fact
def is_prime(number):
    if number <= 1:
        return False
    for n in range(2, number):
        if number % n == 0:
            return False
        else:
            return True
def vowels(textV):
    vow = list()
    for i in textV:
        if i in 'aeiouAEIOU':
            vow.append(i)
    return vow


