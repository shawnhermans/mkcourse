from fire import testutils
from mkcourse.commands import MkCourse


class MkCourseCliTest(testutils.BaseTestCase):
    def testMkCourseBasic(self):
        course = MkCourse()
