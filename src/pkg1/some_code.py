import pytest


def add_one(n: int) -> int:
    return n + 1

if __name__ == '__main__':
    print('some_code.py')
    pytest.main(['-v'])
