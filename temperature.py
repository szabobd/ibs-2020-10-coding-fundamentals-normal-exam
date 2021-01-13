def count(a):
        with open(a, 'r') as in_file:
            list_of_list = [[el] for el in in_file.readlines()]

            complete_list = []
            for i in list_of_list:
                for single in i:
                    complete_list.append(single.split())

            i = 0
            france = []
            sweden = []
            germany = []
            for i in complete_list:
                for counter, j in enumerate(i):
                    print(counter, j)
                    if counter == 0:
                        france.append(j)
                    elif counter == 1:





count('results.txt')