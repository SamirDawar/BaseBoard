#!/bin/bash
# Quick incremental rebuild script
# Use this after making code changes

set -e

cd "$(dirname "$0")/build/release"

echo "Running incremental build..."
ninja -j $(sysctl -n hw.ncpu)

echo ""
echo "Build complete!"
echo "Run: ./kicad/kicad.app/Contents/MacOS/kicad"
