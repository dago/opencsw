#!/usr/bin/env python2.6 -t

"""Helps to check if all needed libs are in the catalog.
writes all missings libs in a file missing_libs.txt in the format: libname:pkg:arch:osrel
"""

import optparse
import rest
import common_constants
import pprint
import gdbm
import logging
import sys
import os
import cjson
import subprocess
import makeStdLibDb

catrel = 'unstable'
cache_file_bins = 'bins-%s-%s-%s.json'
cache_file_links = 'links-%s-%s-%s.json'
cache_file_needed_bins = 'needed-bins-%s-%s-%s.json'
fn_stdlibs = 'stdlibs.json'
fn_report = 'missing_libs.txt'

class FindBins(object):

  def __init__(self):
    self.cached_catalogs_bins = {}
    self.cached_catalogs_links = {}
    self.cached_catalogs_needed_bins = {}
    self.rest_client = rest.RestClient()
    self.cp = rest.CachedPkgstats("pkgstats.db")

  def MakeRevIndex(self, catrel, arch, osrel):
    key = (catrel, arch, osrel)
    if key in self.cached_catalogs_bins:
      return
    fn_bins = cache_file_bins% key
    fn_links = cache_file_links% key
    fn_needed_bins = cache_file_needed_bins % key
    if os.path.exists(fn_bins) and os.path.exists(fn_needed_bins) and os.path.exists(fn_links):
      with open(fn_bins, "r") as fd:
        self.cached_catalogs_bins[key] = cjson.decode(fd.read())
      with open(fn_links, "r") as fd:
        self.cached_catalogs_links[key] = cjson.decode(fd.read())
      with open(fn_needed_bins, "r") as fd:
        self.cached_catalogs_needed_bins[key] = cjson.decode(fd.read())
      return
    catalog = self.rest_client.GetCatalog(*key)
    bins = {}
    links = {}
    needed_bins = {}
    i = 0
    for pkg_simple in catalog:
      i = i+1
      cb = []
      cl = []
      nb = []
      # pprint.pprint(pkg_simple)
      md5 = pkg_simple["md5_sum"]
      pkg = self.cp.GetPkgstats(md5)
      if not pkg:
        logging.warning("MakeRevIndex: No package for %r", md5)
        continue
      try:   
        pkg_name = pkg["basic_stats"]["pkgname"]
        for p in pkg['binaries_dump_info']:
          for b in p['needed sonames']:
            if b not in nb:
              nb.append(b)
        for b in pkg['binaries']:
            if b not in cb:
              cb.append(b)
            else:
              logging.debug("MakeRevIndex: %s already in cache")
        for pm in pkg['pkgmap']:
            if pm['type'] == 's': # symbolic link
              cl.append(pm['line'].split(' ')[3].split('=')[0]) # take the linkname
                
      except KeyError:
        logging.warning("MakeRevIndex: no pkg structure: ")
        # logging.warning(pkg)
      bins[pkg_name] = cb
      needed_bins[pkg_name] = nb
      links[pkg_name] = cl
      sys.stdout.write("\rMakeRevIndex:%4d %s" % (i,pkg_name))
      sys.stdout.flush()
    sys.stdout.write("\n")
    self.cached_catalogs_bins[key] = bins
    self.cached_catalogs_links[key] = links
    self.cached_catalogs_needed_bins[key] = needed_bins
    with open(fn_bins, "w") as fd:
      fd.write(cjson.encode(self.cached_catalogs_bins[key]))
    fd.close()
    with open(fn_links, "w") as fd:
      fd.write(cjson.encode(self.cached_catalogs_links[key]))
    fd.close()
    with open(fn_needed_bins, "w") as fd:
      fd.write(cjson.encode(self.cached_catalogs_needed_bins[key]))
    fd.close()

  def getBins(self, catrel, arch, osrel):
    self.MakeRevIndex(catrel, arch, osrel)
    key = (catrel, arch, osrel)
    return self.cached_catalogs_bins[key]

  def getLinks(self, catrel, arch, osrel):
    self.MakeRevIndex(catrel, arch, osrel)
    key = (catrel, arch, osrel)
    return self.cached_catalogs_links[key]

  def getNeededBins(self, catrel, arch, osrel):
    self.MakeRevIndex(catrel, arch, osrel)
    key = (catrel, arch, osrel)
    return self.cached_catalogs_needed_bins[key]

class PackageScanner(object):

  def scanPackage(self):
    # Get md5 sums
    rest_client = rest.RestClient()
    rd = FindBins()
    needed_bins = {}
    osrel_list = []
    with open(fn_stdlibs, "r") as fd:
        stdlibs = cjson.decode(fd.read())
    fl = open(fn_report, "w")
    for osrel in common_constants.OS_RELS:
      if osrel in common_constants.OBSOLETE_OS_RELS:
        logging.debug("scanPackage: %s is obsoleted" % osrel)
        continue
      for arch in common_constants.PHYSICAL_ARCHITECTURES:
        # get the list of binaries of a package
        bins = rd.getBins(catrel, arch, osrel)
        # get the list of libs which a package needs
        needed_bins = rd.getNeededBins(catrel, arch, osrel)
        # get the list of links in a package
        links = rd.getLinks(catrel, arch, osrel)
        i = 0
        checked = []
        for pkg in needed_bins:
          i = i+1
          for nb in needed_bins[pkg]:
            if nb in checked: continue
            checked.append(nb)
            found = False
            # at first search the lib in any other package
            for npkg in bins:
              for b in bins[npkg]:
                # if lib in the package
                if nb in b:
                  found = True
                  # logging.debug ("\nfound %s [%s]: %s in %s (%s)" % (osrel,pkg,nb,b,npkg))
                  break
              if found: break
            if not found:
                # second search is there a link with this name            
                for lpkg in links:
                  for l in links[lpkg]:
                    # if lib in the package
                    if nb in l:
                      found = True
                      # logging.debug ("\nfound %s [%s]: %s in %s (%s)" % (osrel,pkg,nb,b,npkg))
                      break
                  if found: break
            if not found:
                # third is the need lib a std solaris lib
                if nb in stdlibs:
                    found = True
                    # logging.debug ("\nfound %s" % nb)
            # at last search the lib in earlier os releases
            if not found: 
              fl.write("%s:%s:%s:%s\n" % (nb,pkg,arch,osrel) )
              print "\nNOT FOUND: %s, needed in pkg %s %s %s" % (nb,pkg,arch,osrel)
            sys.stdout.write("\rscanPackage %4d %s" % (i,pkg))
            sys.stdout.flush()
    fl.close()
 
def main():
  parser = optparse.OptionParser()
  parser.add_option("--debug", dest="debug", action="store_true")
  options, args = parser.parse_args()
  if options.debug:
    logging.basicConfig(level=logging.DEBUG)
  if not os.path.exists(fn_stdlibs):
    print "needed file %s not found, will create this" % fn_stdlibs
    makeStdLibDb.buildStdlibList()
  pr = PackageScanner()
  pr.scanPackage()
  print ""


if __name__ == '__main__':
  main()
