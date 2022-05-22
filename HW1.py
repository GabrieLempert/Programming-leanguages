def sum_of_list(list_of):
    sum_list = 0
    for x in list_of:
        sum_list = sum(x) + sum_list
    return sum_list


def reverse_list(list_inside):
    return list_inside[::-1]


def reverse_list_of_list(list_of_list):
    for x in list_of_list:
        if type(x) == list:
            list_of_list[list_of_list.index(x)] = reverse_list(x)
    return reverse_list(list_of_list)


def reverse_string(string):
    return string[::-1]


def reverse_tuple(tuples_q3):
    new_tup = tuples_q3[::-1]
    return new_tup


def test_q2():
    assert (sum_of_list([[1, 2], [3, 4], [5, 6]]) == 21)
    assert (sum_of_list([[1], [3, 4], [5, 6]]) == 19)
    assert (sum_of_list([[-1], [3.4, 4], [5.2, 6]]) == 17.6)


def sort_tuples(tuples_q4):
    new_list = []
    new_list1 = set()
    for x in tuples_q4:
        for y in x:
            if type(y) == str:
                new_list.append(y)
        new_list.sort()
    for x in tuples_q4:
        for y in x:
            if type(y) != str:
                new_list1.add(y)
    new_list1 = sorted(new_list1)
    for x in new_list1:
        new_list.append(x)
    return new_list


def sort_tuples_dictionary(tuples_q4_b):
    dict1 = {}
    y = 0
    for x in sort_tuples(tuples_q4_b):
        dict1[y] = x
        y = y + 1
    return dict1


def tests_q3():
    # A
    assert (reverse_string("gabi lempert"))
    assert (reverse_string("ella peled"))
    assert (reverse_string("Dobby the dog"))
    # B
    assert (reverse_list_of_list([[1, 2], [3, 4], [5, 6]]) == [[6, 5], [4, 3], [2, 1]])
    assert (reverse_list_of_list([[1, [1, 3], 2], 5, 6]) == [6, 5, [2, [1, 3], 1]])
    assert (reverse_list_of_list([1, 2, 3, 4, 5]) == [5, 4, 3, 2, 1])
    # C
    assert (reverse_tuple((3, 'a', 'd', 'f', 'g', 'e', 'e', 'k')) == ('k', 'e', 'e', 'g', 'f', 'd', 'a', 3))
    assert (reverse_tuple((3, 'a', 5.5, [1, 2], 'g', 'e', 'e', "gabi")) == ('gabi', 'e', 'e', 'g', [1, 2], 5.5, 'a', 3))
    assert (reverse_tuple((3, 4, 5.5, [1, 2], 'z', 2, 'e', "ella")) == ('ella', 'e', 2, 'z', [1, 2], 5.5, 4, 3))


def test_q4():
    # A
    assert (
            sort_tuples(({2, 4, 3}, {'f', 'h', 'u', 'r', 'b', 'n', 'd'})) == ['b', 'd', 'f', 'h', 'n', 'r', 'u', 2, 3,
                                                                              4])
    assert (sort_tuples(({2, 4, 3, 'g', 'd'}, {'f', 'h', 'u', 1, 3, 4})) == ['d', 'f', 'g', 'h', 'u', 1, 2, 3, 4])
    # B
    assert (sort_tuples_dictionary(({2, 4, 3, 'g', 'd'}, {'f', 'h', 'u', 1, 3, 4})) == {0: 'd', 1: 'f', 2: 'g', 3: 'h',
                                                                                        4: 'u', 5: 1, 6: 2, 7: 3, 8: 4})
    assert (sort_tuples_dictionary(({2, 1.3, 3, 'g', 'd'}, {4.6, 2, 'h', 'A', 1, 3})) == {0: 'A', 1: 'd', 2: 'g',
                                                                                          3: 'h', 4: 1, 5: 1.3, 6: 2,
                                                                                          7: 3, 8: 4.6})
    

if __name__ == '__main__':
    test_q2()
    tests_q3()
    test_q4()
# 