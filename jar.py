class Jar:
    def __init__(self, capacity=12):
        if not isinstance(capacity, int) or capacity <= 0:
            raise ValueError("Capacity must be a non-negative integer")
        self._capacity = capacity
        self._cookies = 0
        # Max cookies allowed to fit in jar
    
    def __str__(self):
        return "🍪" * self._cookies
        # Returns no. of cookies in the jar eg -if 3 cookies it should return "🍪🍪🍪"
    
    def deposit(self, n):
        if n < 0:
            raise ValueError("Cannot deposite -negative number of cookies")
        if self._cookies + n > self._capacity:
            raise ValueError("Deposit would exceed jar capacity")
        
        self._cookies += n
        return f"Deposited {n} Cookies"
        # adds n no. of cookies
    
    def withdraw(self, n):
        if n <= 0:
            raise ValueError("Nuber specified must be positive")
        if n > self._cookies:
            raise ValueError("Not enough cookies in the jar to withdraw")
        
        self._cookies -= n 
        return f"Withdrew {n} Cookies"
        # removed n no. of cookies
        # if no cookies raise ValueError
    
    @property
    def capacity(self):
        return self._capacity
        # return capacity
    
    @property
    def size(self):
        return self._cookies
        # return no. of cookies in the jar in numerics

jar = Jar(20)
print(jar.deposit(5))
print(jar.deposit(8))
print(jar.withdraw(3))
print(jar.withdraw(6))
print(f"Current number of cookies in the jar: {jar.size}")
print(f"Jar capacity: {jar.capacity}")
print(jar)