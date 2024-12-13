class Fraction:

     def __init__(self,number_numerator, number_denominator=None):
        
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

     def numerator(self, num = None):
          if num:
               self.number_numerator = num
               self.__fraction_reduction()
          return self.number_numerator

     def denominator(self, num = None):
          if num:
               self.number_denominator = num
               self.__fraction_reduction()
          return self.number_denominator


     def __str__(self) -> str:
          return f'({str(self.number_numerator)}/
                 {str(self.number_denominator)})'
   
     def __repr__(self):
          return f'Fraction({str(self.number_numerator)}, 
                 {str(self.number_denominator)})'



fraction1 = Fraction(8,50)
# fraction2 = Fraction('42./77224')
fraction1.denominator(44)
print(fraction1)


