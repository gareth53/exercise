import os
import sys
import unittest

sys.path.append(os.getcwd())

if __name__ == '__main__':
	try:
		filepath = sys.argv[1]
		path_bits = filepath.split('/')
		directory = "/".join(path_bits[:-1])
		pattern = path_bits[-1]
	except IndexError:
		directory = "tests"
		pattern = "*"

	print(directory, pattern)
	loader = unittest.TestLoader()
	tests = loader.discover(directory, pattern=pattern)

	runner = unittest.TextTestRunner(verbosity=2)
	runner.run(tests)
