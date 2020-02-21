# js-d3-flame-graph

The js-d3-flame-graph package

## Build instructions
```
VER=2.1.9
spectool -g js-d3-flame-graph.spec
./create_dependency_bundle.sh d3-flame-graph-$VER.tar.gz d3-flame-graph-deps-$VER.tar.xz
./check_npm_dependencies.py js-d3-flame-graph.spec d3-flame-graph-$VER.tar.gz d3-flame-graph-deps-$VER.tar.xz
fedpkg new-sources d3-flame-graph-$VER.tar.gz d3-flame-graph-$VER.tar.xz

fedpkg local
fedpkg lint
fedpkg mockbuild
fedpkg scratch-build --srpm

fedpkg build
fedpkg update
```
