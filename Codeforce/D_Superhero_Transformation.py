import sys
def solution():
    data = sys.stdin.read().split()
    if len(data) < 2:
        return
    it = iter(data)
    s = next(it)
    t = next(it)
    if len(s) != len(t):
        print("No")
        return
    vowels = set("aeiou")
    for char_s, char_t in zip(s, t):
        if (char_s in vowels) != (char_t in vowels):
            print("No")
            return
    print("Yes")
if __name__ == "__main__":
    solution()