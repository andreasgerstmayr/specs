#!/usr/bin/env python3
import sys
import json
import urllib.request


def update_spec(spec_path):
    version = None
    spec_provides = []
    with open(spec_path) as spec:
        for line in spec.readlines():
            line = line.strip()
            if 'Version:' in line:
                version = line.split()[1]
            elif 'Provides: bundled(nodejs-' in line:
                spec_provides.append(line)

    if not version:
        raise 'Version not found'

    package_json_url = 'https://raw.githubusercontent.com/performancecopilot/grafana-pcp/release-{}/package.json'.format(version)
    package_json = None
    with urllib.request.urlopen(package_json_url) as response:
        package_json = json.loads(response.read())

    yarn_lock_url = 'https://raw.githubusercontent.com/performancecopilot/grafana-pcp/release-{}/yarn.lock'.format(version)
    yarn_lock = None
    with urllib.request.urlopen(yarn_lock_url) as response:
        yarn_lock = response.read().decode('utf8')

    dependencies = list(package_json['dependencies'].keys()) + list(package_json['devDependencies'].keys())
    yarn_lock = '\n'.join((yarn_lock.split('\n'))[4:]) # skip header
    provides = []
    for pkg in yarn_lock.split('\n\n'):
        lines = pkg.split('\n')
        pkg_name = lines[0].split('@')[0]
        pkg_version = lines[1].split('"')[1]

        if pkg_name in dependencies:
            provides.append('Provides: bundled(nodejs-{}) = {}'.format(pkg_name, pkg_version))

    if spec_provides == provides:
        print ('Spec provides section is up-to-date')
        return True
    else:
        print ('Please update the spec file with the following lines:')
        print ('\n'.join(provides))
        return False

if __name__ == '__main__':
    is_uptodate = update_spec(sys.argv[1])
    sys.exit(0 if is_uptodate else 1)
