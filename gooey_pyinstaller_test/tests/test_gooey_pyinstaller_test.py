#!/usr/bin/env python
# coding: utf-8

"""
test_gooey_pyinstaller_test
----------------------------------
Tests for `gooey_pyinstaller_test` module.
"""

# Third Party Libraries
import logging
import pytest

# Gooey PyInstaller test Modules
# from gooey_pyinstaller_test import gooey_pyinstaller_test

# pylint: disable=redefined-outer-name, unused-argument

log = logging.getLogger(__name__)

@pytest.fixture
def setup_000(mocker):
    # mocker.patch("module.to.patchsleep")
    yield


def test_000_something(setup_000):
    pass
