@echo off

coverage erase
coverage run -m unittest discover
coverage report --omit="test_*"
coverage html --omit="test_*"