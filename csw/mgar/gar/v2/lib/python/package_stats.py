#!/usr/bin/env python2.6

import cjson
import copy
import dateutil.parser
import itertools
import logging
import mute_progressbar
import os
import pprint
import progressbar
import progressbar.widgets
import re
import sqlobject
import subprocess
import sys
from sqlobject import sqlbuilder

from lib.python import catalog
from lib.python import configuration
from lib.python import database
from lib.python import errors
from lib.python import models
from lib.python import opencsw
from lib.python import overrides
from lib.python import rest
from lib.python import sharedlib_utils
from lib.python import shell
from lib.python import tag


class PackageError(errors.Error):
  """Problem with the package file examined."""


class PackageStats(object):
  """Collects stats about a package and saves them.

  Takes care of processing data from a SVR4 package and returing them as data structures.
  """

  def __init__(self, srv4_pkg, stats_basedir=None, md5sum=None, debug=False):
    super(PackageStats, self).__init__()
    self.srv4_pkg = srv4_pkg
    self.md5sum = md5sum
    self.dir_format_pkg = None
    self.all_stats = {}
    self.db_pkg_stats = None
    config = configuration.GetConfig()
    self.rest_client = rest.RestClient(
        pkgdb_url=config.get('rest', 'pkgdb'),
        releases_url=config.get('rest', 'releases'))

  def __unicode__(self):
    return (u"<PackageStats srv4_pkg=%s md5sum=%s>"
            % (self.srv4_pkg, self.md5sum))

  def GetDbObject(self):
    if not self.db_pkg_stats:
      md5_sum = self.GetMd5sum()
      logging.debug(u"GetDbObject(): %s md5sum: %s", self, md5_sum)
      res = models.Srv4FileStats.select(models.Srv4FileStats.q.md5_sum==md5_sum)
      try:
        self.db_pkg_stats = res.getOne()
      except sqlobject.SQLObjectNotFound as e:
        logging.debug(u"GetDbObject(): %s not found", md5_sum)
        return None
      logging.debug(u"GetDbObject(): %s succeeded", md5_sum)
    return self.db_pkg_stats

  def GetAllStats(self):
    if not self.all_stats and self.StatsExist():
      self.all_stats = self.ReadSavedStats()
    elif not self.all_stats:
      self.all_stats = self.CollectStats()
    return self.all_stats

  def GetSavedOverrides(self):
    if not self.StatsExist():
      raise PackageError("Package stats not ready.")
    pkg_stats = self.GetDbObject()
    res = models.CheckpkgOverride.select(models.CheckpkgOverride.q.srv4_file==pkg_stats)
    override_list = []
    for db_override in res:
      d = {
          'pkgname': db_override.pkgname,
          'tag_name': db_override.tag_name,
          'tag_info': db_override.tag_info,
      }
      override_list.append(overrides.Override(**d))
    return override_list

  def GetSavedErrorTags(self):
    pkg_stats = self.GetDbObject()
    res = models.CheckpkgErrorTag.select(models.CheckpkgErrorTag.q.srv4_file==pkg_stats)
    tag_list = [tag.CheckpkgTag(x.pkgname, x.tag_name, x.tag_info, x.msg)
                for x in res]
    return tag_list

  def ReadSavedStats(self):
    return self.rest_client.GetBlob('pkgstats', self.GetMd5sum())


class StatsCollector(object):
  """Takes a list of files and makes sure they're put in a database."""

  def __init__(self, logger=None, debug=False):
    if logger:
      self.logger = logger
    else:
      self.logger = logging
    self.debug = debug
    self.config = configuration.GetConfig()
    self.rest_client = rest.RestClient(
        pkgdb_url=self.config.get('rest', 'pkgdb'),
        releases_url=self.config.get('rest', 'releases'))

  def CollectStatsFromCatalogEntries(self, catalog_entries, force_unpack=False):
    """Returns: A list of md5 sums of collected statistics."""
    args_display = [x['file_basename'] for x in catalog_entries]
    if len(args_display) > 5:
      args_display = args_display[:5] + ["...more..."]
    self.logger.debug("Processing: %s, please be patient", args_display)
    md5_sum_list = []
    # Reversing the item order in the list, so that the pop() method can be used
    # to get packages, and the order of processing still matches the one in the
    # catalog file.
    total_packages = len(catalog_entries)
    if not total_packages:
      raise PackageError("The length of package list is zero.")
    counter = itertools.count(1)
    self.logger.info("Juicing the svr4 package stream files...")
    if self.debug:
      pbar = mute_progressbar.MuteProgressBar()
    else:
      pbar = progressbar.ProgressBar(widgets=[
        progressbar.widgets.Percentage(),
        ' ',
        progressbar.widgets.ETA(),
        ' ',
        progressbar.widgets.Bar()
      ])
      pbar.maxval = total_packages
      pbar.start()
    base_dir, _ = os.path.split(__file__)
    collect_pkg_metadata = os.path.join(base_dir, "collect_pkg_metadata.py")
    for catalog_entry in catalog_entries:
      pkg_file_name = catalog_entry['pkg_path']
      args = [collect_pkg_metadata]
      stderr_file = subprocess.PIPE
      if self.debug:
        args.append('--debug')
        stderr_file = None
      if force_unpack:
        args += ['--force-unpack']
      args += ['--input', pkg_file_name]
      ret_code, stdout, stderr = shell.ShellCommand(args, allow_error=False,
                                                    stderr=stderr_file)
      try:
        data_back = cjson.decode(stdout)
        if data_back['md5_sum'] != catalog_entry['md5sum']:
          msg = ('Unexpected file content: catalog said '
                 'that %r would have MD5 sum %r but it '
                 'turned out to be %r when read from allpkgs. '
                 'We cannot continue, because we have no '
                 'access to the data we are asked to examine.'
                 % (catalog_entry['file_basename'],
                    catalog_entry['md5sum'],
                    data_back['md5_sum']))
          raise PackageError(msg)
        md5_sum_list.append(data_back['md5_sum'])
      except cjson.DecodeError:
        logging.fatal('Could not deserialize %r', stdout)
        raise
      pbar.update(counter.next())
    pbar.finish()
    return md5_sum_list
