def main():
    array = [3, 4, -1, 1]
    result = get_integer(array)
    print(result)


def get_integer(array):
    for x in range(1, max(array)+2):
        if x not in array:
            return x
        else:
            continue


if __name__ == '__main__':
    main()
