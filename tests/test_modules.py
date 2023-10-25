from example_package import module1, module2


def test_module1():
    assert module1.add(2, 2) == 4


def test_module2():
    assert 'module 2' in module2.introduce()