import unittest
from tests.test_database import DatabaseTestCase

# create a new test suite
suite = unittest.TestSuite([
    unittest.TestLoader().loadTestsFromTestCase(DatabaseTestCase)
])

runner = unittest.TextTestRunner(verbosity=3)
result = runner.run(suite)