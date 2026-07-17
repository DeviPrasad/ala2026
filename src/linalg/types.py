def test_types():
    assert type(3) == int
    assert type((3,)) == tuple
    assert isinstance(3, int)
    assert isinstance((3,), tuple)


def test_equality_and_identity():
    assert 3 == 3
    assert (3,) == (3,)
    assert 3 != 4
    assert (3,) != (4,)
    assert 3 != (3,)
    ## Identity
    a = tuple([10, 20, 30])
    b = tuple([10, 20, 30])
    assert a == b
    assert a is a
    assert b is b
    assert a is not b
    assert b is not a
    assert not a is b
    assert not (tuple([3]) is tuple([3]))
    #
    # Check this out!!
    a = (10, 20, 30)
    b = (10, 20, 30)
    assert a == b
    if a is b:
        print("optimization: 'a' and 'b' are the same object")


if __name__ == "__main__":
    test_types()
    test_equality_and_identity()
