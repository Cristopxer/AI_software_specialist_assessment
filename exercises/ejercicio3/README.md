# Ejercicio 3
## Run
* Takes "exercise3_input.txt" as input and the output is write in "exercise3_output.txt"
  ```Shell
  cd .\exercises\ejercicio3\
  python .\exercise3.py  
  ```
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; You can update the evaluated file and output in exercise3.py
```Python
  minimum_jumps("YOUR INPUT FILE HERE.txt", "YOUR OUTPUT FILE HERE.txt")
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
rootdir: D:\Crist\Documents\GBM\exercises\exercises\ejercicio3
plugins: cov-4.1.0
collected 3 items

tests\test_exercise3.py ...                                                      [100%]

---------- coverage: platform win32, python 3.11.5-final-0 -----------
Name                      Stmts   Miss  Cover
---------------------------------------------
__init__.py                   0      0   100%
exercise3.py                 23      0   100%
tests\__init__.py             0      0   100%
tests\test_exercise3.py      26      0   100%
---------------------------------------------
TOTAL                        49      0   100%


================================== 3 passed in 0.15s ==================================

```