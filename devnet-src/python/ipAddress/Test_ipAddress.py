import unittest
from io import StringIO
import sys
import os
import pandas as pd
from ipAddress import calculate_subnet_info  # Replace with the name of your script file

class TestSubnetCalculation(unittest.TestCase):

    def setUp(self):
        """Redirect stdout to capture print statements."""
        self.held_output = StringIO()
        sys.stdout = self.held_output

    def tearDown(self):
        """Reset stdout."""
        sys.stdout = sys.__stdout__

    def test_valid_input(self):
        """Test with valid input."""
        calculate_subnet_info(50)
        output = self.held_output.getvalue()
        self.assertIn("Subnet details saved to subnet_details.xlsx.", output)
        
        # Check the output Excel file
        self.assertTrue(os.path.exists("subnet_details.xlsx"))
        df = pd.read_excel("subnet_details.xlsx")
        
        # Check if the file contains subnet details
        self.assertIn("Subnet", df.columns)
        self.assertIn("First Host", df.columns)

    def test_minimum_hosts(self):
        """Test with the minimum number of hosts (2)."""
        calculate_subnet_info(2)
        output = self.held_output.getvalue()
        self.assertIn("Subnet details saved to subnet_details.xlsx.", output)
        
        # Check prefix and usable addresses for this case
        df = pd.read_excel("subnet_details.xlsx")
        self.assertEqual(df.iloc[0]["Usable Addresses"], 2)
        self.assertEqual(df.iloc[0]["Prefix Length"], 30)

    def test_maximum_hosts(self):
        """Test with the maximum number of hosts (250)."""
        calculate_subnet_info(250)
        output = self.held_output.getvalue()
        self.assertIn("Subnet details saved to subnet_details.xlsx.", output)
        
        # Check prefix and usable addresses for this case
        df = pd.read_excel("subnet_details.xlsx")
        self.assertEqual(df.iloc[0]["Usable Addresses"], 250)
        self.assertEqual(df.iloc[0]["Prefix Length"], 24)

    def test_invalid_host_number_too_low(self):
        """Test with a host number less than 2."""
        with self.assertRaises(ValueError) as context:
            calculate_subnet_info(1)
        self.assertIn("The number of hosts must be between 2 and 250.", str(context.exception))

    def test_invalid_host_number_too_high(self):
        """Test with a host number greater than 250."""
        with self.assertRaises(ValueError) as context:
            calculate_subnet_info(300)
        self.assertIn("The number of hosts must be between 2 and 250.", str(context.exception))

    def test_non_integer_input(self):
        """Test with non-integer input."""
        with self.assertRaises(ValueError):
            calculate_subnet_info("fifty")  # Invalid input

if __name__ == "__main__":
    unittest.main()
