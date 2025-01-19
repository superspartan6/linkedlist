import unittest
from linkedlist import LinkedList

class TestLinkedList(unittest.TestCase):


    def setUp(self):
        self.ll = LinkedList()


    def test_addvalue_getsize_returnlist(self):
        self.ll.add_value(10)
        self.assertEqual(self.ll.get_size(), 1)
        self.assertEqual(self.ll.return_list(), [10])

        self.ll.add_value(20)
        self.ll.add_value(15)
        self.assertEqual(self.ll.get_size(), 3)
        self.assertEqual(self.ll.return_list(), [10, 20, 15])


    def test_insertvalue(self):
        self.ll.insert_value(0, 10)
        self.ll.insert_value(0, 12)
        self.assertEqual(self.ll.return_list(), [12, 10])

        self.ll.insert_value(2,7)
        self.ll.insert_value(2,4)
        self.assertEqual(self.ll.return_list(), [12,10,4,7])


    def test_removefirstvalue(self):
        self.ll.add_value(5)
        self.ll.add_value(3)
        self.ll.add_value(5)

        self.ll.remove_first_value(5)
        self.assertEqual(self.ll.return_list(), [3,5])

        self.ll.remove_first_value(5)
        self.assertEqual(self.ll.return_list(), [3])


    def test_removeallvalue(self):
        self.ll.add_value(5)
        self.ll.add_value(3)
        self.ll.add_value(5)

        self.ll.remove_all_value(5)
        self.assertEqual(self.ll.return_list(), [3])

        self.ll.remove_first_value(3)
        self.assertEqual(self.ll.return_list(), [])


    def test_removeindex(self):
        self.ll.add_value(10)
        self.ll.add_value(15)
        self.ll.add_value(20)

        self.ll.remove_index(0)
        self.assertEqual(self.ll.return_list(), [15, 20])

        self.ll.remove_index(1)
        self.assertEqual(self.ll.return_list(), [15])


    def test_removeall(self):
        self.ll.add_value(10)
        self.ll.add_value(15)
        self.ll.add_value(20)

        self.ll.remove_all()
        self.assertEqual(self.ll.return_list(), [])


    def test_searchvalue(self):
        self.ll.add_value(10)
        self.ll.add_value(15)
        self.ll.add_value(20)

        self.assertEqual(self.ll.search_value(10), 0)
        self.assertEqual(self.ll.search_value(15), 1)
        self.assertEqual(self.ll.search_value(20), 2)
        
        self.assertEqual(self.ll.search_value(100), None)


    def test_searchallvalue(self):
        self.ll.add_value(10)
        self.ll.add_value(15)
        self.ll.add_value(10)

        self.assertEqual(self.ll.search_all_value(10), [0,2])
        self.assertEqual(self.ll.search_all_value(15), [1])
        self.assertEqual(self.ll.search_all_value(100), [])


    def test_searchindex(self):
        self.ll.add_value(10)
        self.ll.add_value(15)
        self.ll.add_value(20)

        self.assertEqual(self.ll.search_index(0), 10)
        self.assertEqual(self.ll.search_index(1), 15)
        self.assertEqual(self.ll.search_index(2), 20)


    def test_updateindex(self):
        self.ll.add_value(10)
        self.ll.add_value(15)
        self.ll.add_value(20)

        self.ll.update_index(0, 5)
        self.assertEqual(self.ll.return_list(), [5,15,20])
        self.ll.update_index(1, 5)
        self.assertEqual(self.ll.return_list(), [5,5,20])
        self.ll.update_index(2, 5)
        self.assertEqual(self.ll.return_list(), [5,5,5])


    def test_getsize(self):
        self.assertEqual(self.ll.get_size(), 0)
        self.ll.add_value(10)
        self.assertEqual(self.ll.get_size(), 1)
        self.ll.add_value(15)
        self.assertEqual(self.ll.get_size(), 2)





    def test_outOfRangeExceptions(self):
        self.ll.insert_value(0, 10)
        with self.assertRaises(Exception) as context:   # out of range for insert_value()
            self.ll.insert_value(4,12)
            
        with self.assertRaises(Exception) as context:
            self.ll.insert_value(-2,12)

        with self.assertRaises(Exception) as context:   # out of range for remove_index()
            self.ll.remove_index(4)
            
        with self.assertRaises(Exception) as context:
            self.ll.remove_index(-2)

        with self.assertRaises(Exception) as context:   # out of range for search_index()
            self.ll.search_index(4)
            
        with self.assertRaises(Exception) as context:
            self.ll.search_index(-2)

        with self.assertRaises(Exception) as context:   # out of range for update_index()
            self.ll.update_index(4,12)
            
        with self.assertRaises(Exception) as context:
            self.ll.update_index(-2,12)




    def test_iterations_emptylist(self): #testing iterator with empty list
        values = []

        for node in self.ll:        
            values.append(node)

        self.assertEqual(values, [])

        

    def test_iterations_multiplevalues(self): #testing iterator with multiple values
        values = []

        self.ll.add_value(1)
        self.ll.add_value(2)
        self.ll.add_value(3)

        for node in self.ll:        
            values.append(node)

        self.assertEqual(values, [1,2,3])







if __name__ == "__main__":
    unittest.main()