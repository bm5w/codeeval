from cStringIO import StringIO
import sys
import subprocess


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
    expected = ['aht,ath,hat,hta,tah,tha',
                'abc,acb,bac,bca,cab,cba',
                '6Zu,6uZ,Z6u,Zu6,u6Z,uZ6']
    # with Capture() as output:
    process = subprocess.Popen('python string_permutations.py input.txt',
                               shell=True,
                               stdout=subprocess.PIPE)
    output, stderr = process.communicate()
    output = output.splitlines()
    for ex, act in map(None, expected, output):
        assert ex == act
