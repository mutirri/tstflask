#!/usr/bin/env python

import os
import sys
import unittest
from argparse import ArgumentParser

import coverage

def main():
    from tstflask.core import settings

    parser = ArgumentParser()

    parser.add_argument('source_dir', nargs='?', default='')
    parser.add_argument('-v', '--verbosity', default=2, type=int)
    parser.add_argument('--coverage', action='store_true', default=True)
    parser.add_argument('--no-coverage', action='store_false', dest='coverage')

    args = parser.parse_args()

    if args.coverage:
        import coverage
        cov = coverage.coverage(
            include='**%s**' %
            args.source_dir if args.source_dir else '**/tstflask/**',
            omit=[
                '**/lib/python2.7/**',
                '**/site-packages/**',
                '**/tests/**',
            ])
        cov.start()

    loader = unittest.loader.TestLoader()
    discover_dir = os.path.join(os.path.dirname(__file__), '..', args.source_dir)

    print('Discover %s' % discover_dir)

    loader.discover(os.path.join(os.path.dirname(__file__), "..", ""))

    tests = loader.discover(discover_dir)
    runner = unittest.TextTestRunner(verbosity=args.verbosity)
    result = runner.run(tests)

    if args.coverage:
        cov.stop()
        cov.save()

    sys.exit(0 if result.wasSuccessful() else -1)


if __name__ == '__main__':
    main()
