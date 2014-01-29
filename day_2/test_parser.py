from nose import main
from nose.tools import eq_
import fp


def test_filereader():
    myfp = fp.FileReader()
    results = myfp.process('2012_12_15.txt')
    assert 'Lewiston' in results
    assert 'Forked_River' in results


def test_add():
    myfp = fp.FileReader()
    eq_(12, myfp.add(3, 9))


if __name__ == '__main__':
    main()
