import sys
import pytest

if __name__ == '__main__':
    # sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
    sys.exit(pytest.main(['-v']))

from pkg1 import add_one
from pkg2 import add_two


class TestAddFns:
    def test_add_one(self):
        assert add_one(3) == 4
        
    def test_add_two(self):
        assert add_two(5) == 7

    def test_combined_add(self):
        assert add_one(add_one(1)) == add_two(1)
