from ARRRtomatic_diff import AutoDiffRev


def test_instantiation_neg():
    x = AutoDiffRev(name='x', val=-3)
    assert x == -3, 'Negative instantiation failed'
    assert x.get_gradient()[0] == 1, 'Negative instantiation failed'


def test_instantiation_pos():
    x = AutoDiffRev(name='x', val=3.5)
    assert x == 3.5, 'Positive instantiation failed'
    assert x.get_gradient()[0] == 1, 'Positive instantiation failed'


def test_instantiation_zero():
    x = AutoDiffRev(name='x', val=0)
    assert x == 0, 'Zero instantiation failed'
    assert x.get_gradient()[0] == 1, 'Zero instantiation failed'


def test_bogus_instantiation():
    try:
        x = AutoDiffRev("gobbledgook")
    except TypeError:
        print("Caught error as expected")


def test_empty_instantiation():
    try:
        x = AutoDiffRev()
    except TypeError:
        print("Caught error as expected")


def test_double_instantiation():
    try:
        x = AutoDiffRev(name='x', val=3, trace=3)
    except TypeError:
        print("Caught error as expected")


def test_nameless_instantiation():
    try:
        x = AutoDiffRev(val=3)
    except ValueError:
        print("Caught error as expected")


def test_diagnose():
    x = AutoDiffRev(name='x', val=-3)
    assert x.diagnose() is None
