"""Program 27: Rotate a list to the right by k positions."""


def rotate_list(items, k):
    if not items:
        return []

    k = k % len(items)

    if k == 0:
        return items.copy()

    return items[-k:] + items[:-k]


if __name__ == "__main__":
    items = list(map(int, input("Enter numbers: ").split()))
    k = int(input("Enter rotation positions: "))
    print(rotate_list(items, k))