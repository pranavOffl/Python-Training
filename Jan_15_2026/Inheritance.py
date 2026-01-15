# single Level

class A:
    pass

class B(A):
    pass

# Multi level

class A:
    pass
class B(A):
    pass
class C(B):
    pass

# Multiple

class A:
    pass
class B:
    pass
class C(A, B):
    pass

# Hierarical

class A:
    pass
class B(A):
    pass
class C(A):
    pass

# Hybrid

class A:
    pass
class B(A):
    pass
class C(A):
    pass
class D(B, C):
    pass