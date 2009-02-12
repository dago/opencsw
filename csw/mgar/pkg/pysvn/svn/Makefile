GARNAME    = pysvn
GARVERSION = 1.6.2
CATEGORIES = utils

DESCRIPTION = Python Bindings for Subversion
define BLURB
	Bindings for Subversion, an opensource version control system.
endef

PACKAGES    = CSWpysvn
CATALOGNAME = py_svn
SPKG_DESC   = Python Bindings for Subversion

SPKG_SOURCEURL = http://pysvn.barrys-emacs.org/source_kits/
MASTER_SITES   = http://pysvn.tigris.org/
DISTFILES      = $(GARNAME)-$(GARVERSION).tar.gz

PATCHFILES = 

# We define upstream file regex so we can be notifed of 
# new upstream software release
UFILES_REGEX = (\d+(?:\.\d+)*)

#BUILD64    = 1
#NO_ISAEXEC = 0

CONFIGURE_ARGS  = $(DIRPATHS)

REQUIRED_PKGS_CSWpysvn  = 

TEST_TARGET = 

include gar/category.mk
