import subprocess


def test_happy_numbers():
    expected = [1, 1, 0]
    process = subprocess.Popen('python happy_numbers.py input.txt',
                               shell=True,
                               stdout=subprocess.PIPE)
    output, stderr = process.communicate()
    output = output.splitlines()
    for ex, act in map(None, expected, output):
        assert ex == int(act)
