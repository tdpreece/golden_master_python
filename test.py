import app
import mock
import random
import unittest

from StringIO import StringIO


class TestApp(unittest.TestCase):
    @mock.patch('sys.stdout', new_callable=StringIO)
    def test(self, stdout):
        random.seed(0)
        app.main()
        self.assertEqual(
            stdout.getvalue(),
            (
                '0.844421851525\n0.75795440294\n0.420571580831\n'
                '0.258916750293\n0.511274721369\n0.40493413745\n'
                '0.783798589035\n0.303312726079\n0.476596954152\n'
                '0.583382039455\n'
            )
        )


if __name__ == '__main__':
    unittest.main()
