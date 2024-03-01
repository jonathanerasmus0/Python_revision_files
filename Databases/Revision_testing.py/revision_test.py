'''import unittest
import unittest.mock




def sum_list():
    l=input("enter 5 digits with space: ")
    l=l.split(" ")
    print(sum(map(int,l)))
    return sum(map(int,l))


#print(sum_list())


class Test_sum_list(unittest.TestCase):
   def test1(self):
       self.variable = " 7 7 7 7 7"
       with patch("builtins.input", return_value=self.variable):
           print(sum_list())
    
if __name__ == '__main__':
    unittest.main()'''
    
    
def write_data(f):
      f.write("123456789012345678")
                


if __name__ == '__main__':
    with open("test.txt", "w") as f:
        write_data(f)

    
