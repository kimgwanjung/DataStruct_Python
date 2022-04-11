def printPoly(p_x,t_x):
    polyStr = "P(x) = "

    for i in range(len(tx)):
        term = p_x[i]
        coef = t_x[i]

        if (coef >= 0):
            polyStr +="+"
        polyStr += str(coef) + "x^" + str(term) + " "
    return polyStr

def calcPoly(xVal, p_x, t_x):
    retValue = 0


    for i in range(len(tx)):
        term = p_x[i]
        coef = t_x[i]
        retValue += coef * xValue ** term
        term -= 1
        
    return retValue

px = [300, 20, 0]
tx = [7,-4,5]
if __name__ == "__main__":
    pStr = printPoly(px,tx)
    print(pStr)

    xValue = int(input("X 값-->"))

    pxValue = calcPoly(xValue, px,tx)
    print(pxValue)
