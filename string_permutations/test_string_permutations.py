from cStringIO import StringIO
import subprocess


def test_string_premutations():
    expected = ['aht,ath,hat,hta,tah,tha',
                'abc,acb,bac,bca,cab,cba',
                '6Zu,6uZ,Z6u,Zu6,u6Z,uZ6']
    process = subprocess.Popen('python string_permutations.py input.txt',
                               shell=True,
                               stdout=subprocess.PIPE)
    output, stderr = process.communicate()
    output = output.splitlines()
    for ex, act in map(None, expected, output):
        assert ex == act
