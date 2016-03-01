import app
import mock
import unittest

from StringIO import StringIO


class TestApp(unittest.TestCase):
    @mock.patch('sys.stdout', new_callable=StringIO)
    def test(self, stdout):
        app.main()
        self.assertEqual(stdout.getvalue(), '')


if __name__ == '__main__':
    unittest.main()
