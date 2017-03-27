import os
import sys
import unittest

sys.path.append(os.getcwd())

if __name__ == '__main__':
	try:
		filepath = sys.argv[1]
		directory, pattern = filepath.split('/')
	except IndexError:
		directory = "tests"
		pattern = "*"

	loader = unittest.TestLoader()
	tests = loader.discover(directory, pattern=pattern)

	runner = unittest.TextTestRunner(verbosity=2)
	runner.run(tests)
