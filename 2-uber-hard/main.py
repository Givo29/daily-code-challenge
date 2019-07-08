def main():
    array = [1, 2, 3, 4, 5]
    result = find_output(array)
    print(result)


def find_output(array):
    result = []
    for x in range(len(array)):
        total = 1
        excluded = array[:x]+array[x+1:]
        for number in excluded:
            total = total * number
        result.append(total)
    return result


if __name__ == '__main__':
    main()
