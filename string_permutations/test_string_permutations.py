from cStringIO import StringIO
import sys
import string_permutations


class Capture(list):
    """Context manager for capturing stdout."""
    def __enter__(self):
        self._stdout = sys.stdout
        sys.stdout = self._stringio = StringIO()
        return self

    def __exit__(self, *args):
        self.extend(self._stringio.getvalue().splitlines())
        sys.stdout = self._stdout


def test_string_premutations():
    expected = ['aht,ath,hat,hta,tah,tha'
                'abc,acb,bac,bca,cab,cba',
                '6Zu,6uZ,Z6u,Zu6,u6Z,uZ6']
    with Capture() as output:
        string_permutations.main('input.txt')
    for ex, act in map(none, expected, output):
        assert ex == act
