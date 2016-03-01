import mock
import random
import unittest

from approvaltests import Approvals
from approvaltests.TextDiffReporter import TextDiffReporter
from StringIO import StringIO


class TestAscript(unittest.TestCase):
    @mock.patch('sys.stdout', new_callable=StringIO)
    def test(self, stdout):
        random.seed(0)
        import ascript
        reporter = TextDiffReporter()
        Approvals.verify(stdout.getvalue(), reporter)


if __name__ == '__main__':
    unittest.main()
