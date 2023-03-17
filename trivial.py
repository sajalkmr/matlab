import numpy as np
A=np . matrix ([ [1 ,2 ,-1],[2 ,1 , 4],[3 ,3 , 4] ])
B=np . matrix ([ [0],[0],[0] ])
r=np . linalg . matrix_rank ( A )
n=A . shape [1]
if ( r= =n ):
print (" System has trivial solution ")
else :
print (" System has ", n-r , " non - trivial solution ( s ) ")


import numpy as np
A=np . matrix ([ [1 ,2 ,-1],[2 ,1 , 4],[1 ,-1 , 5] ])
B=np . matrix ([ [0],[0],[0] ])
r=np . linalg . matrix_rank ( A )
n=A . shape [1]
if ( r= =n ):
print (" System has trivial solution ")
else :
print (" System has ", n-r , " non - trivial solution ( s ) ")
