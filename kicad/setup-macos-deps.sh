#!/bin/bash
# KiCad macOS Build Dependencies Installation Script
# This script installs all required dependencies for building KiCad on macOS

set -e

echo "======================================"
echo "KiCad Build Dependencies Setup"
echo "======================================"
echo ""

# Check if Homebrew is installed
if ! command -v brew &> /dev/null; then
    echo "Error: Homebrew is not installed."
    echo "Please install Homebrew from https://brew.sh/"
    exit 1
fi

echo " Homebrew detected"
echo ""

# Update Homebrew
echo "Updating Homebrew..."
brew update

echo ""
echo "Installing KiCad build dependencies..."
echo "This may take 15-30 minutes depending on your system..."
echo ""

# Core build tools
brew install cmake ninja

# Required libraries
brew install wxwidgets boost glew glm cairo curl protobuf python@3

# Optional but recommended libraries
brew install ngspice opencascade nng swig doxygen

echo ""
echo "======================================"
echo "Dependency Installation Complete!"
echo "======================================"
echo ""
echo "Verifying installations..."
cmake --version
python3 --version
ninja --version

echo ""
echo "Next steps:"
echo "1. Run: mkdir -p build/release && cd build/release"
echo "2. Run: cmake -G Ninja -DCMAKE_BUILD_TYPE=RelWithDebInfo ../.."
echo "3. Run: ninja"
echo ""
