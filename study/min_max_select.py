def min_max_select(data):
    is_odd = True if len(data) % 2 == 1 else False
    x_min = data[0] if is_odd else min(data[:2])
    x_max = data[0] if is_odd else max(data[:2])

    i = 0
    while i < len(data) - 1:

        x, y = data[i], data[i + 1]

        if x < y:
            if x < x_min:
                x_min = x
        else:
            if y < x_min:
                x_min = y

        if x > y:
            if x > x_max:
                x_max = x
        else:
            if y > x_max:
                x_max = y

        i += 1

    return x_min, x_max


if __name__ == '__main__':
    data = [29, 0, 2, 3, 1, 5, 7, 18, -1, 4, -12]
    x_min, x_max = min_max_select(data)

    print("Minimum {}, Maximum {}".format(x_min, x_max))
