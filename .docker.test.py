import logging

from dmoj import judgeenv
from dmoj.citest import ci_test
from dmoj.executors import get_available

ALLOW_FAIL = {'GASARM', 'JAVA9', 'JAVA10', 'OBJC'}
OVERRIDES = {}


def main():
    logging.basicConfig(level=logging.INFO)

    judgeenv.env['runtime'] = {}
    judgeenv.env['extra_fs'] = {}

    print('Testing executors...')

    ci_test(get_available(), OVERRIDES, ALLOW_FAIL)


if __name__ == '__main__':
    main()