NAME = UNIVERSAL-can
VERSION = 1.16
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = CHROMATIC

DESCRIPTION = Hack around people calling UNIVERSAL::can() as a function
define BLURB
  The UNIVERSAL class provides a few default methods so that all objects 
  can use them. Object orientation allows programmers to override these 
  methods in subclasses to provide more specific and appropriate behavior.
  Some authors call methods in the UNIVERSAL class on potential invocants 
  as functions, bypassing any possible overriding. This is wrong and you 
  should not do it. Unfortunately, not everyone heeds this warning and 
  their bad code can break your good code.
endef

PACKAGES = CSWpmuniversalcan
CATALOGNAME = pm_universalcan

CONFIGURE_SCRIPTS = $(WORKSRC)/Build.PL
BUILD_SCRIPTS = $(WORKSRC)/Build
TEST_SCRIPTS = $(WORKSRC)/Build
INSTALL_SCRIPTS = $(WORKSRC)/Build

LICENSE = $(FILEDIR)/LICENSE

ARCHALL = 1

include gar/category.mk
