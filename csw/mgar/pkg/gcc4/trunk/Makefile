GARNAME = gcc
GARVERSION = 4.3.3
CATEGORIES = lang

DESCRIPTION = The GNU Compiler Collection
define BLURB
	The GNU Compiler Collection includes front ends for C, C++, 
	Objective-C, Fortran, Java, and Ada, as well as libraries 
	for these languages (libstdc++, libgcj,...).
endef

DISTFILES  = $(GARNAME)-$(GARVERSION).tar.bz2

MASTER_SITES = http://gcc.gnu.org/
SPKG_SOURCEURL = http://gcc.releasenotes.org/releases/

# We define upstream file regex so we can be notifed 
# of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.bz2

###  Scripts Section  ###

## Directory to do all the work from
OBJECT_DIR = $(WORKDIR)/$(DISTNAME)/objdir
## Change default $(WORKSRC) to the $(OBJECT_DIR)
WORKSRC = $(OBJECT_DIR)

## After sucessful source extraction
## Create $(OBJECT_DIR) to build in
post-extract-modulated:
	echo "==> Creating Object Dir for Building"
	@( mkdir $(OBJECT_DIR) )
	$(DONADA)

## Override standard configure
CONFIGURE_SCRIPTS = objdir
## instead of changing to $(WORKSRC) and running configure
## Run it from the $(OBJECT_DIR)
configure-objdir:
	echo "==> Running Configure from $(OBJECT_DIR)"
	cd $(OBJECT_DIR) && $(CONFIGURE_ENV) ../configure $(CONFIGURE_ARGS)
	$(DONADA)

## Package Check will fail for self dependencies
## i.e. CSWgcc4core is dependent on CSWgcc4corert
## if CSWgcc4corert is not installed on the build system
## Package Creation will fail and the remaining packages
## will not get created.  
##      ******  Run checkpkg Manually  *****
ENABLE_CHECK = 0

## Tests take a very long time
TEST_SCRIPTS = skip

test-skip:
	$(DONADA)

## For cleanliness I moved the Configuration Definition
## And Packaging Definitions to their own file
include files/configure_def.mk  
include files/package_def.mk

include gar/category.mk
