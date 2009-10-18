GARNAME = cgit
GARVERSION = 0.8.3_opencsw_1
CATEGORIES = devel

DESCRIPTION = Web front-end for Git
define BLURB
cgit is 
 * a cgi application implemented in C: it's basically (yet) another git command, used to generate html.
 * not forking: all git operations are performed by linking with libgit.a.
 * using a built-in cache: the generated html is stored on disk for the benefit of later requests.
 * fond of virtual urls - using PATH_INFO or modules like mod_rewrite makes cgit generate urls with few or no querystring parameters, e.g.
 * http://hjemli.net/git/cgit/log/Makefile vs.
 * http://hjemli.net/git?r=cgit&p=log&path=Makefile.
 * not too visual, but sometimes a bit of graphics can be justified.
 * open source - it is licensed under GPL v2.
 * maintained by Lars Hjemli, who is happy to receive patches, suggestions and bug reports.
endef

REQUIRED_PKGS_CSWcgit = CSWiconv CSWosslrt CSWzlib

#MASTER_SITES = http://hjemli.net/git/cgit/snapshot/
#DISTFILES = $(GARNAME)-$(GARVERSION).tar.gz

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

#GIT_REPOS  = git://github.com/trygvis/cgit.git
GIT_REPOS  = http://localhost/cgit/cgit
#GIT_TREEISH_cgit = v$(GARVERSION)$(if $(PATCHLEVEL),-$(PATCHLEVEL))
GIT_TREEISH_cgit = solaris

DISTFILES = apache.conf.CSW cgitrc.CSW

# The Makefile use "install" to install files but the Sun one is not really compatible
PATH := /usr/ucb:$(PATH)

# If the url used to check for software update is different of MASTER_SITES, then 
# uncomment the next line. Otherwise it is set by default to the value of MASTER_SITES
# UPSTREAM_MASTER_SITES = 

PATCHFILES  = 0001-cgit.conf
PATCHFILES += 8071e18dcbf56b98ecea4332e85884cdd91236cc-d8eb68d5d487014a16b680e7d52122d3415303da.diff

CONFIGURE_SCRIPTS = 

# Disable tests for now, need a round GNU'ism removal there too
TEST_SCRIPTS =

PRESERVECONF  = /etc/opt/csw/cgit/apache.conf.CSW
PRESERVECONF += /etc/opt/csw/cgit/cgitrc.CSW

# Trick to get the gar+git support to export the source code
pre-extract-modulated: git-extract-cgit

post-install-modulated:
	@mkdir -p $(DESTDIR)/etc/opt/csw/cgit/
	@cp $(FILEDIR)/apache.conf.CSW \
		$(FILEDIR)/cgitrc.CSW \
		$(DESTDIR)/etc/opt/csw/cgit/
#	@$(MAKECOOKIE)

include gar/category.mk
