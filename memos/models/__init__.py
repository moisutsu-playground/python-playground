from importlib import reload

from .test1 import test_a

reload(test1)
test_a = test1.test_a
