#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by Jon Surrell,,,
# Copyright (c) 2014 Jon Surrell,,,
#
# License: MIT
#

"""This module exports the Go plugin class."""

from SublimeLinter.lint import Linter, util
from os import devnull as DEVNULL


class Go(Linter):

    """Provides an interface to go build."""

    syntax = 'go'
    cmd = ('go', 'build', '-o', DEVNULL)
    regex = r'^.+:(?P<line>\d+):\s+(?P<message>.+)$'
    tempfile_suffix = 'go'
    error_stream = util.STREAM_STDERR
    selectors = {}
    word_re = None
    defaults = {}
    inline_settings = None
    inline_overrides = None
    comment_re = None
