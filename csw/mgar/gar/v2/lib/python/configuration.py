# $Id$
# coding=utf-8

import ConfigParser
import errno
import logging
import os
import re
import sqlobject

WS_RE = re.compile(r"\s+")

CHECKPKG_DIR = "%(HOME)s/.checkpkg"
USER_CONFIG_FILE_TMPL = os.path.join(CHECKPKG_DIR, "checkpkg.ini")

CONFIGURATION_FILE_LOCATIONS = [
    (os.path.join(os.path.dirname(__file__), "checkpkg_defaults.ini"),
      True),
    ("/etc/opt/csw/checkpkg.ini", False),
    (USER_CONFIG_FILE_TMPL, False)
]


class Error(Exception):
  "Generic error."


class ConfigurationError(Error):
  "A problem with configuration."


def MkdirP(p):
  try:
    os.makedirs(p)
  except OSError as e:
    if e.errno == errno.EEXIST: pass
    else: raise


def GetConfig():
  config = ConfigParser.SafeConfigParser()
  file_was_found = False
  for file_name_tmpl, default in CONFIGURATION_FILE_LOCATIONS:
    filename = file_name_tmpl % os.environ
    if os.path.exists(filename):
      if not default:
        file_was_found = True
      config.read(file_name_tmpl % os.environ)
  if not file_was_found:
    db_file = "%(HOME)s/.checkpkg/checkpkg.db" % os.environ
    checkpkg_dir = CHECKPKG_DIR % os.environ
    MkdirP(checkpkg_dir)
    config_file = USER_CONFIG_FILE_TMPL % os.environ
    logging.warning(
        "No configuration file found.  Will attempt to create "
        "configuration in %s." % repr(config_file))
    if not config.has_section("database"):
      config.add_section("database")
    config.set("database", "type", "sqlite")
    config.set("database", "name", db_file)
    config.set("database", "host", "")
    config.set("database", "user", "")
    config.set("database", "password", "")
    config.set("database", "auto_manage", "yes")
    fd = open(config_file, "w")
    config.write(fd)
    fd.close()
    logging.debug("Configuration has been written.")
  if not config.has_section("database"):
    logging.fatal("Section 'database' not found in the config file. "
        "Please refer to the documentation: "
        "http://wiki.opencsw.org/checkpkg")
    raise SystemExit
  return config


def SetUpSqlobjectConnection():
  config = GetConfig()

  db_data = {
      'db_type': config.get("database", "type"),
      'db_name': config.get("database", "name"),
      'db_host': config.get("database", "host"),
      'db_user': config.get("database", "user"),
      'db_password': config.get("database", "password")}
  if db_data["db_type"] == "mysql":
    db_uri_tmpl = "%(db_type)s://%(db_user)s:%(db_password)s@%(db_host)s/%(db_name)s"
  elif db_data["db_type"] == "sqlite":
    db_uri_tmpl = "%(db_type)s://%(db_name)s"
  else:
    raise ConfigurationError(
        "Database type %s is not supported" % repr(db_data["db_type"]))
  db_uri = db_uri_tmpl % db_data
  sqo_conn = sqlobject.connectionForURI(db_uri)
  sqlobject.sqlhub.processConnection = sqo_conn
