import unittest
import sys
sys.path.append('../core/')

import logContents

class TestLogContents(unittest.TestCase):

    def test_logContents_n(self):
        list=['fsck_apfs completed at Mon Aug 16 20:36:53 2021\n', 'dev= uuid=00000000-0000-0000-0000-000000000000 vers=1677.120.9 default_ans=n result=0 fp=0 fl=-1 repairs=0 time=0 iter=1\n', 'fsck_apfs completed at Mon Aug 16 20:36:53 2021\n']
        self.assertEqual(logContents.logContents('../Data/testsmall.log', 3, None), list)

    def test_logContents_n_search(self):
        list=['fsck_apfs completed at Mon Aug 16 20:36:53 2021\n', 'fsck_apfs completed at Mon Aug 16 20:36:53 2021\n', 'fsck_apfs completed at Mon Aug 16 20:36:52 2021\n']
        self.assertEqual(logContents.logContents('../Data/testsmall.log', 3, 'completed'), list)

if __name__ == '__main__':
    unittest.main()                           
