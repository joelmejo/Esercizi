import unittest
from ex7 import *

class test1(unittest.TestCase):
    def setUp(self) -> None:
        two_words: list[str]= ["Ciao\n", "Aio\n"]
        with open('./Lezione9/EserciziVari/test_ex7.txt', 'w') as ex_input:
            ex_input.writelines(two_words)
        
        with open('./Lezione9/EserciziVari/test_ex7.txt', 'r') as ex_input:
            inputs_list: list[str] = ex_input.readlines()
            self.input1: str= inputs_list[0].strip('\n')
            self.input2: str= inputs_list[1].strip('\n')
    
    def test_result(self):
        with open('./Lezione9/EserciziVari/test_ex7_results.txt', 'w') as results:
            try:
                self.assertEqual(anagram(self.input1, self.input2), True)
                results.writelines(["EXERCISE 7\n", f"{self.input1} and {self.input2} are an anagram of eachother\n\n"])
                result = True
            except AssertionError as e:
                results.writelines(["EXERCISE 7\n", f"{self.input1} and {self.input2} are not an anagram of eachother\n\n"])
                result = False

            if not result:
                self.assertEqual(anagram(self.input1, self.input2), True)

class test2(unittest.TestCase):
    def setUp(self) -> None:
        two_words: list[str]= ["Hola\n", "Halo\n"]
        with open('./Lezione9/EserciziVari/test_ex7.txt', 'w') as ex_input:
            ex_input.writelines(two_words)
        
        with open('./Lezione9/EserciziVari/test_ex7.txt', 'r') as ex_input:
            inputs_list: list[str] = ex_input.readlines()
            self.input1: str= inputs_list[0].strip('\n')
            self.input2: str= inputs_list[1].strip('\n')
    
    def test_result(self):
        with open('./Lezione9/EserciziVari/test_ex7_results.txt', 'a') as results:
            try:
                self.assertEqual(anagram(self.input1, self.input2), True)
                results.write(f"{self.input1} and {self.input2} are an anagram of eachother\n\n")
                result = True
            except AssertionError as e:
                results.write(f"{self.input1} and {self.input2} are not an anagram of eachother\n\n")
                result = False

            if not result:
                self.assertEqual(anagram(self.input1, self.input2), True)

if __name__ == '__main__':
    unittest.main()