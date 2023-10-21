# Ejercicio 2
## Run
* run exercise 2 - Takes "exercise2_input.txt" as input and the output is write in "exercise2_output.txt"
  ```Shell
  cd .\exercises\ejercicio2\
  python .\exercise2.py  
  ```
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; You can update the evaluated file and output in exercise2.py
```Python
  grand_prix_world_champion("YOUR INPUT FILE HERE.txt", "YOUR OUTPUT FILE HERE.txt")
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
rootdir: D:\Crist\Documents\GBM\exercises\exercises\ejercicio2
plugins: cov-4.1.0
collected 5 items

tests\test_exercise2.py .....                                                    [100%]

---------- coverage: platform win32, python 3.11.5-final-0 -----------
Name                      Stmts   Miss  Cover
---------------------------------------------
__init__.py                   0      0   100%
exercise2.py                 46      0   100%
tests\__init__.py             0      0   100%
tests\test_exercise2.py      37      0   100%
---------------------------------------------
TOTAL                        83      0   100%


================================== 5 passed in 0.16s =================================

```