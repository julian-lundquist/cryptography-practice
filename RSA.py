import math
import random

def is_prime(p):
    for i in range(2, math.isqrt(p)):
        if p % i == 0:
            return False
    return True

def get_prime(size):
    while True:
        p = random.randrange(size, 2*size)
        if is_prime(p):
            return p

def lcm(a, b):
    return a*b//math.gcd(a, b)

def get_e(lambda_n):
    for e in range(2, lambda_n):
        if math.gcd(e, lambda_n) == 1:
            return e
    return False

def get_d(e, lambda_n):
    for d in range(2, lambda_n):
        if d*e % lambda_n == 1:
            return d
    return False


# Key generation done by Alice (secret)
#Step 1: Generate 2 distinct prime numbers
size = 300
p = get_prime(size)
q = get_prime(size)
print("Generated Numbers: ", p, q)

# Step 2: compute n = p*q
n = p*q
print("Modulus n:", n)

# Step 3: Compute lambda(n) = lcm(lambda(p), lambda(q))
lambda_n = lcm(p-1, q-1)
print("Lambda n: ", lambda_n)

# Step 4: Choose an integer e such that 1 < e < lambda(n) and gcd(e, lambda(n)) = 1
e = get_e(lambda_n)
print("Public exponent: ", e)

# Step 5: Solve for the equation d*e = 1 (mod lambda(n))
d = get_d(e, lambda_n)
print("Secret exponent: ", d)

# Generation Results
print("Public Key (e,n):", e, n)
print("Secret Key (d):", d)

# This is the message Bob wants to send
m = 117
c = m**e % n
print("Bob sends: ", c)

# This is Alice decrypting the cipher
m = c**d % n
print("Decrypted Message: ", m)