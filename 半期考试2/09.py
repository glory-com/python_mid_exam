def sorted_with_weird_order(string_list, order):
    order_dict = {char: index for index, char in enumerate(order)}
    def cmp(word):
        return [order_dict[char] for char in word]
    string_list.sort(key=cmp)

    return string_list