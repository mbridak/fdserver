#!/bin/bash
pip uninstall -y fdserver
rm dist/*
python3 -m build
pip install -e .
