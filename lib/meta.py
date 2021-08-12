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
import yaml

from commons.versioning import Version, ReleaseState


def blender_version(s):
    # TODO: add some validation to the input
    br, bf, bp = map(int, s.split(','))
    return br, bf, bp


class MetaCommand:

    def __init__(self):
        parser = argparse.ArgumentParser(prog=sys.argv[1])
        sub_parsers = parser.add_subparsers(dest='COMMAND')

        # show subcommand
        show_parser = sub_parsers.add_parser('show')
        show_parser.add_argument(
            dest='FILE',
            type=argparse.FileType('r'),
            help='path to the addon\'s meta data file'
        )

        # bump subcommand
        bump_parser = sub_parsers.add_parser('bump')
        bump_parser.add_argument(
            dest='FILE',
            type=argparse.FileType('r'),
            help='path to the addon\'s meta data yaml file'
        )
        mutex_group = bump_parser.add_mutually_exclusive_group()
        mutex_group.add_argument(
            '-r',
            '--release',
            dest='RELEASE',
            action='store_true',
            help='bumps the release number and resets all other fields to 0'
        )
        mutex_group.add_argument(
            '-f',
            '--feature',
            dest='FEATURE',
            action='store_true',
            help='bumps the feature number and resets all other fields except release to 0'
        )
        mutex_group.add_argument(
            '-p',
            '--patch',
            dest='PATCH',
            action='store_true',
            help='bumps the patch number and resets all other fields except release and feature to 0'
        )
        bump_parser.add_argument(
            '-s',
            '--state',
            dest='STATE',
            type=int,
            help='sets the state (0 - stable, 1 - alpha, 2 - beta, 3 - release candidate), resets increment to 0'
        )
        bump_parser.add_argument(
            '-i',
            '--increment',
            dest='INCREMENT',
            action='store_true',
            help='bumps the state increment'
        )
        bump_parser.add_argument(
            '-b',
            '--blender',
            dest='BLENDER',
            type=blender_version,
            required=False,
            help='sets the blender min version requirement'
        )
        bump_parser.add_argument(
            '-u',
            '--build',
            dest='BUILD',
            type=int,
            required=False,
            help='sets the build number'
        )
        bump_parser.add_argument(
            '-d',
            '--dry-run',
            dest='DRYRUN',
            action='store_true',
            help='the input meta data file will not be changed'
        )

        self._parser = parser

    def exec(self):
        args = self._parser.parse_args(sys.argv[2:])

        if args.COMMAND == 'show':
            self.show(args.FILE)
        elif args.COMMAND == 'bump':
            self.bump(
                args.FILE, args.RELEASE, args.FEATURE, args.PATCH, args.STATE, args.INCREMENT, args.BLENDER, args.BUILD
            )
        else:
            self._parser.print_help()
            exit(1)

    def _parse_yaml(self, file):
        result = yaml.load(file, yaml.FullLoader)
        file.close()
        return result

    def show(self, file):
        data = self._parse_yaml(file)
        print(yaml.dump(data))

    def bump(self, file, release, feature, patch, state, increment, blender, build):
        data = self._parse_yaml(file)
        version = Version.from_string(data['version'])

        kwargs = {
            'release': release,
            'feature': feature,
            'patch': patch,
            'state': ReleaseState.from_value(state) if state else None,
            'increment': increment,
            'blender': blender,
            'build': build
        }

        print(blender)
        print(version)
        print(Version.bump(version, **kwargs))


if __name__ == '__main__':
    MetaCommand().exec()
