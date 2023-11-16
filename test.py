import unittest
import functions

def test_function_definition(test_case, module_name, function_name, expected_num_args):
            # check the function is defined
            function_defined = hasattr(module_name, function_name)
            test_case.assertTrue(function_defined, f"{function_name} is not defined in {module_name}")

            # check the function takes the expected number of arguments
            from_module = getattr(module_name, function_name)
            num_args = len(from_module.__code__.co_varnames)
            test_case.assertEqual(num_args, expected_num_args, f"{function_name} should take {expected_num_args} argument(s)")

        # usage example:
        # test_function_definition(self, functions, 'meal_time', 1)

class TestFunctions(unittest.TestCase):
    longMessage = False

    def test_meal_time(self):
        # check the function is defined & takes correct # arguments
        test_function_definition(self, functions, 'meal_time', 1)

        from functions import meal_time
        
        # breakfast
        result = meal_time("06:59")
        self.assertEqual(result, "nothing right now", "06:59 should be nothing right now")

        result = meal_time("07:00")
        self.assertEqual(result, "breakfast", "07:00 should be breakfast")

        result = meal_time("07:23")
        self.assertEqual(result, "breakfast", "07:23 should be breakfast")

        result = meal_time("08:00")
        self.assertEqual(result, "breakfast", "08:00 should be breakfast")

        result = meal_time("08:01")
        self.assertEqual(result, "nothing right now", "08:01 should be nothing right now")

        # lunch
        result = meal_time("11:59")
        self.assertEqual(result, "nothing right now", "11:59 should be nothing right now")

        result = meal_time("12:00")
        self.assertEqual(result, "lunch", "12:00 should be lunch")

        result = meal_time("12:33")
        self.assertEqual(result, "lunch", "12:33 should be lunch")

        result = meal_time("13:00")
        self.assertEqual(result, "lunch", "13:00 should be lunch")

        result = meal_time("13:01")
        self.assertEqual(result, "nothing right now", "13:01 should be nothing right now")

        # dinner
        result = meal_time("17:59")
        self.assertEqual(result, "nothing right now", "17:59 should be nothing right now")

        result = meal_time("18:00")
        self.assertEqual(result, "dinner", "18:00 should be dinner")

        result = meal_time("18:23")
        self.assertEqual(result, "dinner", "18:23 should be dinner")

        result = meal_time("19:00")
        self.assertEqual(result, "dinner", "19:00 should be dinner")

        result = meal_time("19:01")
        self.assertEqual(result, "nothing right now", "19:01 should be nothing right now")

        # inappropriate times
        result = meal_time("00:00")
        self.assertEqual(result, "nothing right now", "00:00 should be nothing right now")

        result = meal_time("03:21")
        self.assertEqual(result, "nothing right now", "03:21 should be nothing right now")

        result = meal_time("14:09")
        self.assertEqual(result, "nothing right now", "14:09 should be nothing right now")

        result = meal_time("22:49")
        self.assertEqual(result, "nothing right now", "22:49 should be nothing right now")

    def test_get_filename_extension(self):
        # check the function is defined & takes correct # arguments
        test_function_definition(self, functions, 'get_filename_extension', 1)

        from functions import get_filename_extension

        result = get_filename_extension("hello.txt")
        self.assertEqual(result, "txt", "hello.txt has extension 'txt'")

        result = get_filename_extension("hello.py")
        self.assertEqual(result, "py", "hello.py has extension 'py'")

        result = get_filename_extension("data.json")
        self.assertEqual(result, "json", "data.json has extension 'json'")

        result = get_filename_extension("data.csv")
        self.assertEqual(result, "csv", "data.csv has extension 'csv'")

        result = get_filename_extension("kitty.jpg")
        self.assertEqual(result, "jpg", "kitty.jpg has extension 'jpg'")

    def test_is_image_file(self):
       # check the function is defined & takes correct # arguments
        test_function_definition(self, functions, 'get_filename_extension', 1)

        from functions import is_image_file

        result = is_image_file("hello.txt")
        self.assertEqual(result, False, "hello.txt is not an image file")

        result = is_image_file("kitty.jpg")
        self.assertEqual(result, True, "kitty.jpg is an image file")

        result = is_image_file("data.csv")
        self.assertEqual(result, False, "data.csv is not an image file")

        result = is_image_file("data.jpeg")
        self.assertEqual(result, True, "data.jpeg is an image file")

        result = is_image_file("data.json")
        self.assertEqual(result, False, "data.json is not an image file")

        result = is_image_file("data.png")
        self.assertEqual(result, True, "data.png is an image file")

        result = is_image_file("clouds.gif")
        self.assertEqual(result, True, "clouds.gif is an image file")

        result = is_image_file("monitor.tiff")
        self.assertEqual(result, True, "monitor.tiff is an image file")


if __name__ == '__main__':
    unittest.main(verbosity=2, exit=False, catchbreak=False)
