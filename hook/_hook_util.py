import functools
import importlib
import sys
import time
import logging

LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
logging.basicConfig(filename='web.log', level=logging.DEBUG, format=LOG_FORMAT)

_modules_name = {'mock'}

class ModeuleFinder:
    def find_module(self, module_name, path):
        print('find %s' % (module_name))
        if module_name in _modules_name:
            return PathReloader()


class PathReloader:

    def load_module(self, module_name):
        print('load  %s' % (module_name))
        if module_name in sys.modules:
            return sys.modules[module_name]
        finder = sys.meta_path.pop(0)

        module = importlib.import_module(module_name)

        module_hook(module_name, module)

        sys.meta_path.insert(0, finder)
        return module

sys.meta_path.insert(0, ModeuleFinder())


def module_hook(module_name, module):
    if module_name == 'mock':
        module.mock_db = request_check(module.mock_db)
        module.mock_db = get_execution_time(module.mock_db)

def get_execution_time(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        logging.info('%s spent %s s' % (func.__name__,(end - start)))
        print('%s spent %s s' % (func.__name__,(end - start)))
        return result
    return wrapper

def request_check(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if 'delete' in args:
            logging.warning('being attacked')
            return '403 Forbidden '
        result = func(*args, **kwargs)
        return result
    return wrapper