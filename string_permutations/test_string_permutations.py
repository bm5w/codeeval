from cStringIO import StringIO
import sys
import fizz_buzz


class Capture(list):
    """Context manager for capturing stdout."""
    def __enter__(self):
        self._stdout = sys.stdout
        sys.stdout = self._stringio = StringIO()

    def __exit__(self, *args):
        self.extend(self._stringio.getvalue().splitlines())
        sys.stdout = self._stdout



expected = ['aht,ath,hat,hta,tah,tha'
            'abc,acb,bac,bca,cab,cba',
            '6Zu,6uZ,Z6u,Zu6,u6Z,uZ6']