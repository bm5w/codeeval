from cStringIO import StringIO
import sys
import fizz_buzz


class Capture(list):
    """Context manager for capturing stdout."""
    def __enter__(self):
        self._stdout = sys.stdout
        sys.stdout = self._stringio = StringIO()
        return self

    def __exit__(self, *args):
        self.extend(self._stringio.getvalue().splitlines())
        sys.stdout = self._stdout


def test_fizz_buzz():
    expected = ['1 2 F 4 B F 7 8 F B', '1 F 3 F 5 F B F 9 F 11 F 13 FB 15']
    with Capture() as output:
        fizz_buzz.main("input_test.txt")
    assert len(expected) == len(output)
    for ex, act in zip(expected, output):
        assert ex == act
