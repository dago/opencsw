#!/opt/csw/bin/python

import cjson
import logging
import argparse
import urllib2
import sys
import re

logging.basicConfig(format='%(asctime)s %(levelname)s:%(message)s')
logger = logging.getLogger(__name__)

remote_scheme = ['http','https']
local_scheme = ['file']

def prepareCatListFromURI(uri):
    catlst = []
    if '://' in uri:
        scheme = uri.split(':')[0]
        if scheme in remote_scheme:
            logger.info("fetch remote %s", uri)
            data = urllib2.urlopen(uri).read()
            catlst = cjson.decode(data)
            for e in catlst:
                del e[9]
            return catlst
        elif scheme in local_scheme:
            uri = re.sub('.*://','',uri)
        else:
            logger.error('unsupported URI format')
            sys.exit(4)
    with open(uri) as lcat:
        logger.info("fetch local %s", uri)
        for line in lcat: # skip 4 lines header '# CREATIONDATE'
            if line.startswith("# CREATIONDATE"): 
                break
        for line in lcat:
            if line.startswith("-----BEGIN PGP SIGNATURE"): 
                break
            catlst.append(line.rstrip().split(' '))
    return catlst
            
def compareOutOfOrder(a_catlst, b_catlst, idx):
    a_pkgName2Idx = {}
    i = idx 
    for j in range(idx,len(a_catlst)):
        a_pkgName2Idx[a_catlst[j][0]] = j
    # import pdb; pdb.set_trace()
    while i < len(b_catlst):
        if b_catlst[i][0] in a_pkgName2Idx:
            if b_catlst[i] != a_catlst[a_pkgName2Idx[b_catlst[i][0]]]:
                logger.warning("pkgs different at {0},{1}: {2} {3}".format(i,a_pkgName2Idx[b_catlst[i][0]],a_catlst[a_pkgName2Idx[b_catlst[i][0]]],b_catlst[i]))
                sys.exit(1)
        else:
            logger.warning("not in acat: %s", b_catlst[i])
            sys.exit(1)
        i += 1 
    b_pkgName2Idx = {}
    for j in range(idx,len(b_catlst)):
        b_pkgName2Idx[b_catlst[j][0]] = j
    # import pdb; pdb.set_trace()
    i = idx
    while i < len(a_catlst):
        if a_catlst[i][0] not in b_pkgName2Idx:
            logger.warning("not in bcat: %s", a_catlst[i])
            sys.exit(1)
        i += 1 
        
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
    if len(a_catlst) != len(b_catlst):
        logger.warning("a has %d, b has %d packages",len(a_catlst),len(b_catlst))
        # sys.exit(1)
    for i in range(len(b_catlst)):
        try:
            if b_catlst[i] != a_catlst[i] :
                if b_catlst[i][0] != a_catlst[i][0]: 
                    logger.warning("packages out of order: A: %s; B: %s",a_catlst[i][0], b_catlst[i][0])
                    compareOutOfOrder(a_catlst, b_catlst, i)
                    break
                else:
                    logger.warning("pkgs different: {0} {1}".format(a_catlst[i],b_catlst[i]))
                    sys.exit(1)
        except IndexError as e:
            logger.info("package %s not in acat", b_catlst[i])
            
    # import pdb; pdb.set_trace()
    logger.info("catalogs are same")
    sys.exit(0)


if __name__ == '__main__':
    main()
