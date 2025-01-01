# Remake the challenge 35 of the triangles, adding the resource of showing what kind of triangle 
# will be formed: 

# equilateral: all sides equal
# isosceles: 2 sides equal
# scalene: all sides different

s1 = float(input('1st side: '))
s2 = float(input('2nd side: '))
s3 = float(input('3rd side: '))
if s1<s2+s3 and s2<s1+s3 and s3<s1+s2:
    print('these segments can form a triangle')
    if s1==s2 and s2==s3: # if s1 == s2 == s3: 'o python aceita este formato'
        print('the triangle is equilateral')
    elif s1==s2 or s2==s3 or s3==s1:                 # diferente no python é representado por '!='
        print('the triangle is isosceles')           # s1 != s2 != s3 != s1 
    else:                                            # finalizamos com else para evitar criar outra comb ainda. .
        print('the triangle is scalene')
else:
    print('these segments cannot form a triangle')
