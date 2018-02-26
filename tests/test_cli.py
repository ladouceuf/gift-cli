"""Tests for our main gift CLI module."""


from subprocess import PIPE, Popen as popen
from unittest import TestCase
import sys
sys.path.insert(0, 'gift')
from __init__ import __version__ as VERSION


class TestHelp(TestCase):
    def test_returns_usage_information(self):
        output = popen(['gift', '-h'], stdout=PIPE).communicate()[0]
        self.assertTrue('Usage:' in str(output))

        output = popen(['gift', '--help'], stdout=PIPE).communicate()[0]
        self.assertTrue('Usage:' in str(output))


class TestVersion(TestCase):
    def test_returns_version_information(self):
        process = popen(['gift', '--version'], stdout=PIPE)
        stdout = process.communicate()[0]
        print('STDOUT:{}'.format(stdout))
        self.assertTrue(str(stdout.strip())[2:6]==str(VERSION)[0:4])