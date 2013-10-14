#!/opt/csw/bin/python -t -O

''' Compare two different catalog releases and show:
    - Which packages need rebuilding (so they don't depend on the _stub any more)
    - Which _stub packages can be removed
    - Which packages can declare incompatibility on the old packages, so that the old packages can be removed
    
    set PYTHONPATH=/path/to/.buildsys/v2
    alternatively can used: sys.path.append('/path/to/.buildsys/v2')

    ToDO:
    - read the sub hint from catalog
      * if stub has consumer -> rebuild
      * if stub has no consumer and the stub is present in the old/"from" catalog -> remove
      * if stub has no consumer and the stub does not yet present in the old/"from" catalog -> keep      
'''

import optparse
import pprint
import gdbm
import logging
import sys
import os
import subprocess
from collections import namedtuple
import re
import cjson

from lib.python import rest
from lib.python import common_constants
from lib.python import configuration
from lib.python.safe_remove_package import RevDeps

logging.basicConfig(format='%(asctime)s %(levelname)s:%(message)s')
logger = logging.getLogger(__name__)

oldcatrel = ''
newcatrel = ''
datadir=configuration.CHECKPKG_DIR % os.environ
# fn_revdep = os.path.join(datadir,'RevDeps_%s_%s_%s.json')
fn_cat = os.path.join(datadir,'catalog_%s_%s_%s.json')
fn_removelst = 'PkgsToRemoveFrom_%s_%s_%s.lst'
fn_rebuildlst = 'PkgsToRebuildFrom_%s_%s_%s.lst'
revdeplst = {}
    
CatSubSet = namedtuple('CatSubSet','catalogname md5_sum version dependlist')

class CompCatalog(object):

    def __init__(self,name,arch,osrel):
        self.rest_client = rest.RestClient()
        self.catrel = name
        self.arch = arch
        self.osrel = osrel
      
    def __getCat(self, name,arch,osrel):
        ''' get dependcy list from catalog, read cached list if available '''
        catlst = {}
        if os.path.exists(fn_cat % (name,osrel,arch)):
            logger.info('CompCatalog::getCat: use cached data: %s' % (fn_cat % (name,osrel,arch)))
            with open(fn_cat % (name,osrel,arch), "r") as fd:
                catlst = cjson.decode(fd.read())
        else:
            cat = self.rest_client.GetCatalog(name,arch,osrel)
            for pkg in cat:
                try:
                    pkgitems = self.rest_client.GetPkgstatsByMd5(pkg['md5_sum'])
                    pkgdeplst = [ i[0] for i in pkgitems['depends']]
                    catlst[pkgitems['basic_stats']['pkgname']] = CatSubSet(pkg['catalogname'],pkg['md5_sum'],pkg['version'],pkgdeplst)
                except Exception as inst:
                    logger.error("CompCatalog::getPkgStat: %s %s %s" , type(inst),pkg['catalogname'],pkg['md5_sum'])
            with open(fn_cat % (name,osrel,arch), "w") as fd:
                fd.write(cjson.encode(catlst))
                logger.info('CompCatalog::getCat: write cache file: %s' % (fn_cat % (name,osrel,arch)))
        return catlst
    
    def getCatalog(self):
        return self.__getCat(self.catrel,self.arch,self.osrel)

def processCat(catrel,arch,osrel):
    revdeplst = {}
    
    logger.info("processCat: -> %s %s %s" % (catrel, arch, osrel))
    cc = CompCatalog(catrel,arch,osrel)
    catlst = cc.getCatalog()
    logger.info("processCat: iterate on %s" % (catrel))
    
    ''' build reverse dependency list '''
    rd = RevDeps()
    for p in catlst.keys():
        revdeplst[p] = rd.RevDepsByPkg(catrel,arch,osrel,p)
    
    logger.info("processCat: <- %s %s %s" % (catrel, arch, osrel))
    return catlst, revdeplst
  
def main():
    parser = optparse.OptionParser()
    parser.add_option("--debug", dest="debug", action="store_true")
    parser.add_option("--verbose", dest="verbose", action="store_true")
    parser.add_option("--to-catalog-release", dest="newcatalog", default='kiel', 
                    help='set name of catalog to fetch', metavar = 'catalogname')
    parser.add_option("--from-catalog-release", dest="oldcatalog", default='dublin', 
                    help='set name of previous (older) catalog to fetch', metavar = 'old catalogname')
    parser.add_option("--os-arch", dest="arch", default='i386', 
                    help='set name of architecture (sparc|i386) to fetch', metavar = 'OS Architecture')
    parser.add_option("--os-release", dest="osrel", default='SunOS5.10', 
                    help='set os release to fetch (SunOS5.10|SunOS5.11)', metavar = 'OS Release')
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
    
    newcatlst, newrevdeplst = processCat(newcatrel,arch,osrel)
    oldcatlst, oldrevdeplst = processCat(oldcatrel,arch,osrel)
    
    to_remove_candidates = []
    rebuildlst = []
    logger.debug(' process dependecies in %s' % newcatrel)
    for p in newrevdeplst.keys():
        ''' check stub packages '''
        catalogname = CatSubSet(*newcatlst[p]).catalogname
        if catalogname.endswith("_stub"):
            if not newrevdeplst[p]:
                to_remove_candidates.append(p)
                logger.debug("{0}({1}) has no consumer".format(p,catalogname))
            else:
                for dp in newrevdeplst[p]:
                    dpkg = dp[1]
                    if dpkg not in rebuildlst and not CatSubSet(*newcatlst[dpkg]).catalogname.endswith("_stub"):
                          rebuildlst.append(dpkg)
                          logger.info(" REBUILD: {3}\n\t\t\tthese still use {0} ({1}) in {2}\n"
                                .format(p,CatSubSet(*newcatlst[p]).catalogname,newcatrel,
                                        [ dp[1] for dp in newrevdeplst[p]]))
    reallyremovelst = []
    logger.debug(' process dependecies in %s' % newcatrel)

    for p in to_remove_candidates:
        if p in oldrevdeplst: # this package is already a _stub in oldcatalog -> drop
            reallyremovelst.append(p)
            logger.info(" DROP   : %s from %s" % (p,newcatrel))
        else:
            logger.info(" KEEP   : {0} not a _stub package in {1}".format(p,oldcatrel))
    
    print ('write %s' % (fn_removelst % (newcatrel,osrel,arch))) 
    rmcnt = 0
    with open(fn_removelst % (newcatrel,osrel,arch), "w") as fd:
        for rp in reallyremovelst:
            fd.write(CatSubSet(*newcatlst[rp]).catalogname+'\n')
            rmcnt = rmcnt + 1
    logger.info("packages to remove: %d" % rmcnt)
    print ('write %s' % (fn_rebuildlst % (newcatrel,osrel,arch))) 
    rbcnt = 0
    with open(fn_rebuildlst % (newcatrel,osrel,arch), "w") as fd:
        for rp in rebuildlst:
            fd.write(CatSubSet(*newcatlst[rp]).catalogname+'\n')
            rbcnt = rbcnt + 1
    logger.info("packages to rebuild: %d" % rbcnt)


if __name__ == '__main__':
    main()
