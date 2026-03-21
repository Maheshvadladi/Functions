Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #ASCII
>>> #chr()
>>> chr(20)
'\x14'
>>> chr(68)
'D'
>>> chr(65)
'A'
>>> chr(90)
'Z'
>>> #ord()
>>> ord("a")
97
>>> ord("z")
122
>>> ord("1")
49
>>> ord("100")
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    ord("100")
TypeError: ord() expected a character, but string of length 3 found
>>> chr(57)
'9'
>>> ord("9")
57
>>> ord("19")
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    ord("19")
TypeError: ord() expected a character, but string of length 2 found
