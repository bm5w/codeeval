import interrupted_bubble_sort
import sys
from cStringIO import StringIO


class Capture(list):
    """Context manager for capturing stdout."""
    def __enter__(self):
        self._stdout = sys.stdout
        self.stdout = self._stringio = StringIO()
        return self

    def __exit__(self, *args):
        self.extend(self._stringio.getvalue().splitlines())
        sys.stdout = self._stdout


def test_sample():
    expected = ['36 47 28 20 78 79 16 8 45 72 69 81 66 60 8 3 86 87 90 90',
                '40 42 24 16 52 66 69',
                ('0 15 25 18 34 5 21 46 47 48 48 1 43 50 53 29 54 62 74 74' +
                 ' 76 78'),
                '5 48 18 51 61',
                '55 31 59 4 1 25 26 19 60 0 68 73']
    with Capture() as output:
        interrupted_bubble_sort.main('input.txt')
    for exp, act in map(None, expected, output):
        assert exp == act
