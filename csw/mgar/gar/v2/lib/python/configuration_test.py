#!/usr/bin/env python2.6

import ConfigParser
import unittest

from lib.python import configuration

class ConfigUnitTest(unittest.TestCase):

  def testComposeURI1(self):
    config = ConfigParser.SafeConfigParser(configuration.CONFIG_DEFAULTS)
    config.add_section('database')
    config.set('database', 'type', 'sqlite')
    config.set('database', 'name', ':memory:')
    self.assertEqual(
        'sqlite:/:memory:?cache=false&debug=false&debugDisplay=false',
        configuration.ComposeDatabaseUri(config))

  def testComposeUriDebug(self):
    config = ConfigParser.SafeConfigParser(configuration.CONFIG_DEFAULTS)
    config.add_section('database')
    config.set('database', 'type', 'sqlite')
    config.set('database', 'name', ':memory:')
    config.set('database', 'debug', 'true')
    config.set('database', 'debugDisplay', 'true')
    self.assertEqual(
        'sqlite:/:memory:?cache=false&debug=true&debugDisplay=true',
        configuration.ComposeDatabaseUri(config))

  def testComposeUriDebugMysql(self):
    config = ConfigParser.SafeConfigParser(configuration.CONFIG_DEFAULTS)
    config.add_section('database')
    config.set('database', 'type', 'mysql')
    config.set('database', 'name', 'checkpkg')
    config.set('database', 'host', 'localhost')
    config.set('database', 'user', 'checkpkg_user')
    config.set('database', 'password', 'secret')
    config.set('database', 'debug', 'true')
    config.set('database', 'cache', 'true')
    self.assertEqual(
        'mysql://checkpkg_user:secret@localhost/checkpkg?cache=true',
        configuration.ComposeDatabaseUri(config))


if __name__ == '__main__':
  unittest.main()
