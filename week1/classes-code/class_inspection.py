>>> class X:
...    a = 3
...    b = 3.1415
...
>>> x = X()
>>> type(x)
<type 'instance'>
>>> dir(x)
['__doc__', '__module__', 'a', 'b']
>>> type(x.a)
<type 'int'>

