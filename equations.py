#  סיימתי את התרגיל
def exponent (x:float)-> float:
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

def Ln(x:float) -> float:
    y=0
    i=0
    while (i<500):
        y=y+(2*((x-exponent(y))/(x+exponent(y))))
        i=i+1
    return y

def XtimesY(x:float,y:float) -> float:
    if x>0 :
        sum_num=exponent(y*Ln(x))
        return  sum_num
    else:
        sum_num = float(0.0) 
        return sum_num

def sqrt(y:float,x:float)-> float:
    sum_sqrt= XtimesY(x,(1/y))
    return sum_sqrt
            
def calculate(x:float)-> float:
    try: 
        sum_num=0
        sum_num=(XtimesY(2.718281828459045,x)*XtimesY(7,x)*XtimesY(x,-1)*sqrt(x,x))
        return float('%0.6f' % sum_num )
    except:
        return float(0.0)