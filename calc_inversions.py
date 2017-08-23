

def load_input_array():
    results = []
    with open('fixtures/inversions.txt') as f:
        for line in f.readlines():
            results.append(int(line.strip()))
    return results


def merge_arrays(a, b):
    n = len(a) + len(b)
    m = int(n / 2)
    result = [0] * n

    i = 0
    j = 0
    inversions = 0

    while i < m and j < m:
        a_item = a[i]
        b_item = b[j]

        if a_item <= b_item:
            result[i + j] = a_item
            i += 1
        else:
            result[i + j] = b_item
            j += 1
            inversions += m - i

    for i in range(i, m):
        result[i + j] = a[i]

    for j in range(j, m):
        result[i + j] = b[j]
        inversions += m - i

    return inversions, result


def calc_inversions(arr):
    n = len(arr)

    if n >= 2:
        m = int(n / 2)

        a_inv, a = calc_inversions(arr[:m])
        b_inv, b = calc_inversions(arr[m:])
        inv, result = merge_arrays(a, b)
        return a_inv + b_inv + inv, result

    else:
        return 0, arr


if __name__ == '__main__':
    main()
