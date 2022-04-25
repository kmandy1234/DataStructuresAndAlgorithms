import unittest
from linked_list_ds import SingleList

class TestLinkedList(unittest.TestCase):
    def test_insert_end(self):
        a = SingleList()
        a.addNodeEnd(2)
        a.addNodeEnd(4)
        a.addNodeEnd(8)
        res = a.display()
        self.assertEqual(res, [2, 4, 8])
    
    def test_insert_start(self):
        a = SingleList()
        a.addNodeStart(3)
        a.addNodeStart(2)
        self.assertEqual(a.display(),[2,3])
    
    def test_insert_specified_pos(self):
        a = SingleList()
        a.addNodePosition(4, 0)
        a.addNodePosition(6, 1)
        a.addNodePosition(5, 1)
        self.assertEqual(a.display(),[4,5,6])
    
    def test_display_empty(self):
        a = SingleList()
        self.assertEqual(a.display(),[])

    def test_assert(self):
        with self.assertRaises(Exception) as context:
            a= SingleList()
            a.addNodePosition(4, 0)
            a.addNodePosition(6, 1)
            a.addNodePosition(5, 1)
            a.addNodePosition(8, 4)
        self.assertTrue('specified pos is exceeding the length of ll' in str(context.exception))

    def test_cal_length_empty(self):
        a = SingleList()
        self.assertEqual(a.calLength(), 0)
    
    def test_cal_length_non_empty(self):
        a = SingleList()
        a.addNodeEnd(2)
        self.assertEqual(a.calLength(), 1)



if __name__ == "__main__":
    unittest.main()