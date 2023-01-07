# def num2hex(num):
#     if num >= 0:
#         print ('0x'+'%02x' %num)
#     else:
#         num = -num
#         print('-0x'+'%02x' %num)
# #
# num2hex(-40)
# def Cel2Fah(temp): 
#     s = temp*9/5+32
#     return '%.2f' %s
#     
# Cel2Fah(28)
# def BMI(weight, height): 
#     
#     return '%.1f' %(weight/(height*height))
#     
# BMI(110, 2)
# def BMI(weight, height):
#     s = '%.1f' %(weight/(height*height))
#     return s
# print(BMI(110, 2))
# def percent(value, total):
#     return int(value/total*100)
# print(percent(63,12))
# x = [10]
# def addFirstAndLast(x): 
#     return x[0] + x[-1]
# # print(addFirstAndLast(x))
# def addOne(x):
#     return x+1
# 
# def useFunction(addOne, num):
#     return addOne(num)**2
# 
# print(useFunction(addOne, 0))
# def isPrime(x):
#     if x <= 1:
#         return False
#     else:
#         for i in [2, x]:
#             if x%i==0:
#                 return False
#             else: 
#                 return True
#     
# print(isPrime(15))

# def LeapYear(yr):
#     if (yr%4==0 and yr%100!=0) or yr%400==0:
#         return True
#     else:
#         return False
#     
# print(LeapYear(2018))

# def piApprox(num):
# 	i = 1
# 	pi = 0
# 	while i<num+1:   
# 		c = (-1)**(i+1)
# 		a = 1/(2*i-1)                                   
# 		pi += 4*c*a                  
# 		i+=1                      
# 	return pi
# 
# print(piApprox(10))
def MatrixProduct(a, b):
    D = []
    for i in range(len(a)):        
        C = []
        for j in range(len(b[0])):
            total = 0           
            for k in range(len(a[0])):
                total += a[i][k] * b[k][j]
            C.append(total)
        D.append(C)
    return D
 
print(MatrixProduct([ [1, 3], [-5, 6], [2, 4]], [ [1, 4], [8, 7]]))
