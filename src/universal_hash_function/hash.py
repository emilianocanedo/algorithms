from random import randrange

# hash(k) = (((a*k+b)%p)%m)
# a, b < p-1
# a =! 0
# m = memory space / hash function length
# p = large prime number

class Hash:

    def __init__(self, m):
        self.p = self._get_large_prime()
        self.m = m
        self.a = randrange(1, self.p)
        self.b = randrange(0, self.p)

    def _get_large_prime(self):
        # hardcoded
        return 64988430769
    
    def hash(self, element):
        return (((self.a*element+self.b)%self.p)%self.m)
    
# fast test

myhash = Hash(300)

print(myhash.hash(6656504))
print(myhash.hash(4349854))
print(myhash.hash(543212))