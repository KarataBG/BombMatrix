def matrix_bombing_plan(m):
    T = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(T)

    dictionary = {}
    listOfValues = []
    listTraversed = []

    # Обикаля двуизмерния масив
    for i in range(m):
        for j in range(m):
            adder = 0
            stable = T[i][j] # Взима стойността на текущата стойност от масива
            for a in range(-1, 2):
                for b in range(-1, 2): # Проверява всички съседни в масива
                    if 0 <= i + a < m and 0 <= j + b < m:
                        if T[i + a][j + b] - stable > 0: # Така и изплючва себе си
                            adder += T[i + a][j + b] - stable
                        listTraversed.append([i + a, j + b]) # Записва минаните полета на масива, че да няма повторно итериране

            adder += T[i][j] # Добавя се текущото поле, защото беше записано във втория масив без да бъде добавено

            # Минава неминатите стойности
            for l in range(m):
                for k in range(m):
                    if not listTraversed.__contains__([l, k]):
                        adder += T[l][k]

            # print(listTraversed)
            listTraversed = []
            # print(adder)

            dictionary[(i, j)] = adder

            listOfValues.append(adder)

    # print(list)

    return dictionary


if __name__ == '__main__':
    m = 3

    print(matrix_bombing_plan(m))