import textwrap

def wrap(string, max_width):
    i = max_width
    while i < len(string):
        print(string[:i])
        string = string[i:]
        if len(string) < max_width and len(string) != 0:
            return string
    
if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)