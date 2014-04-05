#!/opt/csw/bin/python -t -O
"""Compare two catalog releases and show:

- Which packages need rebuilding (so they don't depend on the _stub any more)
- Which _stub packages can be removed
- Which packages can declare incompatibility on the old packages, so that the
  old packages can be removed

set PYTHONPATH=/path/to/.buildsys/v2
alternatively can used: sys.path.append('/path/to/.buildsys/v2')

Overview:
- read the stub hint from catalog
  * if any packages depend on the stub -> rebuild them
  * if nothing depends on the stub and the stub is present in the old/"from"
    catalog -> remove
  * if nothing depends on the stub and the stub does not yet present in the
    old/"from" catalog -> keep

TODO:
- Group packages to rebuild by maintainer, and provide a per-maintainer report.
"""

import cjson
import jinja2
import logging
import optparse
import os
import sys

from collections import namedtuple

from lib.python import common_constants
from lib.python import configuration
from lib.python import rest
from lib.python.safe_remove_package import RevDeps

logging.basicConfig(format='%(levelname)s %(asctime)s %(filename)s:%(lineno)d %(message)s')
logger = logging.getLogger(__name__)

DATA_DIR = configuration.CHECKPKG_DIR % os.environ
CATALOG_CACHE_FILENAME_TMPL = os.path.join(DATA_DIR,'catalog_%s_%s_%s.json')

PKGS_TO_REMOVE_TMPL = 'PkgsToRemoveFrom_%s_%s_%s.lst'
PKGS_TO_REBUILD_TMPL = 'PkgsToRebuildFrom_%s_%s_%s.html'

CatSubSet = namedtuple('CatSubSet', ['pkgname', 'catalogname', 'md5_sum',
                                     'version', 'dependlist', 'maintainer'])

REBUILD_TMPL = """<html>
<head>
  <title>Packages to rebuild</title>
  <meta http-equiv="Content-type" content="text/html; charset=utf-8" />
  <style TYPE="text/css">
    body, p, li {
      font-size: 14px;
      font-family: sans-serif;
    }
    .obsolete, .obsolete a { color: brown; }
    .non-obsolete { color: #DDD; }
  </style>
</head>
<body>
  <h1>Packages to rebuild</h1>
  <p>Packages displayed in brown are empty, obsolete packages. The packages on
  the list are the packages which need to be rebuilt with their dependencies
  modified to not include the obsolete packages any more.</p>
  <ul>
  {% for pkg in pkgs %}
    <li>
      {{ pkg.maintainer }}
      <a href="http://buildfarm.opencsw.org/pkgdb/srv4/{{ pkg.md5_sum }}/"
        >{{ pkg.catalogname }}</a>
      {% for dep in pkg.dependlist %}
        {% if dep in obsolete %}
          <span class="obsolete">
          <a href="http://buildfarm.opencsw.org/pkgdb/srv4/{{ obsolete[dep].md5_sum }}/"
             title="{{ dep }} is obsolete; {{ pkg.pkgname }} needs to be rebuilt with {{ dep }} removed from RUNTIME_DEP_PKGS"
          >{{ dep }}</a>
          </span>
        {% endif %}
      {% endfor %}
    </li>
  {% endfor %}
  </ul>
</body>
</html>
"""


class CompCatalog(object):
  def __init__(self, name, arch, osrel, rest_client):
    self.catrel = name
    self.arch = arch
    self.osrel = osrel
    self.rest_client = rest_client
    self.cached_stats = rest.CachedPkgstats(
        os.path.join(DATA_DIR, 'pkgstats'), rest_client)

  def CatSubSetFromFull(self, pkgitems):
    """Returns a CatSubSet from full package stats."""
    pkgname = pkgitems['basic_stats']['pkgname']
    pkgdeplst = [i[0] for i in pkgitems['depends']]
    maintainer = pkgitems['pkginfo']['EMAIL'].split('@')[0]
    return CatSubSet(pkgname,
                     pkgitems['basic_stats']['catalogname'],
                     pkgitems['basic_stats']['md5_sum'],
                     pkgitems['basic_stats']['parsed_basename']['full_version_string'],
                     tuple(pkgdeplst),
                     maintainer)

  def __getCat(self, catrel, arch, osrel):
    """Get dependcy list from the database."""
    logging.info('__getCat(%s, %s, %s)' % (catrel, arch, osrel))
    pkg_by_pkgname = {}
    cat = self.rest_client.GetCatalog(catrel, arch, osrel)
    for pkg in cat:
      pkgitems = self.rest_client.GetPkgstatsByMd5(pkg['md5_sum'])
      catsubset = self.CatSubSetFromFull(pkgitems)
      pkg_by_pkgname[catsubset.pkgname] = catsubset
    return pkg_by_pkgname

  def getCatalog(self):
    return self.__getCat(self.catrel, self.arch, self.osrel)


