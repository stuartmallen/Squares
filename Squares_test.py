import Squares

class TestClass:
    def test_one(self):
        assert Squares.square(2) == 4

    def test_two(self):
        Squares.square(-1) == 1
