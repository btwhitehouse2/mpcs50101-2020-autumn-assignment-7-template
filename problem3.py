class Fraction:
 """This class has characteristics for the numerator on the top and denominator on the botoom"""   
    def __init__(self,top,bottom):
        self.numerator = top
        self.denominator = bottom

    def __str__(self):
        return(str(self.numerator)+"/"+str(self.denominator))

# Find the the greatest common divisor
    def gcd(m,n):
        while m%n != 0:
            oldm = m
            oldn = n
            m = oldn
            n = oldm%oldn
        return(n)

#This formats the print for the fraction with 3 options
#mixed fraction, fraction, whole number, zero
    def formatting_function(newnumerator,newdenominator):
        #if the value is zero or improper it will result in a 0
        if newdenominator == 0:
            return('{}'.format(newdenominator))
        else:
            commonfactor = Fraction.gcd(newnumerator,newdenominator)
            # if whole number
            if commonfactor == newdenominator:
                a = newnumerator // newdenominator
                return('{}'.format(a))
            #mixed number
            elif newnumerator > newdenominator:
                newnumerator = newnumerator//commonfactor
                newdenominator = newdenominator//commonfactor
                a = newnumerator // newdenominator
                b = newnumerator % newdenominator
                return('{}-{}/{}'.format(a, b, newdenominator))
            #fraction
            else:
                newnumerator = newnumerator//commonfactor
                newdenominator = newdenominator//commonfactor
                return Fraction(newnumerator,newdenominator)

    #adds two fractions
    def __add__(self,additionalfraction):
        newnumerator = self.numerator*additionalfraction.denominator + self.denominator*additionalfraction.numerator
        newdenominator = self.denominator * additionalfraction.denominator        
        Fraction.formatting_function(newnumerator,newdenominator)
        return(Fraction.formatting_function(newnumerator,newdenominator))

    #helps to solve if you input a negative number
    def __neg__(self):
        return Fraction(-self.numerator, self.denominator)
    
    #subtracts two fractions
    def __sub__(self,additionalfraction):
        newnumerator = self.numerator*additionalfraction.denominator - self.denominator*additionalfraction.numerator
        newdenominator = self.denominator * additionalfraction.denominator
        Fraction.formatting_function(newnumerator,newdenominator)
        return(Fraction.formatting_function(newnumerator,newdenominator))

    #multiplies two fractions
    def __mul__(self,additionalfraction):
        newnumerator = self.numerator*additionalfraction.numerator
        newdenominator = self.denominator * additionalfraction.denominator
        Fraction.formatting_function(newnumerator,newdenominator)
        return(Fraction.formatting_function(newnumerator,newdenominator))

    #divides two fractions
    def __truediv__(self,additionalfraction):
        newnumerator = self.numerator*additionalfraction.denominator
        newdenominator = self.denominator * additionalfraction.numerator
        Fraction.formatting_function(newnumerator,newdenominator)
        return(Fraction.formatting_function(newnumerator,newdenominator))

    #produces true or false for less than sign
    def __lt__(self,frac2):
        v1 = self.numerator/self.denominator
        v2 = frac2.numerator/frac2.denominator
        if v1 < v2:
            return(True)        
        else:
            return(False)

    #produces true or false for greater than sign
    def __gt__(self,frac2):
        v1 = self.numerator/self.denominator
        v2 = frac2.numerator/frac2.denominator
        if v1 > v2:
            return(True)        
        else:
            return(False)

    #will turn an fraction into a decimal
    def decimal_form(self):
        s = self.numerator/self.denominator
        return("%.3f" %s)
pass

def main():
"""part of the program where you can input values in order to solve any questions"""
    f1 = Fraction(1,2)
    f2 = Fraction(1,2)
    f3 = f1 + f2 
    f4 = f1*f2
    f6 = f1/f2
    #f5=f2-f1
    print(f3)
    print(f4)
    print(f6)
    #print(Fraction.decimal_form(f1))
    #print(f4)
    #print(f5)
    #print(f6)

if __name__ == "__main__":
    main()