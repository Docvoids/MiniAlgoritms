def interpolation_search(lst, search_item):
    low = 0
    high = len(lst) - 1
    search_res = False

    while (low <= high and search_item >= lst[low]) and search_item <= lst[high] and not search_res:

        middle = low + int(((high - low) / (lst[high] - lst[low])) * (search_item - lst[low]))
        guess = lst[middle]
        if guess == search_item:
            search_res = True
        if guess < search_item:
            low = middle + 1
        else:
            high = middle - 1
    return search_res

list = map(int, input().split())
value = int(input("Введіть елемент пошуку"))

result = interpolation_search(list, value)
if result:
    print("Елемент виявлений!")
else:
    print("Елемент не виявлений")