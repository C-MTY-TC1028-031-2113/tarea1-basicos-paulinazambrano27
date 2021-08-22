def main():
    from math import sqrt
   
    oper1 = float(2 * (3 / 4) + 4 * (2 / 3) - 3 * (1 / 5)+ 5 * (1 / 2))
    print(round(oper1, 4))
                  
    oper2 = float(2 * 35 + 4 * 6 ** 3 - 6 * 49)
    print(round(oper2, 4))
                  
    a = 4
    b = 5              
                  
    oper3 = float((a ** 3 + 2 * b ** 2) / (4 * a))
    print(round(oper3, 4))
                  
    a = 4
    a = 5              
                  
    oper4 = float((2 * (a + b) ** 2 + 4 * (a - b) ** 2) / (a * b ** 2))
    print(round(oper4, 4))
                  
    oper5 = float(((a + b) ** 2 + 2 ** (a + b)) ** (1/2) / (2 * a + 2 * b) ** 2)
    print(round(oper5, 4))              
    pass
    
   



if __name__ == '__main__':
    main()
