


def find_first_non_repeating(lst):
    
    count = {}

    for item in lst:
        count[item] = count.get(item, 0) + 1

    for item in lst:
        if count[item] == 1:
            # print(item)
            return item
    else:
        print("No non-repeating element found")

def find_first_non_repeating_using_ordered_dict(lst):
    from collections import Counter

    count = Counter(lst)

    # for item in lst:
    #     count[item] = count.get(item, 0) + 1

    for item, cnt in count.items():
        if cnt == 1:
            return item
    else:
        print("No non-repeating element found")

def find_the_second_non_repeating(lst):
    count = {}

    for item in lst:
        count[item] = count.get(item, 0) + 1

    non_repeating_elements = [item for item in lst if count[item] == 1]

    if len(non_repeating_elements) >= 2:
        return non_repeating_elements[1]
    else:
        print("No second non-repeating element found")

if __name__ == "__main__":
    lst = [1, 2, 3, 2, 1, 4, 5]
    # print(find_first_non_repeating(lst))
    # print(find_first_non_repeating_using_ordered_dict(lst))
    print(find_the_second_non_repeating(lst))
