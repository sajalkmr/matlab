from sympy import *
t= Symbol ('t') # define t as symbol
r= Symbol ('r')
r=4*( 1+cos( t ) )
r1= Derivative (r , t ) . doit () # find the first derivative of r w . r . t " t "
r2= Derivative ( r1 , t ) . doit () # find the second derivative of r w . r . t " t "
rho =( r ** 2+r1 ** 2 ) ** ( 1 . 5 )/( r ** 2+2*r1 ** 2-r*r2 ) ; # Substitute r1 and r2 in
formula
rho1 = rho . subs (t ,pi/2 ) # substitute t in rho
print ('The radius of curvature is %3 . 4f units '% rho1 )

from sympy import *
t ,r ,a , n= symbols ('t r a n')
r=a*sin( n*t )
r1= Derivative (r , t ) . doit ()
r2= Derivative ( r1 , t ) . doit ()
rho =( r ** 2+r1 ** 2 ) ** 1 . 5/( r ** 2+2*r1 ** 2-r*r2 ) ;
rho1 = rho . subs (t ,pi/2 )
rho1 = rho1 . subs (n , 1 )
print (" The radius of curvature is ")
display ( simplify ( rho1 ) )