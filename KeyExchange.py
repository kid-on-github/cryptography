# Diffie-hellman key exchange
primeModulus = 17
primitiveRoot = 3

# find the public key or shared secret
encDec = lambda baseNum,exponent: (baseNum**exponent) % primeModulus

alicePriv = 15
alicePub = encDec(primitiveRoot, alicePriv) # send to Bob

bobPriv = 13
bobPub = encDec(primitiveRoot, bobPriv) # send to Alice

sharedSecret = encDec(bobPub, alicePriv)
sharedSecret = encDec(alicePub, bobPriv)


'''
Notes for Diffie-hellman key exchange:

# The discrete logarithm problem
for exponent in range(1, primeModulus):
    a = (primitiveRoot**exponent) % primeModulus
    print(f'{exponent}:{a}')

primitiveRoot = generator

RSA is useful for encrypting data while the shared key is being established in symmetric key encryption

'''