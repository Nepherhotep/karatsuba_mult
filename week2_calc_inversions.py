from tools import load_input_array


def merge_arrays(a, b):
    result = []

    i = 0
    j = 0
    inversions = 0

    while i < len(a) and j < len(b):
        a_item = a[i]
        b_item = b[j]

        if a_item <= b_item:
            result.append(a_item)
            i += 1
        else:
            result.append(b_item)
            j += 1
            inversions += len(a) - i

    for i in range(i, len(a)):
        result.append(a[i])

    for j in range(j, len(b)):
        result.append(b[j])
        inversions += len(a) - i

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
    a = load_input_array('fixtures/inversions.txt')
    inv, r = calc_inversions(a)
    print(inv)
    print(len(r))

