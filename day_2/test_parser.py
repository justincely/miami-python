from nose import main
from nose.tools import eq_
import filereader


def test_filereader():
    results = filereader.filereader('2012_12_15.txt')
    assert 'Lewiston' in results
    assert 'Forked_River' in results


def test_add():
    eq_(10, filereader.add(3, 9))


if __name__ == '__main__':
    main()
