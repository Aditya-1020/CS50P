import pytest
from jar import Jar


def test_init():
    jar1 = Jar(20)
    assert jar1.capacity == 20
    assert jar1.size == 0
    
    jar2 = Jar()
    assert jar2.capacity == 12
    assert jar2.size == 0
    with pytest.raises(ValueError):
        Jar("invalid")
    with pytest.raises(ValueError):
        Jar(-10)
    with pytest.raises(ValueError):
        Jar(0)



def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar(15)
    assert jar.deposit(5) == "Deposited 5 Cookies"
    assert jar.size == 5
    assert jar.deposit(10) == "Deposited 10 Cookies"
    assert jar.size == 15
    with pytest.raises(ValueError):
        jar.deposit(-3)
    with pytest.raises(ValueError):
        jar.deposit(6)

def test_withdraw():
    jar = Jar(20)
    jar.deposit(10)
    assert jar.withdraw(3) == "Withdrew 3 Cookies"
    assert jar.size == 7
    with pytest.raises(ValueError):
        jar.withdraw(10)
    with pytest.raises(ValueError):
        jar.withdraw(-2)
    with pytest.raises(ValueError):
        jar.withdraw(8)

if __name__ == "__main__":
    pytest.main()