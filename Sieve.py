import math

def prime_pi_full(n):
    if n < 2:
        return 0
    sieve = bytearray(b'\x01') * (n+1)
    sieve[0:2] = b'\x00\x00'
    for i in range(2, int(n**0.5)+1):
        if sieve[i]:
            sieve[i*i:n+1:i] = b'\x00' * ((n - i*i)//i + 1)
    return sum(sieve)

def li_k(x, k=4):
    logx = math.log(x)
    fact = 1
    result = 0.0
    for j in range(1, k+1):
        if j>1: fact*=(j-1)
        result += fact / (logx ** j)
    return x * result

def twin_pi(n):
    sieve = bytearray(b'\x01') * (n+1)
    sieve[0:2] = b'\x00\x00'
    for i in range(2, int(n**0.5)+1):
        if sieve[i]:
            sieve[i*i:n+1:i] = b'\x00' * ((n - i*i)//i + 1)
    return sum(1 for p in range(3, n-1) if sieve[p] and sieve[p+2])

if __name__ == "__main__":
    N=60000000
    print("pi(60M)=", prime_pi_full(N))
