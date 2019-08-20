#!/bin/bash
set -e

VER=$(cat grafana-pcp.spec | grep Version | awk '{print $2}')

pushd $(mktemp -d)
wget https://github.com/performancecopilot/grafana-pcp/archive/v$VER/grafana-pcp-$VER.tar.gz
tar xfz grafana-pcp-$VER.tar.gz
cd grafana-pcp-$VER
yarn install
echo "Compressing..."
XZ_OPT=-9 tar cJf ~/rpmbuild/SOURCES/node_modules-$VER.tar.xz node_modules
popd
