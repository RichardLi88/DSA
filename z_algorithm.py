def z_algorithm(txt: str, pat: str):
    joined_str = pat + "$" + txt
    z_box = [0] * len(joined_str)
    # l is the start of the substring with the highest right index that matches the start of the list
    # r is the right most index of the substring that matches the start of the list so far
    l, r = 0, 0
    z_box[0] = 1
    print(joined_str[1] == joined_str[0])
    for i in range(1, len(z_box)):
        print(joined_str)
        k = i
        length = 0
        if r > i:
            if z_box[k - l] >= r:
                while k < len(z_box) and joined_str[k] == joined_str[length]:
                    length += 1
                    k += 1
                z_box[i] = k - 1
                l = i
                r = k - 1

            else:
                z_box[i] = z_box[i - l]
        else:
            while k < len(joined_str) and joined_str[k] == joined_str[length]:
                length += 1
                k += 1
            if length == 0:
                z_box[i] = 0
            else:
                l = i
                r = k - 1
                z_box[i] = k - l
        print(z_box)
    return z_box


if __name__ == "__main__":
    test_str = "abcd"
    txt = "aabcuiuabcd"
    print(z_algorithm(txt, test_str))
