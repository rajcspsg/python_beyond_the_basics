import contextlib
import sys

@contextlib.contextmanager
def logging_context_manager():
    print('loging context manager enter')
    try:
        yield 'you are within with block'
        print('logging context manager: normal exit')
    except Exception:
        print('logging context manager: Exceptional Exit')
        sys.exc_info()