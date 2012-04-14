#!/opt/csw/bin/python

import sys
import os
import re
from optparse import OptionParser
from datetime import date
from datetime import timedelta

catalog = {};


# ---------------------------------------------------------------------------------------------------------------------
#
#
class CommandLineParser(object):
    """Command line parser. This class is a helper used to retrive options from command line
    """

    def __init__(self):
        # Create the option parser
        self.parser = OptionParser()

        # Add the different command line options to the parser
        self.parser.add_option("-c", "--catalog", help="Defines the catalog to parse. Default is ./catalog",
                                action="store", dest="catalog", type="string")
        self.parser.add_option("-1", "--tier1-list", help="List of tier 1 packages",
                                action="store", dest="tier1", type="string")
        self.parser.add_option("-2", "--tier2-list", help="List of tier 2 packages",
                                action="store", dest="tier2", type="string")
        self.parser.add_option("-3", "--tier3-list", help="List of tier 3 packages",
                                action="store", dest="tier3", type="string")
        self.parser.add_option("-V", "--verbose", help="Activate verbose mode", action="store_true", dest="verbose")

    def parse(self):
        (self.options, self.args) = self.parser.parse_args()
        return self.options, self.args

# ---------------------------------------------------------------------------------------------------------------------
#
#
class ConfigurationParser(object):
    """This class is a helper providing getter and setter on the option from command line
    """

    def __init__(self, args):

        if args.verbose != None:
            self.verbose = args.verbose
        else:
            self.verbose = False

        if args.catalog != None:
            self.catalog = args.catalog
        else:
            self.catalog = "./catalog"

        if args.tier1 != None:
            self.tier1 = args.tier1
        else:
            self.tier1 = "./tier1"

        if args.tier2 != None:
            self.tier2 = args.tier2
        else:
            self.tier2 = "./tier2"

        if args.tier3 != None:
            self.tier3 = args.tier3
        else:
            self.tier3 = "./tier3"

    # -----------------------------------------------------------------------------------------------------------------

    def getCatalog(self):
        return self.catalog

    def getTierInputFile(self, tier):
	if (tier == 1): 
	        return self.tier1

	if (tier == 2): 
        	return self.tier2

	if (tier == 3): 
	        return self.tier3

	return None

    def getTierOutputFile(self, tier):
	return "%(filename)s.out" % { 'filename' : self.getTierInputFile(tier) }

    def getVerbose(self):
        return self.verbose

# ---------------------------------------------------------------------------------------------------------------------
#
#
class Package:
	""" Defines a package. A package has a name (CSWfoo), a list of dependencies (same syntax as
	    catalog (CSWfoo|CSWbar) and a tier (1, 2, 3 or None if undefined)
	"""
	def __init__(self, name=None, version=None, depends=None):
		# Copy the name, depend lsit and tier
		self.name = name
		if (depends != "none"):
			self.depends = depends
		else:
			self.depends = None		

		# By default tier is set to 3. If the package is less than one year old, then it
		# will be promoted to tier 2 later. This is pretty crappy, but at this time there is
		# no way to be sure the catalog is fully parsed
		self.tier = 3
	
		# Compute the date. This information can be missing in some packages
		# Thus date is initialized to None. If it is possible to extract one from
		# revision string, then it will be set
		self.date = None

	        # Retrieve the date from the revision string, if it exists
                re_revisionString = re.compile(',REV=(?P<date>20\d\d\.\d\d\.\d\d)')
		d1 = re_revisionString.search(version)
		
		# Check if d1 is defined, if not, the regexp matched no revision string	
		if d1:	
			# Split the date to retrieve the year month day components
			d2 = d1.group('date').split('.')
			self.date = date(year=int(d2[0]) , month=int(d2[1]), day=int(d2[2]))
			
			# Compute the time elapsed between today and the update date
			delta = date.today() - self.date

			# If the delta between date is more than 365 days, then it has not been updated for a year
			# it goes to tier 3
			if delta.days > 365:
				self.tier = 3
			# Otherwise there is a quite recent update, it moves to tier 2
			else:
				self.tier = 2
		

	def setTier(self, tier):
		# Access to the global variable storing the catalog
		global catalog

		# Check if tier is lower or undefined, then we need to do something
		if self.tier >= tier :
			if self.tier > tier :
				print "%(pkg)s : %(t1)d => %(t2)d" % { 'pkg' : self.name , 't1' : self.tier , 't2' : tier }

			# Set the new tier value
			self.tier = tier
			
			# And iterate the list of dependencies to recursivly call the setTier method
			if (self.depends != None):
				for pkg in self.depends.split('|'):
					catalog[pkg].setTier(tier)
			
def main():

	global catalog
	outputFile = {}

	# Parse command line
	cliParser = CommandLineParser()
	(opts, args) = cliParser.parse()
        configParser = ConfigurationParser(opts)

	# Read catalog content
	for line in open(configParser.getCatalog(), 'r'):
		pkgInfo       = line.split(' ')	
		version       = pkgInfo[1]		
		name          = pkgInfo[2]		
		depends       = pkgInfo[6]
		catalog[name] = Package(name, version, depends)

	# Iterates the catalog once parsed to propagated tier values to depends
	for pkg in catalog:
		catalog[pkg].setTier(catalog[pkg].tier)
	
	for tier in (1 ,2 ,3):
		# Create the three files for outputing tier content
		outputFile[tier] = open(configParser.getTierOutputFile(tier), 'w') 

		# Check if the specific tier file exist
		if os.path.isfile(configParser.getTierInputFile(tier)):
			for line in open(configParser.getTierInputFile(tier) , 'r'):
				name = line.split('\n')	
				catalog[name[0]].setTier(tier)
		else:
			print "File %(filename)s does not exit. Skipping this file" %  { 'filename' : configParser.getTierInputFile(tier) }

	for pkg in catalog:
		outputFile[catalog[pkg].tier].write("%(name)s\n" % { 'name' : catalog[pkg].name })
		
	for tier in (1 ,2 ,3):
		outputFile[tier].close()

# On sort en rendant le code de retour de main
if __name__ == '__main__':
    sys.exit(main())
