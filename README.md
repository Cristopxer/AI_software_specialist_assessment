# AI_software_specialist_assessment
## Setup
* clone the repo
  ```Shell
  git init
  git clone https://github.com/Cristopxer/AI_software_specialist_assessment.git
  ```

* setup clean enviroment
  ```Shell
  cd exercises
  conda create --name [ENV_NAME] --file requeriments.txt
  ```
## Run
* run exercise 1 - The default word used to test is "ANA" so the output will return True
  ```Shell
  python .\exercise1.py  
  ```
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; You can update the evaluated word in exercise1.py
  ```Python
  print(is_palindrome("YOUR WORD HERE"))
  ```
* run exercise 2 - Takes "exercise2_input.txt" as input and the output is write in "exercise2_output.txt"
    ```Shell
  python .\exercise2.py  
  ```
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; You can update the evaluated file and output in exercise2.py
```Python
  grand_prix_world_champion("YOUR INPUT FILE HERE.txt", "YOUR OUTPUT FILE HERE.txt")
  ```
* run exercise 3 - Takes "exercise3_input.txt" as input and the output is write in "exercise3_output.txt"
    ```Shell
  python .\exercise3.py  
  ```
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; You can update the evaluated file and output in exercise3.py
```Python
  minimum_jumps("YOUR INPUT FILE HERE.txt", "YOUR OUTPUT FILE HERE.txt")
  ```
* run exercise 4 - You can upload exercise4.ipynb to google colab and the run all the cells. **You can download the results by executing cell [21] or check output.csv file**
## Unit testing
once you got pytest and pytest-cov intalled to run the unit tests for each exercise run
  ```Shell
  pytest --cov
  ```
the excepted output should look like
```Shell
---------- coverage: platform win32, python 3.11.5-final-0 -----------
Name                      Stmts   Miss  Cover
---------------------------------------------
__init__.py                   0      0   100%
exercise1.py                  6      0   100%
exercise2.py                 46      0   100%
exercise3.py                 23      0   100%
tests\__init__.py             0      0   100%
tests\test_exercise1.py       7      0   100%
tests\test_exercise2.py      37      0   100%
tests\test_exercise3.py      26      0   100%
---------------------------------------------
TOTAL                       145      0   100%


================================================= 11 passed in 0.46s ==================================================

```

