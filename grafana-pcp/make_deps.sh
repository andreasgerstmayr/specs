#!/bin/bash
set -e

VER=$(cat grafana-pcp.spec | grep Version | awk '{print $2}')

if [ -f ~/rpmbuild/SOURCES/grafana-pcp-deps-$VER.tar.xz ]; then
    echo "File ~/rpmbuild/SOURCES/grafana-pcp-deps-$VER.tar.xz exists already."
    exit 0
fi

pushd $(mktemp -d)
wget https://github.com/performancecopilot/grafana-pcp/archive/v$VER/grafana-pcp-$VER.tar.gz
tar xfz grafana-pcp-$VER.tar.gz
cd grafana-pcp-$VER
yarn install
echo "Compressing..."
XZ_OPT=-9 tar cJf ~/rpmbuild/SOURCES/grafana-pcp-deps-$VER.tar.xz node_modules
popd
