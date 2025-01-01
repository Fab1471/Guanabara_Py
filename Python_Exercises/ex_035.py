# Develop a program that read the lenght of 3 segments and tell the user if they can or not form a triangle.

'''
cada um dos segmentos tem q ser menor doq a soma do comprimento dos outros 2


'''
print('=+='*20)
print('Triangle Analyser')
print('=+='*20)
s1 = float(input('1st side: '))
s2 = float(input('2nd side: '))
s3 = float(input('3rd side: '))
if s1<s2+s3 and s2<s1+s3 and s3<s1+s2:
    print('The segments up above can form a triangle.')
else:
    print('The segments up above cannot form a triangle.')
