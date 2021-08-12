# blender-addons-build-scripts
# Copyright (C) 2021 coldrye solutions, Carsten Klein and Contributors
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.


import argparse
import sys


class BLinfoCommand:

    def __init__(self):
        parser = argparse.ArgumentParser(prog=sys.argv[1])
        sub_parsers = parser.add_subparsers(dest='COMMAND')

        # show subcommand
        show_parser = sub_parsers.add_parser('show')
        show_parser.add_argument(
            dest='FILE',
            type=argparse.FileType('r', 0),
            help='path to the addon\'s __init__.py file'
        )

        # update subcommand
        update_parser = sub_parsers.add_parser('update')
        update_parser.add_argument(
            '-s',
            '--source',
            metavar='SOURCE',
            type=argparse.FileType('r', 0),
            required=True,
            help='path to the addon\'s __init__.py file'
        )
        update_parser.add_argument(
            '-m',
            '--meta',
            metavar='META',
            type=argparse.FileType('r', 0),
            required=True,
            help='path to the version meta data file'
        )

        self._parser = parser

    def exec(self):
        args = self._parser.parse_args(sys.argv[2:])

        if args.COMMAND == 'show':
            self.show(args.FILE)
        elif args.COMMAND == 'update':
            self.update(args.SOURCE, args.META)
        else:
            self._parser.print_help()
            exit(1)

    def show(self, file):
        pass

    def update(self, source, meta):
        pass


# TODO
def version_warning(version: Version) -> str:
    result = []
    if version.state == ReleaseState.ALPHA:
        result.append('This is an early alpha release.')
    elif version.state == ReleaseState.BETA:
        result.append('This is an early beta release.')
    elif version.state == ReleaseState.RC:
        result.append('This is a release candidate release.')
    if result:
        result.append('Refer to the documentation for more information.')
    # TBD: add more links to build and release tag
    return ' '.join(result)


# TODO
def version_documentation_link(version: Version) -> str:
    return 'https://github.com/coldrye-solutions/blender-addon-rigified/docs/' + str(version)



if __name__ == '__main__':
    BLinfoCommand().exec()
