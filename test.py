import unittest
import inc_file
import datetime


class IncFileTest(unittest.TestCase):
    ''' Test cases for inc_file.pyw '''

    def test_clean_name(self):
        ''' Test the clean_name function '''
        (path, filename, extension) = inc_file.clean_name(
            'C:\\path\\to\\file name.txt')
        self.assertEqual('C:\\path\\to\\', path)
        self.assertEqual('file name', filename)
        self.assertEqual('.txt', extension)

    def test_is_formatted(self):
        ''' Test the is_formatted function '''
        self.assertTrue(inc_file.is_formatted('1 file name 0123'))
        self.assertFalse(inc_file.is_formatted('file name 0123'))
        self.assertFalse(inc_file.is_formatted('file name 0123 data'))
        self.assertFalse(inc_file.is_formatted('1 0123'))
        self.assertFalse(inc_file.is_formatted('0123'))
        self.assertFalse(inc_file.is_formatted('1 file name'))
        self.assertFalse(inc_file.is_formatted('file name 0123'))
        self.assertFalse(inc_file.is_formatted('file name'))
        self.assertFalse(inc_file.is_formatted('filename'))

    def test_increment_filename(self):
        ''' Test the increment_filename function '''
        date = datetime.date.today().strftime("%m%d")
        self.assertEqual('C:\\path\\to\\2 file name %s.txt' % date,
                         inc_file.increment_filename("C:\\path\\to\\1 file name 0123.txt"))
        self.assertEqual('C:\\path\\to\\1 file name %s.txt' % date,
                         inc_file.increment_filename("C:\\path\\to\\file name.txt"))
        self.assertEqual('C:\\path\\to\\1 1 file name %s.txt' % date,
                         inc_file.increment_filename("C:\\path\\to\\1 file name.txt"))
        self.assertEqual('C:\\path\\to\\1 file name 0123 %s.txt' % date,
                         inc_file.increment_filename("C:\\path\\to\\file name 0123.txt"))

        self.assertEqual('C:\\path\\to\\2 filename %s.txt' % date,
                         inc_file.increment_filename("C:\\path\\to\\1 filename 0123.txt"))
        self.assertEqual('C:\\path\\to\\1 filename %s.txt' % date,
                         inc_file.increment_filename("C:\\path\\to\\filename.txt"))
        self.assertEqual('C:\\path\\to\\1 1 filename %s.txt' % date,
                         inc_file.increment_filename("C:\\path\\to\\1 filename.txt"))
        self.assertEqual('C:\\path\\to\\1 filename 0123 %s.txt' % date,
                         inc_file.increment_filename("C:\\path\\to\\filename 0123.txt"))


if __name__ == '__main__':
    unittest.main()
