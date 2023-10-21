def grand_prix_world_champion(input_file, output_file):
    f = open(input_file, 'r')
    line_num = 1
    line = f.readline()
    while line:
        [prixes, pilots] = [int(x)
                            for x in line.strip().split(" ")]
        if prixes == 0 and pilots == 0:
            break
        if not ((prixes > 0 and prixes <= 100) and (pilots > 0 and pilots <= 100)):
            raise Exception(
                f'In input file: line {line_num} - The number of Grand Prixes(G) and Pilots(P) must be between 1 and 100')

        # Get positions matrix
        positions = []
        for prix in range(1, prixes + 1):
            positions.append(f.readline().strip().split(" "))
            line_num += 1

        # Get number of score systems
        score_systems = int(f.readline().strip())
        line_num += 1

        if not (score_systems > 0 and score_systems <= 10):
            raise Exception(
                f'In input file: line {line_num} - The number of Score Systems(S) must be between 1 and 10')

        # Get each score system
        aux = 0
        while (aux < score_systems):
            inputScores = f.readline().strip().split(" ")
            if not (int(inputScores[0]) > 0 and int(inputScores[0]) <= pilots):
                raise Exception(
                    f'In input file: line {line_num} - The number of last finishing order must be between 1 and {pilots}')
            lastFinishing = int(inputScores[0]) + 1
            historicPositions = [0] * pilots

            # Setting historial per player
            for x in range(prixes):
                for y in range(1, lastFinishing):
                    idx = positions[x].index(str(y))
                    historicPositions[idx] += int(inputScores[y])

            # calculate de winner/s
            max = 0
            winner = ""
            count = 1
            for x in historicPositions:
                if max <= int(x):
                    if max == int(x):
                        winner = winner + " " + str(count)
                    else:
                        winner = str(count)
                        max = x
                count += 1

            aux += 1

            f_output = open(output_file, "a")
            f_output.write(winner + "\n")
            f_output.close()
        line = f.readline()

    print(f"Calculations finished successfully see {output_file} file for results")


grand_prix_world_champion("exercise2_input.txt", "exercise2_output.txt")
