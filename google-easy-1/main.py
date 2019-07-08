def main():
    array = [10, 15, 3, 7]
    k = 17
    result = check(array, k)
    print(result)

def check(array, k):
    for number in array:
        for x in range(len(array)):
            if array[x] + number == k:
                return True
            else:
                pass
    return False

if __name__ == '__main__':    
    main()