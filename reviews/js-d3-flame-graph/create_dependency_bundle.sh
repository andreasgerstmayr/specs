#!/bin/bash -eu

SRC=$(readlink -f "${1:?Usage: $0 source destination}")
DEST=$(readlink -f "${2:?Usage: $0 source destination}")

if [ -f "$DEST" ]; then
    echo "File $DEST exists already."
    exit 0
fi
if [ "$#" -gt 2 ]; then
    PATCHES=$(readlink -f "${@:3}")
else
    PATCHES=""
fi

pushd "$(mktemp -d)"

echo Extracting sources...
tar xfz "$SRC"
ls
cd d3-flame-graph-*

echo Applying patches...
for patch in $PATCHES
do
    patch -p1 < $patch
done

echo Installing dependencies...
npm install

echo Compressing...
XZ_OPT=-9 tar cJf "$DEST" node_modules

popd
