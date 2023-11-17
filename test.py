import unittest
import functions
import inspect

def test_function_definition(test_case, module_name, function_name, expected_num_args):
    # check the function is defined
    module = __import__(module_name)
    function_defined = hasattr(module, function_name)
    test_case.assertTrue(function_defined, f"{function_name} is not defined in {module_name}")

    # check the function takes correct # arguments
    function = getattr(module, function_name)
    signature = inspect.signature(function)
    num_arguments = len(signature.parameters)

    test_case.assertEqual(num_arguments, expected_num_args, f"{function_name} should take {expected_num_args} argument(s)")

class TestFunctions(unittest.TestCase):
    longMessage = False

    def test_meal_time(self):
        # check the function is defined & takes correct # arguments
        test_function_definition(self, "functions", 'meal_time', 1)

        from functions import meal_time
        
        test_cases = {
            "00:00": "nothing at this time",
            "6:30": "nothing at this time",
            "6:59": "nothing at this time",
            "7:30": "breakfast",
            "8:01": "nothing at this time",
            "10:00": "nothing at this time",
            "11:59": "nothing at this time",
            "12:45": "lunch",
            "13:01": "nothing at this time",
            "17:59": "nothing at this time",
            "18:30": "dinner",
            "19:01": "nothing at this time",
            "23:45": "nothing at this time",
        }

        for time_string, expected_result in test_cases.items():
            with self.subTest(time_string=time_string):
                result = meal_time(time_string)
                self.assertEqual(result, expected_result, f"{time_string} should give {expected_result}")

    def test_get_filename_extension(self):
        # check the function is defined & takes correct # arguments
        test_function_definition(self, "functions", 'get_filename_extension', 1)

        from functions import get_filename_extension

        test_cases = {
            "hello.txt": "txt",
            "hello.py": "py",
            "data.json": "json",
            "data.csv": "csv",
            "kitty.jpg": "jpg",
        }

        for filename, expected_extension in test_cases.items():
            with self.subTest(filename=filename):
                result = get_filename_extension(filename)
                self.assertEqual(result, expected_extension, f"{filename} has extension {expected_extension}")

    def test_is_image_file(self):
       # check the function is defined & takes correct # arguments
        test_function_definition(self, "functions", 'get_filename_extension', 1)

        from functions import is_image_file

        test_cases = {
            "hello.txt": False,
            "kitty.jpg": True,
            "data.csv": False,
            "data.jpeg": True,
            "data.json": False,
            "data.png": True,
            "clouds.gif": True,
            "monitor.tiff": True,
        }

        for filename, expected_result in test_cases.items():
            with self.subTest(filename=filename):
                result = is_image_file(filename)
                self.assertEqual(result, expected_result, f"{filename} is {'' if expected_result else 'not'} an image file")


if __name__ == '__main__':
    unittest.main(verbosity=2, exit=False, catchbreak=False)
