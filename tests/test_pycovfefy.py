#!/usr/bin/env python
# -*- coding: utf-8 -*-


import pytest

from click.testing import CliRunner

from pycovfefy import pycovfefy
from pycovfefy import cli


@pytest.mark.parametrize("word,expected_covfefe", [
    ['coverage', 'covfefe']
])
def get_covfefe(word, expected_covfefe):
    assert pycovfefy.get_covfefe(word) == expected_covfefe


def test_command_line_interface():
    runner = CliRunner()
    result = runner.invoke(cli.main)
    assert result.exit_code == 0
    assert 'pycovfefy.cli.main' in result.output
    help_result = runner.invoke(cli.main, ['--help'])
    assert help_result.exit_code == 0
    assert '--help  Show this message and exit.' in help_result.output