def processCat(catrel, arch, osrel, rest_client):
    logger.info("processCat: -> %r %r %r" % (catrel, arch, osrel))

    cc = CompCatalog(catrel, arch, osrel, rest_client)
    pkg_by_pkgname = cc.getCatalog()
    logger.info("processCat: iterate on %r" % (catrel))

    # build reverse dependency list
    rev_deps_access = RevDeps(rest_client)
    rev_deps_by_pkg = {}
    for pkgname in pkg_by_pkgname:
        pkg = pkg_by_pkgname[pkgname]
        # RevDepsByPkg returns only md5 sums and pkgnames, so we need to map
        # them back to CatSubSet
        revdeps = rev_deps_access.RevDepsByPkg(catrel, arch, osrel, pkgname)
        # rev_deps_by_pkg[pkg] = [pkg_by_pkgname[pkgname] for _, pkgname in revdeps]
        revdep_pkgs = []
        for _, pkgname in revdeps:
          revdep_pkg = pkg_by_pkgname[pkgname]
          revdep_pkgs.append(revdep_pkg)
        try:
          rev_deps_by_pkg[pkg] = revdep_pkgs
        except TypeError as exc:
          logging.fatal('pkg: %r', pkg)
          raise

    logger.info("processCat: <- %r %r %r" % (catrel, arch, osrel))
    return pkg_by_pkgname, rev_deps_by_pkg


def ComputeRemoveAndRebuild(oldcatrel, newcatrel, arch, osrel, rest_client):
    newcatlst, newrevdeplst = processCat(newcatrel, arch, osrel, rest_client)
    oldcatlst, oldrevdeplst = processCat(oldcatrel, arch, osrel, rest_client)

    obsolete_pkgs_by_pkgname = {}
    to_remove_candidates = []
    rebuildlst = set()
    logger.debug(' process dependecies in %s' % newcatrel)
    for pkg in newrevdeplst:
        # Checking stub packages
        catalogname = pkg.catalogname
        if catalogname.endswith("_stub"):
            obsolete_pkgs_by_pkgname[pkg.pkgname] = pkg
            if not newrevdeplst[pkg]:
                # Stub has no reverse dependencies, so it will be considered for removal.
                to_remove_candidates.append(pkg)
                logger.debug("{0}({1}) has no consumer".format(pkg.pkgname, catalogname))
            else:
                # Reverse dependencies of this stub need to be rebuilt.
                for new_rev_dep in newrevdeplst[pkg]:
                    is_newpkg_stub = new_rev_dep.catalogname.endswith("_stub")
                    if new_rev_dep not in rebuildlst and not is_newpkg_stub:
                          rebuildlst.add(new_rev_dep)
                          logger.info(" REBUILD: {3}, it still depends on {0} ({1}) in {2}"
                                .format(pkg.pkgname, pkg.catalogname, newcatrel,
                                  '%s/%s' % (new_rev_dep.pkgname, new_rev_dep.catalogname)))
    pkgs_to_drop = []
    logger.debug(' process dependecies in %s' % newcatrel)

    for pkg in to_remove_candidates:
        if pkg in oldrevdeplst:
            # this package is already a _stub in the old catalog,
            # and therefore can be dropped
            pkgs_to_drop.append(pkg)
            logger.info(" DROP   : {0}/{1} from {2}"
                        .format(pkg.pkgname, pkg.catalogname, newcatrel))
        else:
            logger.info(" KEEP   : {0} not a _stub package in {1}"
                        .format(pkg.pkgname, oldcatrel))
    return pkgs_to_drop, rebuildlst, obsolete_pkgs_by_pkgname


