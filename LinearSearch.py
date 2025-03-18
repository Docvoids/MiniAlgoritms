def linear_search(lst, search_item):
    low = 0
    search_result = False

    while low < len(lst) and not search_result:
        if lst[low] == search_item:
            search_result = True
        else:
            low += 1
    return search_result

list = map(int, input().split())
value = int(input("Введіть елемент пошуку"))

result = linear_search(list, value)
if result:
    print("Елемент виявлений!")
else:
    print("Елемент не виявлений")