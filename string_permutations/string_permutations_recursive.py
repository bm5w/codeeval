import sys
from itertools import permutations


def _perm(input):
    perm = permutations(input)
    output = [''.join(x) for x in perm]
    output.sort()
    print ','.join(output)


def _recursive_perm(input):
    if len(input) < 2:
        return [input]
    else:
        out = []
        for i, char in enumerate(input):
            ss = input[:i] + input[i+1:]
            ss_out = _recursive_perm(ss)
            for x in ss_out:
                out.append(char+x)
        out.sort()
        return out


if __name__ == "__main__":
    input = sys.argv[1]
    print _recursive_perm(input)