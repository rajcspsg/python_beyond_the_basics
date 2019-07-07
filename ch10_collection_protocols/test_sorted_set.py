import unittest

from sorted_set import *

class TestConstruction(unittest.TestCase):
    
    def test_empty(self):
        s = SortedSet([])
        
    def test_default_empty(self):
        print('test_default_empty')
        s = SortedSet()
        
    def test_from_seq(self):
        s = SortedSet([7, 3, 4, 1])
        
    def test_with_dups(self):
        s = SortedSet([9, 9, 9])
        
    def test_from_iterable(self):
        def gen6842():
            yield 6
            yield 8
            yield 4
            yield 2
            
        s = SortedSet(gen6842())
        
class TestContainer(unittest.TestCase):
    def setUp(self):
        self.s = SortedSet([6,7,3,9])
        
    def test_positive_contained(self):
        self.assertTrue(6 in self.s)
        
    def test_negative_contained(self):
        self.assertFalse(2 in self.s)
        
    def test_positive_not_contained(self):
        self.assertTrue(5 not in self.s)
        
    def test_negative_not_contained(self):
        self.assertFalse(9 not in self.s)
        
class TestSizedProtocol(unittest.TestCase):
    def setUp(self):
        self.s = SortedSet([])
        
    def test_empty(self):
        s = SortedSet([])
        self.assertEqual(len(s), 0)

    def test_one(self):
        s = SortedSet([42])
        self.assertEqual(len(s), 1)
        
    def test_ten(self):
        s = SortedSet(range(10))
        self.assertEqual(len(s), 10)
        
    def test_with_dupls(self):
        s = SortedSet([5,5,5])
        self.assertEqual(len(s), 1)
        
class TestIterableProtocol(unittest.TestCase):
    def setUp(self):
        self.s = SortedSet([7,2,1,1,9])
        
    def test_iter(self):
        i = iter(self.s)
        self.assertEqual(1, next(i))
        self.assertEqual(2, next(i))
        self.assertEqual(7, next(i))
        self.assertEqual(9, next(i))
        self.assertRaises(StopIteration, lambda: next(i))
        
    def test_for_loop(self):
        index = 0
        expected = [1, 2, 7, 9]
        for item in self.s:
            self.assertEqual(item, expected[index])
            index += 1
  
class TestSequenceProtocol(unittest.TestCase):
    # tests for index
    def setUp(self):
        self.s = SortedSet([1,4,9,13,15])
        
    def test_index_zero(self):
        self.assertEqual(1, self.s[0])
        
    def test_index_four(self):
        self.assertEqual(15, self.s[4])
        
    def test_one_beyond_the_end(self):
        with self.assertRaises(IndexError):
            self.s[5]

    def test_index_minus_one(self):
        self.assertEqual(self.s[-1], 15)
    
    def test_index_minus_five(self):
        self.assertEqual(self.s[-5], 1)
        
    def test_index_minus_one_before_the_genesis(self):
        with self.assertRaises(IndexError):
            self.s[-6]
            
    # test for slicing
    
    def test_slice_from_start(self):
        self.assertEqual(self.s[:3], SortedSet([1,4,9]))
        
    def test_slice_to_end(self):
        self.assertEqual(self.s[3:], SortedSet([13, 15]))
        
    def test_slice_arbitrary(self):
        self.assertEqual(self.s[2:4], SortedSet([9,13]))
        
    def test_slice_empty(self):
        self.assertEqual(self.s[10:], SortedSet())
        
    def test_slice_full(self):
        self.assertEqual(self.s[:], self.s)
        
class TestReprProtocol(unittest.TestCase):
    
    def test_empty(self):
        s = SortedSet()
        self.assertEqual(repr(s), "SortedSet()")
        
    def test_repr_some(self):
        s = SortedSet([42, 40, 19])
        self.assertEqual((repr(s)), "SortedSet([19, 40, 42])")

class TestEqualityProtocol(unittest.TestCase):
    def test_positive_equal(self):
        self.assertTrue(SortedSet([4,5,6]) == SortedSet([4,5,6]))
        
    def test_negative_equal(self):
        self.assertFalse(SortedSet([4,5,6]) == SortedSet([1,2,3]))
        
    def test_type_mismatch(self):
        self.assertFalse(SortedSet([4,5,6]) == [4,5,6])
        
    def test_identical(self):
        s = SortedSet([4,5,6])
        self.assertTrue(s == s)
          
if __name__ == '__main__':
    print('running sorted set unit tests')
    unittest.main()