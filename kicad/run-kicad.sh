#!/bin/bash
# Run KiCad from the build directory

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
BUILD_DIR="$SCRIPT_DIR/build/release"

if [ ! -d "$BUILD_DIR/kicad/kicad.app" ]; then
    echo "Error: KiCad not built yet!"
    echo "Run ./build-kicad.sh first"
    exit 1
fi

echo "Launching KiCad AI Fork..."
"$BUILD_DIR/kicad/kicad.app/Contents/MacOS/kicad" "$@"
