import subprocess


def test_lca():
    expected = ['30', '8']
    process = subprocess.Popen('python lca.py input.txt',
                               shell=True,
                               stdout=subprocess.PIPE)
    output, stderr = process.communicate()
    output = output.splitlines()
    for ex, act in map(None, expected, output):
        assert ex == act