def WriteToTextFiles(pkgs_to_drop, pkgs_to_rebuild, newcatrel, arch, osrel,
                     obsolete):
    print ('writing %s' % (PKGS_TO_REMOVE_TMPL % (newcatrel,osrel,arch)))
    with open(PKGS_TO_REMOVE_TMPL % (newcatrel, osrel, arch), "w") as fd:
        for pkg in sorted(pkgs_to_drop, key=lambda p: p.catalogname):
            fd.write(pkg.catalogname + '\n')
    logger.info("number of packages to remove: %d" % len(pkgs_to_drop))
    print ('write %s' % (PKGS_TO_REBUILD_TMPL % (newcatrel,osrel,arch)))
    with open(PKGS_TO_REBUILD_TMPL % (newcatrel,osrel,arch), "w") as fd:
        template = jinja2.Template(REBUILD_TMPL)
        pkgs = sorted(pkgs_to_rebuild, key=lambda p: (p.maintainer, p.catalogname))
        fd.write(template.render(catrel=newcatrel, osrel=osrel, arch=arch,
                                 pkgs=pkgs, obsolete=obsolete))
    logger.info("# of packages to rebuild: %d" % len(pkgs_to_rebuild))


def GetCLIOptions():
    parser = optparse.OptionParser()
    parser.add_option("--debug", dest="debug", action="store_true")
    parser.add_option("--verbose", dest="verbose", action="store_true")
    parser.add_option("--to-catalog-release", dest="newcatalog", default='unstable',
                    help='set name of catalog to fetch', metavar = 'catalogname')
    parser.add_option("--from-catalog-release", dest="oldcatalog", default='kiel',
                    help='set name of previous (older) catalog to fetch',
                    metavar = 'old catalogname')
    parser.add_option("--os-arch", dest="arch", default='i386',
                    help='set name of architecture (sparc|i386) to fetch',
                    metavar = 'OS Architecture')
    parser.add_option("--os-release", dest="osrel", default='SunOS5.10',
                    help='set os release to fetch (SunOS5.10|SunOS5.11)',
                    metavar = 'OS Release')
    options, args = parser.parse_args()
    opterror = False
    if options.verbose:
        logger.setLevel(logging.INFO)
    if options.debug:
        logger.setLevel(logging.DEBUG)
    if options.newcatalog in common_constants.DEFAULT_CATALOG_RELEASES:
        newcatrel = options.newcatalog
    else:
        logger.error('unknown catalog: %s',options.newcatalog)
        opterror = True
    if options.oldcatalog in common_constants.DEFAULT_CATALOG_RELEASES:
        oldcatrel = options.oldcatalog
    else:
        logger.error('unknown catalog: %s',options.newcatalog)
        opterror = True
    if options.arch in common_constants.PHYSICAL_ARCHITECTURES:
        arch      = options.arch
    else:
        logger.error('unknown architecture: %s',options.arch)
        opterror = True
    if options.osrel in common_constants.OS_RELS:
        osrel     = options.osrel
    else:
        logger.error('unknown OS Release: %s',options.osrel)
        opterror = True
    if opterror:
        sys.exit(1)
    return oldcatrel, newcatrel, arch, osrel


def main():
    oldcatrel, newcatrel, arch, osrel = GetCLIOptions()

    config = configuration.GetConfig()
    username, password = rest.GetUsernameAndPassword()
    rest_client = rest.RestClient(
        pkgdb_url=config.get('rest', 'pkgdb'),
        releases_url=config.get('rest', 'releases'),
        username=username,
        password=password)

    removelst, rebuildlst, obsolete = (
        ComputeRemoveAndRebuild(oldcatrel, newcatrel, arch, osrel,
                                rest_client))
    WriteToTextFiles(removelst, rebuildlst, newcatrel, arch, osrel, obsolete)


if __name__ == '__main__':
    main()
