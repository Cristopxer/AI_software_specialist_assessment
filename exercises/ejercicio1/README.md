# Ejercicio 1
## Run
* run exercise 1 - The default word used to test is "ANA" so the output will return True
  ```Shell
  cd .\exercises\ejercicio1\
  python .\exercise1.py  
  ```
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; You can update the evaluated word in exercise1.py
  ```Python
  print(is_palindrome("YOUR WORD HERE"))
  ```

## Unit testing
once you got pytest and pytest-cov intalled to run the unit tests execute the following command
  ```Shell
  pytest --cov
  ```
the excepted output should look like
```Shell
================================= test session starts =================================
platform win32 -- Python 3.11.5, pytest-7.4.0, pluggy-1.0.0
rootdir: D:\Crist\Documents\GBM\exercises\exercises\ejercicio1
plugins: cov-4.1.0
collected 3 items

tests\test_exercise1.py ...                                                      [100%]

---------- coverage: platform win32, python 3.11.5-final-0 -----------
Name                      Stmts   Miss  Cover
---------------------------------------------
__init__.py                   0      0   100%
exercise1.py                  6      0   100%
tests\__init__.py             0      0   100%
tests\test_exercise1.py       7      0   100%
---------------------------------------------
TOTAL                        13      0   100%


================================== 3 passed in 0.11s ==================================

```