#Write a program that takes an integer between 0 and 1 million and returns the 
#word equivalent

def words(n): 
   units = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"] 
   teens = ["Ten","Eleven","Twelve","Thirteen","Fourteen","Fifteen","Sixteen","Seventeen","Eighteen","Nineteen"] 
   tens = ["Twenty","Thirty", "Fourty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"] 
   if n <= 9: 
        return units[n] 
   elif n >= 10 and n <= 19: 
        return teens[n-10] 
   elif n >= 20 and n <= 99: 
        if n % 10 != 0:
            return tens[(n//10)-2] + " " + (units[n % 10]) 
        else:
            return tens[(n//10)-2]
   elif n >= 100 and n <= 999: 
        if n % 100 !=0:
            return words(n//100) + " Hundred And " + (words(n % 100))
        else:
            return words(n//100) + " Hundred"
   elif n >= 1000 and n <= 99999: 
        if n % 1000 !=0:
            return words(n//1000) + " Thousand " + (words(n % 1000))
        else:
            return words(n//1000) + " Thousand " 
   elif n>=100000 and n<=1000000:
        if n % 100000 !=0:
            return words(n//100000) + " Hundred And " + (words(n % 100000))
        else:
            return words(n//100000) + " Hundred " + " Thousand "
   

print(words(34))
