from src.utils import MyList


def test_pop_last_element_by_default():
    list = MyList(["a", "b"])
    item_ut = list.pop_with_default()
    assert item_ut == "b"

def test_pop_with_index():
    list = MyList(["a", "b", "c"])
    item_ut = list.pop_with_default(1)
    assert item_ut == "b"

def test_pop_with_default():
    list = MyList()
    item_ut = list.pop_with_default(default="default")
    assert item_ut == "default"

def test_pop_return_none_without_default():
    list = MyList()
    item_ut = list.pop_with_default()
    assert item_ut is None
