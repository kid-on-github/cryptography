# This program was made to learn about how Pub/Priv key encryption (RSA) works

# Helpful links
# https://www.khanacademy.org/computing/computer-science/cryptography/modern-crypt/\

# video on finding d (RSA)
# https://www.youtube.com/watch?v=aibrvM5mDs8&t=798s



# random prime numbers
p, q = 53, 59

# public key = e & n
e, n = 3, p*q

# ø(n)  [phi(n)]
øn = (p-1)*(q-1)

# find value for d (private key)
for k in range(e):
    numerator = 1.0+(k*øn)
    if numerator%e == 0:
        d = int(numerator/e)
        break

# verify that d is valid
if e*d%øn != 1:
    raise Exception('ERROR: Invalid value generated for d')

# encrypt and decrypt
encDec = lambda msg,key: msg**key%n


rawMsg = 42
encMsg = encDec(rawMsg,e)
decMsg = encDec(encMsg,d)

print(
    f'''
    origonal msg:   {rawMsg}
    encrypted msg:  {encMsg}
    decrypted msg:  {decMsg}
    '''
)

rawMsg = 42
sign = encDec(rawMsg,d)
check = encDec(sign,e)

print(
    f'''
    origonal msg:   {rawMsg}
    signed msg:     {sign}
    plain msg:      {check}
    '''
)





'''
To Do:
msg padding: https://en.wikipedia.org/wiki/Optimal_asymmetric_encryption_padding

Notes for RSA:
p and q are both random prime numbers with similar length

e is coprime to ø(n) and 1 < e < ø(n)
e is small odd number that does not share factor with phi n

n is the modulus for the public key and the private keys

k = mod
d = (1+k*øn)/e
possible values for k = range(0,e)

'''