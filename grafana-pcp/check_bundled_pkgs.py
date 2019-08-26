#!/usr/bin/env python3
import sys
import json
import urllib.request
import tarfile

def update_spec(spec_path, deps_bundle_path):
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

    dependencies = list(package_json['dependencies'].keys()) + list(package_json['devDependencies'].keys())
    deps_bundle = tarfile.open(deps_bundle_path, "r")
    provides = []
    for pkg in dependencies:
        f = deps_bundle.extractfile('node_modules/{}/package.json'.format(pkg))
        pkg_json = json.load(f)
        provides.append('Provides: bundled(nodejs-{}) = {}'.format(pkg_json["name"], pkg_json["version"]))
    deps_bundle.close()
    provides.sort()

    if spec_provides == provides:
        print ('Spec provides section is up-to-date')
        return True
    else:
        print ('Please update the spec file with the following lines:')
        print ('\n'.join(provides))
        return False

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print ("usage: {} grafana.spec grafana-pcp-deps.tar.xz".format(sys.argv[0]))
        sys.exit(1)

    is_uptodate = update_spec(sys.argv[1], sys.argv[2])
    sys.exit(0 if is_uptodate else 1)
