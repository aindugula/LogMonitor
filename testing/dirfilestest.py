import unittest
import sys
sys.path.append('../core/')

import listFilesInDir as filesList

class TestFilesInDirMethods(unittest.TestCase):

    def test_numfiles(self):
        self.assertEqual(len(filesList.listFilesInDir('../Data/')), 5)

    def test_fileslist(self):
        list=['testempty.log', 'system.log', 'wifi.log', 'testsmall.log', 'testlarge.log']
        self.assertEqual(filesList.listFilesInDir('../Data'), list)
 
if __name__ == '__main__':
    unittest.main()
