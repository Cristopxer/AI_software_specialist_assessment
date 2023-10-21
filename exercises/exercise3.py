def minimum_jumps(input_file, output_file):
    """Calculates the minimum number of jumps between 0 and case_value(x)
    only allowing to jump y + k (k is the number of jumps done)
    and y - 1

    Args:
      input_file: A string containing the path to the input file
      output_file: A string containing the path to the output file

    Returns:
      An output file with the results of minimun number of jumps to reach case_value(x) and a banner confirming the end of the calculations.
    """
    f = open(input_file, 'r')

    # Get number of test cases (t)
    t_cases = int(f.readline().strip())
    if not (t_cases > 0 and t_cases <= 1000):
        raise Exception(f"The number of test cases must be between 1 and 1000")

    # Iterates through the file test_cases times to get the case values(x)
    line = 1
    while (t_cases > 0):

        case_value = int(f.readline().strip())
        line += 1

        if not (case_value > 0 and case_value <= 106):
            raise Exception(
                f"In input file: line {line} - The number of test value must be between 1 and 106")

        for i in range(1, case_value+1):
            if(i * (i+1) >= 2*case_value):
                break
        currentPoint = ((i * (i+1))/2)
        if(currentPoint == case_value+1):
            i += 1

        # Saving the results
        f_output = open(output_file, 'a')
        f_output.write(f"{i} \n")
        f_output.close()

        t_cases -= 1

    print("Jumps successfully calculated")


minimum_jumps("exercise3_input.txt", "exercise3_output.txt")
