"""Program 22: Check whether two strings are anagrams."""


def is_anagram(first, second):
    first_clean = "".join(first.lower().split())
    second_clean = "".join(second.lower().split())

    return sorted(first_clean) == sorted(second_clean)


if __name__ == "__main__":
    first = input("Enter first string: ")
    second = input("Enter second string: ")
    print(is_anagram(first, second))