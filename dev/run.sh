#!/bin/bash

BASE_DIR=$(realpath $(dirname $(realpath $0))/..)

# Check if you are using the correct system for development

DISTRO=$(bash -c "source /etc/os-release; echo \$NAME")
VERSION=$(bash -c "source /etc/os-release; echo \$VERSION_ID")
if [ "$DISTRO" != "Debian GNU/Linux" ] || [ "$VERSION" != "12" ] ; then
    echo "error: Debian GNU/Linux 12 required"
    exit 1
fi

# Check if the required APT packages are installed

packages=(python3 python3-pip python3-venv)

for package in "${packages[@]}"; do
    if ! dpkg -s $package > /dev/null 2>&1; then
        echo "error: missing package $package, try: apt install $package"
        exit 1
    fi
done

# Create a virtual environment for Python

PYENV_DIR="$BASE_DIR/dev/env"

if [ ! -d "$PYENV_DIR" ]; then
    python3 -m venv "$PYENV_DIR"
fi

# Install the required pip packages

"$PYENV_DIR/bin/pip" install -r "$BASE_DIR/app/requirements.txt"

# Run the development server

mkdir -p "$BASE_DIR/dev/log"

export CITHERON_CONFIG_FILE="$BASE_DIR/dev/config.yml"

cd "$BASE_DIR/app"

"$PYENV_DIR/bin/flask" run --debug --host=0.0.0.0
