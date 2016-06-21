
import unittest
#from Calculator_app import  add1,subtract1,multiply1,divide1,add_3_Numbers1,factorial1,sqrRoot1,square1,power1,floor1
from  Calculator  import Calculator

# test the calculator functionality
class TestCalculator1(unittest.TestCase):
    def setUp(self):
		self.calc = Calculator()

	#  test add function
	#
    def test_calculator_add_method_returns_correct_result(self):
		self.assertEqual(4, self.calc.add1(2, 2))
		self.assertEqual(0, self.calc.add1(-5, 5))
		self.assertEqual(-8, self.calc.add1(-4,-4))

    def test_calculator_add_method_returns_error_result(self):
		self.assertEqual(5, self.calc.add1(2, 2))

    def test_calculator_add_method_returns_nunnumer_error_result(self):
		self.assertEqual(4, self.calc.add1("two", 2))

class TestCalculator2(unittest.TestCase):
    def setUp(self):
		self.calc = Calculator()
		
	#  test subtract function
	#
    def test_calculator_subtract_method_returns_correct_result(self):
		self.assertEqual(0, self.calc.subtract1(2, 2))
		self.assertEqual(-10, self.calc.subtract1(-5, 5))
		self.assertEqual(10, self.calc.subtract1(5,-5))

    def test_calculator_subtract_method_returns_error_result(self):
		self.assertEqual(5, self.calc.subtract1(2, 2))

    def test_calculator_subtract_method_returns_nunnumer_error_result(self):
		self.assertEqual(3, self.calc.subtract1("five", 2))

class TestCalculator3(unittest.TestCase):
    def setUp(self):
		self.calc = Calculator()
		
	#  test multiply function
	#
    def test_calculator_multiply_method_returns_correct_result(self):
		self.assertEqual(4, self.calc.multiply1(2, 2))
		self.assertEqual(-25, self.calc.multiply1(-5, 5))
		self.assertEqual(9, self.calc.multiply1(3,3))

    def test_calculator_multiply_method_returns_error_result(self):
		self.assertEqual(5, self.calc.multiply1(2, 2))

    def test_calculator_multiply_method_returns_nunnumer_error_result(self):
		self.assertEqual(10, self.calc.multiply1("five", 2))


class TestCalculator4(unittest.TestCase):
    def setUp(self):
		self.calc = Calculator()
		
	#  test divide function
	#
    def test_calculator_divide_method_returns_correct_result(self):
		self.assertEqual(1, self.calc.divide1(2, 2))
		self.assertEqual(-5, self.calc.divide1(-25, 5))
		self.assertEqual(3, self.calc.divide1(9,3))

    def test_calculator_divide_method_returns_error_result(self):
		self.assertEqual(5, self.calc.divide1(2, 0))

    def test_calculator_divide_method_returns_nunnumer_error_result(self):
		self.assertEqual(3, self.calc.divide1("six", 2))
		 

class TestCalculator5(unittest.TestCase):
    def setUp(self):
		self.calc = Calculator()
		
	#  test factorial function
	#
    def test_calculator_factorial_method_returns_correct_result(self):
		self.assertEqual(120, self.calc.factorial1(5))
		self.assertEqual(1, self.calc.factorial1(0))

    def test_calculator_factorial_method_returns_error_result(self):
		self.assertEqual(4, self.calc.factorial1(4))

    def test_calculator_factorial_method_returns_nunnumer_error_result(self):
		self.assertEqual(120, self.calc.factorial1("five"))
		 

class TestCalculator6(unittest.TestCase):
    def setUp(self):
		self.calc = Calculator()
		
	#  test sqrRoot function
	#
    def test_calculator_sqrRoot_method_returns_correct_result(self):
		self.assertEqual(3, self.calc.sqrroot1(9))
		self.assertEqual(5, self.calc.sqrroot1(25))
		self.assertEqual(0, self.calc.sqrroot1(0))

    def test_calculator_sqrRoot_method_returns_error_result(self):
		self.assertEqual(-3, self.calc.sqrroot1(-9))

    def test_calculator_sqrRoot_method_returns_nunnumer_error_result(self):
		self.assertEqual(3, self.calc.sqrroot1("nine"))
		 
	

class TestCalculator7(unittest.TestCase):
    def setUp(self):
		self.calc = Calculator()
		
	#  test square function
	#
    def test_calculator_square_method_returns_correct_result(self):
		self.assertEqual(9, self.calc.square1(3))
		self.assertEqual(1, self.calc.square1(1))
		self.assertEqual(9, self.calc.square1(-3))

    def test_calculator_square_method_returns_error_result(self):
		self.assertEqual(-9, self.calc.square1(-3))

    def test_calculator_square_method_returns_nunnumer_error_result(self):
		self.assertEqual(9, self.calc.square1("three"))
		 

class TestCalculator8(unittest.TestCase):
    def setUp(self):
		self.calc = Calculator()
		
	#  test power function
	#
    def test_calculator_power_method_returns_correct_result(self):
		self.assertEqual(27, self.calc.power1(3,3))
		self.assertEqual(.125, self.calc.power1(8,-1))
		self.assertEqual(-3, self.calc.power1(-3,1))

    def test_calculator_power_method_returns_error_result(self):
		self.assertEqual(-9, self.calc.power1(-3,-3))

    def test_calculator_power_method_returns_nunnumer_error_result(self):
		self.assertEqual(9, self.calc.power1("three",3))

		 
class TestCalculator9(unittest.TestCase):
    def setUp(self):
		self.calc = Calculator()
		
	#  test floor function
	#
    def test_calculator_floor_method_returns_correct_result(self):
		self.assertEqual(343, self.calc.floor1(343.93))
		self.assertEqual(22, self.calc.floor1(22.33))
		self.assertEqual(-14, self.calc.floor1(-13.33))

    def test_calculator_floor_method_returns_error_result(self):
		self.assertEqual(23, self.calc.floor1(22.22))

    def test_calculator_floor_method_returns_nunnumer_error_result(self):
		self.assertEqual(3, self.calc.floor1("three.three"))
		 

if __name__ == '__main__':
    unittest.main()
