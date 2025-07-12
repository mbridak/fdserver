#!/bin/bash
pip uninstall -y fdserver
rm dist/*
python3 -m build
python3 -m twine upload dist/*
