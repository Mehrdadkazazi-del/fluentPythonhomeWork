import pytest

from src.pytest.stack import Stack

class TestStack:

    def setup_method(self):
        self.stack_object = Stack()

    @pytest.mark.ex
    def test_stack_is_empty(self):
        assert self.stack_object.is_empty()
        assert len(self.stack_object) == 0
        assert repr(self.stack_object) == "Stack()"
        assert str(self.stack_object) == "Stack()"

        with pytest.raises(IndexError):
            self.stack_object.pop()

    def test_push_one_item(self):
        self.stack_object.push(2)
        assert not self.stack_object.is_empty()
        assert len(self.stack_object) == 1
        assert self.stack_object.top() == 2
        assert repr(self.stack_object) == "Stack()"
        assert str(self.stack_object) == "Stack(2)"

    def test_push_multiple_items(self):
        self.stack_object.push(3)
        self.stack_object.push(4)
        self.stack_object.push(5)
        assert len(self.stack_object) == 3
        assert self.stack_object.top() == 5
        # assert str(self.stack_object) == "Stack(3,4,5)"

    @pytest.mark.non_integer
    def test_push_non_integer_items(self):
        with pytest.raises(TypeError):
            self.stack_object.push("4")
        with pytest.raises(TypeError):
            self.stack_object.push(3.1)
        with pytest.raises(TypeError):
            self.stack_object.push(True)

    @pytest.mark.parametrize("parameter",["4",3.1,True,"test"])
    @pytest.mark.non_integer_items_with_parameters
    def test_push_non_integer_items_with_parameters(self, parameter):
        with pytest.raises(TypeError):
            self.stack_object.push(parameter)

    @pytest.mark.slow_test
    def test_push_multiple_items_until_exception_raises(self):
        for i in range(1_000_000):
            self.stack_object.push(i)

        assert self.stack_object.is_full()

        with pytest.raises(OverflowError):
            self.stack_object.push(254)

    def test_pop_one_item(self):
        self.stack_object.push(1)
        top_item = self.stack_object.pop()

        assert top_item == 1
        assert self.stack_object.is_empty()
        assert len(self.stack_object) == 0

    def test_pop_multiple_items(self):
        self.stack_object.push(1)
        self.stack_object.push(2)

        assert len(self.stack_object) == 2
        assert self.stack_object.pop() == 2
        assert self.stack_object.pop() == 1

        with pytest.raises(IndexError):
            self.stack_object.pop()