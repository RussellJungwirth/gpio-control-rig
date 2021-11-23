#!/bin/bash

# Checks for required environment variables to make sure they are present

if [ -z "${PIP_INDEX_URL}" ]; then
  echo "PIP_INDEX_URL not set. Please set it in the proper .env or .bashrc file"
  exit 1
fi
