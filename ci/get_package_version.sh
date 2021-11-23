#!/usr/bin/env sh
# echos the version number for the package

if echo "$PWD" | grep -q '/ci$'; then
    VERSION_FILE='../src/__init__.py'
else
    VERSION_FILE='src/__init__.py'
fi

if  [ -e "${VERSION_FILE}" ]; then
    grep '^__version__' "${VERSION_FILE}" | sed "s/^[[:space:]]*__version__[[:space:]]*=[[:space:]]*['\"]\{0,1\}\([^'\"]\{1,\}\)*['\"]\{0,1\}/\1/"
else
    echo "UNKNOWN"
fi
