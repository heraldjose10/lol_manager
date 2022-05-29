import unittest
from tests.test_database import DatabaseTestCase
from tests.test_routes import RoutesTestCase

# create a new test suite
suite = unittest.TestSuite([
    unittest.TestLoader().loadTestsFromTestCase(DatabaseTestCase),
    unittest.TestLoader().loadTestsFromTestCase(RoutesTestCase)
])

runner = unittest.TextTestRunner(verbosity=3)
result = runner.run(suite)