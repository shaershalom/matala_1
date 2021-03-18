#  סיימתי את התרגיל
def exponent (x):
    i=1
    squar=1
    assembly=1
    answer=1
    while (i<171):
        squar=squar*x
        assembly=assembly*i
        answer=answer+(squar/assembly)
        i=i+1
    return answer

def Ln(x):
    y=0
    i=0
    while (i<500):
        y=y+(2*((x-exponent(y))/(x+exponent(y))))
        i=i+1
    return y

def XtimesY(x,y):
    if x>0 :
        sum_num=exponent(y*Ln(x))
        return  sum_num
    else:
        sum_num=0.0
        return  sum_num

print( XtimesY(-2,2))
'''    
def sqrt(y,x):
    sum_sqrt= XtimesY(x,(1/y))
    return sum_sqrt
            
def calculate(x):
    sum_num=0
    sum_num=(XtimesY(2.718281828459045,x)*XtimesY(7,x)*XtimesY(x,-1)*sqrt(x,x))
    return float('%0.6f' % sum_num )


try:
    x=float(input("enter number : "))
    print(float(calculate(x)))
except:
    print(float(0.0))
'''