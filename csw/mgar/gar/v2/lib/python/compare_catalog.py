#!/opt/csw/bin/python

import cjson
import logging
import argparse
import urllib2
import sys
import re
from lib.python import catalog

logging.basicConfig(format='%(asctime)s %(levelname)s:%(message)s')
logger = logging.getLogger(__name__)

remote_scheme = ['http','https']
local_scheme = ['file']
catalog_keys = ['catalogname','version','pkgname','file_basename',
                    'md5sum','size','deps','category','i_deps']

def xxxSplitPkgList(pkglist):
    if not pkglist:
        pkglist = ()
    elif pkglist == "none":
        pkglist = ()
    else:
       pkglist = tuple(pkglist.split("|"))
    return pkglist

def convToDict(catlst):
    catdict = []
    for entry in catlst:
        del entry[9]
	entry[6] = catalog.SplitPkgList(entry[6])
	entry[8] = catalog.SplitPkgList(entry[8])
        catdict.append(dict(zip(catalog_keys,entry)))
    return catdict

def prepareCatListFromURI(uri):
    catlst = []
    if '://' in uri:
        scheme = uri.split(':')[0]
        if scheme in remote_scheme:
            logger.info("fetch remote %s", uri)
            data = urllib2.urlopen(uri).read()
            return convToDict(cjson.decode(data))
        elif scheme in local_scheme:
            uri = re.sub('.*://','',uri)
        else:
            logger.error('unsupported URI format')
            sys.exit(4)
    return catalog.OpencswCatalog(open(uri)).GetCatalogData()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-v","--verbose", dest="verbose", action="store_true",default=False)
    parser.add_argument("acat",help="catalog URI")
    parser.add_argument("bcat",help="catalog URI")
    args = parser.parse_args()
    opterror = False
    if args.verbose:
        logger.setLevel(logging.INFO)
    if args.acat is None or args.bcat is None:
        logger.error("mandatory args 'acat' 'bcat' missing")
        sys.exit(2)

    logger.info("fetch cat_a %s", args.acat)
    a_catlst = prepareCatListFromURI(args.acat)
    
    logger.info("fetch cat_b %s", args.bcat)
    b_catlst = prepareCatListFromURI(args.bcat)

    logger.info("compare ...")
    if a_catlst == b_catlst:
        logger.info("catalogs are same")
        sys.exit(0)
    else:
        for i in range(len(a_catlst)):
	    for k in catalog_keys:
                if a_catlst[i][k] != b_catlst[i][k]:
                    logger.warning("catalogs are different; package index:%d, kex: %s", i, k);
        sys.exit(1)

if __name__ == '__main__':
    main()
