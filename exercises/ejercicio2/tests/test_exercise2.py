from ejercicio2.exercise2 import grand_prix_world_champion

import pytest
import os

# Test if the number of pilots(P) is between 1 and 100


def test_number_of_pilots_exception():
    try:
        file_path = os.path.join(
            os.getcwd(), 'tests', 'file_inputs', 'exercise2_input_200_pilots.txt')
        grand_prix_world_champion(file_path, "exercise2_output_test.txt")
    except Exception as e:
        assert f"{str(e)[-69:]}" == "The number of Grand Prixes(G) and Pilots(P) must be between 1 and 100"

# Test if the number of grand_prix(G) is between 1 and 100


def test_number_of_prix_exception():
    try:
        file_path = os.path.join(
            os.getcwd(), 'tests', 'file_inputs', 'exercise2_input_300_prixes.txt')
        grand_prix_world_champion(file_path, "exercise2_output_test.txt")
    except Exception as e:
        assert f"{str(e)[-69:]}" == "The number of Grand Prixes(G) and Pilots(P) must be between 1 and 100"

# Test if the number of score_systems(S) is between 1 and 10


def test_number_of_score_systems_exception():
    try:
        file_path = os.path.join(
            os.getcwd(), 'tests', 'file_inputs', 'exercise2_input_50_score_systems.txt')
        grand_prix_world_champion(file_path, "exercise2_output_test.txt")
    except Exception as e:
        assert str(
            e)[-55:] == "The number of Score Systems(S) must be between 1 and 10"

# Test if the number of score system description(K) is between 1 and P


def test_number_of_score_system_description_exception():
    try:
        file_path = os.path.join(
            os.getcwd(), 'tests', 'file_inputs', 'exercise2_input_score_description.txt')
        grand_prix_world_champion(file_path, "exercise2_output_test.txt")
    except Exception as e:
        assert "The number of last finishing order must be between 1 and" in str(
            e)


# Test if output file matches with correct answer in exercise2__output_test.txt
def test_correct_answer():
    file_path = os.path.join(os.getcwd(), 'tests',
                             'file_inputs', 'exercise2_output_test.txt')
    input_file_path = os.path.join(os.getcwd(), 'tests',
                                   'file_inputs', 'exercise2_input_test.txt')

    if os.path.exists(file_path):
        os.remove(file_path)
    grand_prix_world_champion(input_file_path, file_path)
    correct_answer = """3
3
1 2 3
3
3
2 4
4
"""
    f = open(file_path, 'r')
    text = f.read()
    assert text == correct_answer
