def solution(n):
    if isinstance(n,int):
        primes = make_prime_list(100000)
        if n>len(primes): return
        if n<0: return
        s=''
        for i in range(0,5):
            s+=primes[n+i]
        print(s)
        return s
    else:
        return

def is_prime_number(num):
    if num<=1:
        return False
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            return False
    return True

def make_prime_list(hi):
    prime_list=''
    for i in range(2,hi,1):
        if is_prime_number(i):
            prime_list+=str(i)
    return prime_list

solution(0)
solution(5000)