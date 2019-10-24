import os
import sys

boot_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'hook')

def main():
    args = sys.argv[1:]
    os.environ['PYTHONPATH'] = boot_path
    print(os.environ)
    print(sys.executable)
    os.execl(sys.executable, sys.executable, *args)
    pass

if __name__ == '__main__':
    main()