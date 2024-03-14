def bubble_sort(array):
    """
    Отсортировать список

    Ключевой аргумент:

    array - список, передаваемый для сортировки
    """

    swapped = True

    while swapped:
        swapped = False

        for i in range(len(array) - 1):
            if array[i] > array[i + 1]:

                array[i], array[i + 1] = array[i + 1], array[i]

                swapped = True


list_for_sort = [9, 6, 4, 5, 1, 34, 89, 35]
bubble_sort(list_for_sort)
print(list_for_sort)

