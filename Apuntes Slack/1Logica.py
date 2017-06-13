#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
and (y)
or (o)
not (no)
!= (no es igual)
== (es igual)
>= (es mayor o igual que)
<= (es menor o igual que)
True (Verdad)
False (Falso)

EQUIVALENCIAS

NOT
not False -> True
not True -> False

OR
True or False -> True
True or True -> True
False or True -> True
False or False -> False

AND
True and False -> False
True and True -> True
False and True -> False
False and False -> False

NOT OR
not (True or False) -> False
not (True or True) -> False
not (False or True) -> False
not (False or False) -> True

NOT AND
not (True and False) -> True
not (True and True) -> False
not (False and True) -> True
not (False and False) -> True
1 != 0 -> True
1 != 1 -> False
0 != 1 -> True
0 != 0 -> False

IGUAL
1 == 0 -> False
1 == 1 -> True
0 == 1 -> False
0 == 0 -> True
"""

# Jugamos?

print(1)
print(True and True)
print(2)
print(False and True)
print(3)
print(1 == 1 and 2 == 1)
print(4)
print("test" == "test")
print(5)
print(1 == 1 or 2 != 1)
print(6)
print(True and 1 == 1)
print(7)
print(False and 0 != 0)
print(8)
print(True or 1 == 1)
print(9)
print("test" == "testing")
print(10)
print(1 != 0 and 2 == 1)
print(11)
print("test" != "testing")
print(12)
print("test" == 1)
print(13)
print(not (True and False))
print(14)
print(not (1 == 1 and 0 != 1))
print(15)
print(not (10 == 1 or 1000 == 1000))
print(16)
print(not (1 != 10 or 3 == 4))
print(17)
print(not ("testing" == "testing" and "Zed" == "Cool Guy"))
print(18)
print(1 == 1 and (not ("testing" == 1 or 1 == 0)))
print(19)
print("chunky" == "bacon" and (not (3 == 4 or 3 == 3)))
print(20)
print(3 == 3 and (not ("testing" == "testing" or "Python" == "Fun")))
