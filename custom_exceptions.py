def validate_pwd(pwd):
    if len(pwd) <10:
        raise ValueError # raise a built-in exception
    
# and we can write our own custom exceptions
class PwdTooShort(ValueError): # extend the ValueError exception type
    pass

def validate_pwd2(pwd):
    if len(pwd) <10:
        raise PwdTooShort

if __name__ == '__main__':
    pwd = 'abc' # too short
    # we can throw any exception
    try:
        validate_pwd2(pwd)
    except PwdTooShort as err:
        print(f'Password must be ten characters or more {err}')
    except ValueError as err:
        print(f'oops: password must be ten characters or more {err}')
