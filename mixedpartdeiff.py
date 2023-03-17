from sympy import *
x , y = symbols ('x y')
u=exp( x )*( x*cos( y )-y*sin( y ) ) # input mutivariable function u = u (x , y )
dux = diff (u , x ) # Differentate u w . r . t x
duy = diff (u , y ) # Differentate u w . r . t . y
duxy = diff ( dux , y ) # or duxy = diff (u ,x , y )
duyx = diff ( duy , x ) # or duyx = diff (u ,y , x )
# Check the condtion uxy = uyx
if duxy = = duyx :
print ('Mixed partial derivatives are equal ')
else :
print ('Mixed partial derivatives are not equal ')
