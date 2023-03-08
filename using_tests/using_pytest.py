from collections import namedtuple

# we may need to pip install pytest
# pip install -U pytest

# namedtuple lets us create a tuple with named members
# we can also set defaults for the tuple member values

task = namedtuple('Task', ['owner', 'title', 'completed', 'id'] )
task.__new__.__defaults__ = (None, None, False, None) # choose sensible defaults

# here are some tests
def test_defaults():
    '''test the Task gets the expected default values'''
    t = task()
    s = task(None, None, False, None)
    assert t == s # this is a Pytest assertion

def test_member_access():
    ''' test that the task members can be accessed as expected'''
    t = task('Emily', 'Have lunch') # other members will be default valus
    assert t.owner == 'Emily'
    assert t.title == 'Have lunch'
    assert (t.completed, t.id) == (False, None)

if __name__ == '__main__':
    # t0 = task('Grace', 'talk about pytest', False, 0)
    # t1 = task() # use the defaults
    # print( t0, t1 )
    # we can run tests on our code using pytest
    test_defaults()
    test_member_access()