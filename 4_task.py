class Fraction:

    def __init__(self,number_numerator, number_denominator = None):
        
        if isinstance(number_numerator, str):
            result = number_numerator.split('/')
            self.number_numerator = int(result[0])
            self.number_denominator = int(result[1])
        else:
            self.number_numerator = number_numerator
            self.number_denominator = number_denominator

        self.__fraction_reduction()

    
    def __fraction_reduction(self):
        a = self.number_numerator
        b = self.number_denominator
        while b!= 0:
            a, b = b, a % b
        
        # для корректного вывода __repr__ перевод в формат int
        self.number_numerator = int(self.number_numerator / a)  
        self.number_denominator = int(self.number_denominator / a)


    def __neg__(self):
        if self.number_numerator < 0: 
            return Fraction(f"{-self.number_numerator}/{self.number_denominator}")
        if  self.number_denominator < 0:
            return Fraction(f"{self.number_numerator}/{-self.number_denominator}")
        if self.number_numerator < 0 and self.number_denominator < 0:
            return Fraction(f"{-self.number_numerator}/{-self.number_denominator}")

    def numerator(self, num = None):
        if num is not None:
            self.number_numerator = num
            self.__fraction_reduction()
        # elif num < 0:
            # # self.number_numerator = -num
            # self.__neg__()
            # self.__fraction_reduction()
        return self.number_numerator

    def denominator(self, num = None):
        if num:
            self.number_denominator = num
            self.__fraction_reduction()
        return self.number_denominator


    def __add__(self, other):
        if isinstance(other, Fraction):
            if self.number_denominator != other.number_denominator:

                new_denominator = (self.number_denominator * other.number_denominator)
                new_numerator = (self.number_numerator * other.number_denominator) 
                                + (other.number_numerator * self.number_denominator)
                
                        
                return Fraction(new_numerator, new_denominator)
            
            else: 
                new_numerator = self.number_numerator + other.number_numerator
                new_denominator = self.number_denominator
                        
                return Fraction(new_numerator,  new_denominator)
    def __iadd__(self, other):
        if isinstance(other, Fraction):
            if self.number_denominator != other.number_denominator:

                new_number_denominator = (self.number_denominator * other.number_denominator)
                new_number_numerator = (self.number_numerator * other.number_denominator) 
                + (other.number_numerator * self.number_denominator)
                self.number_denominator =  new_number_denominator
                self.number_numerator = new_number_numerator
                
                return Fraction(self.number_numerator, self.number_denominator)
            
            else:
                new_numerator = self.number_numerator + other.number_numerator
                new_denominator = self.number_denominator
                self.number_denominator =  new_denominator
                self.number_numerator = new_numerator 
                
                return Fraction(self.number_numerator, self.number_denominator)


    def __sub__(self, other):
        if isinstance(other, Fraction):
            if self.number_denominator != other.number_denominator:
    
                new_denominator = (self.number_denominator * other.number_denominator)
                new_numerator = (self.number_numerator * other.number_denominator) 
                - (other.number_numerator * self.number_denominator)

                return Fraction(new_numerator, new_denominator)
            
            else:
                new_numerator = self.number_numerator - other.number_numerator
                new_denominator = self.number_denominator

                return Fraction(new_numerator, new_denominator)

    def __isub__(self, other):
        if isinstance(other, Fraction):
            if self.number_denominator != other.number_denominator:

                new_number_denominator = (self.number_denominator * other.number_denominator)
                new_number_numerator = (self.number_numerator * other.number_denominator) 
                - (other.number_numerator * self.number_denominator)
                self.number_denominator =  new_number_denominator
                self.number_numerator = new_number_numerator
                
                return Fraction(self.number_numerator, self.number_denominator)
            
            else:
                new_numerator = self.number_numerator - other.number_numerator
                new_denominator = self.number_denominator
                self.number_denominator =  new_denominator
                self.number_numerator = new_numerator 
                
                return Fraction(self.number_numerator, self.number_denominator)


    def __str__(self) -> str:
        return f"{self.number_numerator}/{self.number_denominator}"

    def __repr__(self):
        return f" Fraction ({self.number_numerator}, {self.number_denominator})"
   
