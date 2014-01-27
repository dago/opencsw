#!/opt/csw/bin/python

import cjson
import logging
import optparse
import urllib2
import sys

logging.basicConfig(format='%(asctime)s %(levelname)s:%(message)s')
logger = logging.getLogger(__name__)

def main():
    parser = optparse.OptionParser()
    parser.add_option("-v","--verbose", dest="verbose", action="store_true",default=False)
    parser.add_option("-a","--existing-catalog", dest="oldcatalog", 
                    help='set URI of existing catalog', metavar = 'catalog')
    parser.add_option("-b","--new-catalog", dest="newcatalog", 
                    help='set URI of catalog to generate', metavar = 'catalog')
    options, args = parser.parse_args()
    opterror = False
    if options.verbose:
        logger.setLevel(logging.INFO)
    if options.debug:
        logger.setLevel(logging.DEBUG)
    if options.newcatalog is None or options.oldcatalog is None:
        logger.error("mandatory option missing")
        sys.exit(2)
    oldcat = options.oldcatalog
    newcat = options.newcatalog
    logger.info(" compare %s with %s", oldcat, newcat)

    data = urllib2.urlopen(oldcat).read()
    a_catlst = cjson.decode(data)
    for e in a_catlst:
        del e[9]
    b_catlst = []
    with open(newcat) as nc:
        for i in range(4): # skip 4 lines header
            nc.readline()
        for cl in nc.readlines():
            if "-----BEGIN" == cl.split(' ')[0]:
                break
            b_catlst.append(cl.rstrip().split(' '))
    if len(a_catlst) != len(b_catlst):
        logger.warning("a has %d, b has %d packges",len(a_catlst),len(b_catlst))
        sys.exit(1)
    for i in range(len(b_catlst)):
        if b_catlst[i] != a_catlst[i] :
            logger.warning("a is {0}, b is {1}".format(a_catlst[i],b_catlst[i]))
            sys.exit(1)
            
    # import pdb; pdb.set_trace()
    logger.debug("catalogs are same")
    sys.exit(0)


if __name__ == '__main__':
    main()
