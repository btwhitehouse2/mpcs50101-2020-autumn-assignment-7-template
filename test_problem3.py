import pytest
from problem3 import Fraction, decimal_form
#import propblem3 as p3

    
def test_initialization():
    """Test fraction creation"""
    f1 = 0.625
    f2 = Fraction(5,8)
    f3 = Fraction(0,5)
    f4 = 0.0 
    assert f1.__str__() == "5/8"
    assert decimal_form(f2) == 0.625
    assert f1 == f2
    assert abs(f3) == f4

def test_add():
    """Test the addition function"""
    f1 = Fraction(5,8) 
    f2 = Fraction(5,8) 

    add_them_up = f1 + f2
    assert add_them_up.__str__() != "10/8" 
    assert add_them_up.__str__() != "5/4" 
    assert add_them_up.__str__() == "1-1/4" 
    assert decimal_form(add_them_up) == 1.25
  
def test_subtract():
    """Test the addition function"""
    f1 = Fraction(2,1) 
    f2 = Fraction(1,2) 

    total = f1 - f2
    assert total.__str__() == "3/2" 
    assert decimal_form(total) == 1.5


def test_multiply():
    """ """
    f1 = Fraction(5,8) 
    f2 = Fraction(2,1)
    f3 = f1 * f2
    assert f3.__str__() != "10/8"
    assert f3.__str__() == "5/4"
    assert decimal_form(f3) == 1.25

def test_divide():
    """ """
    f1 = Fraction(5,8) 
    f2 = Fraction(1,1)
    f3 = f1 / f2
    assert f3.__str__() == "5/8"
    assert decimal_form(f3) == 0.625
