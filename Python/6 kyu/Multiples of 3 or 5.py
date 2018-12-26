def solution(number):
    #the sum of all natural numbers till n is 1+  2  +  3  +...+(n-2)+(n-1)+n
    #adding this same series but in reverse:  n+(n-1)+(n-2)+...+  3  +  2  +1
    #then we get:                           (n+1)+(n+1)+(n+1)+(n+1)+....(n+1)
    #so we have that 2*Series = n*(n+1) -> series that represent the sum of natural numbers is
    #n*(n+1)/2; Now we can get the sum of any multiples as well
    mult3 = (number-1)//3 #number of mulitples of 3 till the number (exclusive)
    mult5 = (number-1)//5 #number of mulitples of 5 till the number (exclusive)
    mult15 = (number-1)//15 #number of mulitples of 15 till the number (exclusive)
    #the sum of all multiples of 3 or 5 is defined as sum(mult3) + sum(mult5) - sum(mult15) as we need to get rid of duplicates
    #applying the series we defined earlier and multiplying it by 3/5/15 to get the sum of the multiples only
    #as 1+2+3+4+... can be converted to 3*1+3*2+3*3+3*4+.... to get the multiples of 3
    return 3*(mult3*(mult3+1)//2) + 5*(mult5*(mult5+1)//2) - 15*(mult15*(mult15+1)//2)
