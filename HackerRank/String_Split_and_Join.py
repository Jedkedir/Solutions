def split_and_join(line):
    array = line.strip().split()
    return "-".join(array)

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)