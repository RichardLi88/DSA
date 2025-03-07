def z_algorithm(txt: str, pat: str):
    z_box = [0] * len(pat)
    l, r = 0, 0
    z_box[0] = 1
    for i in range(1, len(pat)):
        if r < i:
            k, current_length = i, 0
            while (
                k + current_length < len(pat)
                and pat[current_length] == pat[k + current_length]
            ):
                r = k + current_length
                current_length += 1
            if current_length > 0:
                r = k + current_length - 1
                l = k
                z_box[k] = current_length - 1
            else:
                z_box[k] = z_box[k - 1]
        elif z_box[k - l] + k < r:
            z_box[k] = z_box[k - l]
        else:
            k, current_length = i, z_box[k - l]
            while k + current_length < len(pat):
                r = k + current_length
                if r == len(pat):
                    break
                if pat[r + 1] == pat[k - l + current_length + 1]:
                    r += 1
