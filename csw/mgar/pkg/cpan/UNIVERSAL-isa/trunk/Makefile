NAME = UNIVERSAL-isa
VERSION = 1.03
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = CHROMATIC

DESCRIPTION = Attempt to recover from people calling UNIVERSAL::isa as a function
define BLURB
  Whenever you use "isa" in UNIVERSAL as a function, a kitten using 
  Test::MockObject dies. Normally, the kittens would be helpless, but 
  if they use UNIVERSAL::isa (the module whose docs you are reading), 
  the kittens can live long and prosper.
  This module replaces UNIVERSAL::isa with a version that makes sure that, 
  when called as a function on objects which override isa, isa will 
  call the appropriate method on those objects
  In all other cases, the real UNIVERSAL::isa gets called directly.
endef

PACKAGES = CSWpmuniversalisa
CATALOGNAME = pm_universalisa

BUILD_DEP_PKGS = CSWpmmodulebuild

CONFIGURE_SCRIPTS = $(WORKSRC)/Build.PL
BUILD_SCRIPTS = $(WORKSRC)/Build
TEST_SCRIPTS = $(WORKSRC)/Build
INSTALL_SCRIPTS = $(WORKSRC)/Build

ARCHALL = 1

LICENSE = $(FILEDIR)/LICENSE

include gar/category.mk
