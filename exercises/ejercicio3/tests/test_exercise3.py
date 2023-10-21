from ejercicio3.exercise3 import minimum_jumps

import pytest
import os


# Test if the number of test cases is between 1 and 1000
def test_t_cases():
    try:
        file_path = os.path.join(os.getcwd(), 'tests',
                                 'file_inputs', 'exercise3_input_2000_test_cases.txt')

        minimum_jumps(file_path, "exercise3_output_test.txt")
    except Exception as e:
        assert str(e) == "The number of test cases must be between 1 and 1000"


# Test if the case value is between 1 and 106
def test_case_values():
    try:
        file_path = os.path.join(os.getcwd(), 'tests',
                                 'file_inputs', 'exercise3_input_200_test_values.txt')

        minimum_jumps(file_path, "exercise3_output_test.txt")
    except Exception as e:
        assert str(e)[-50:] == "The number of test value must be between 1 and 106"


# Test if output file matches with correct answer in exercise3_output_test.txt
def test_correct_answer():
    input_file_path = os.path.join(os.getcwd(), 'tests',
                                   'file_inputs', 'exercise3_input_test.txt')
    output_file_path = os.path.join(os.getcwd(), 'tests',
                                    'file_inputs', 'exercise3_output_test.txt')

    if os.path.exists(output_file_path):
        os.remove(output_file_path)

    minimum_jumps(input_file_path, output_file_path)
    correct_answer = """1 
3 
2 
3 
4 
"""
    f = open(output_file_path, 'r')
    answer = f.read()
    f.close()

    assert correct_answer == answer
