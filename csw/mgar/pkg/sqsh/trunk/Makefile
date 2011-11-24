NAME = sqsh
VERSION = 2.1.7
CATEGORIES = utils

PACKAGING_PLATFORMS = solaris10-sparc solaris10-i386

# Hardwired to skip the tests
ifeq ($(VERSION),2.1.7)
#TEST_TARGET = check
TEST_SCRIPTS = 
endif

DESCRIPTION = powerful SQL shell with advanced scripting ability for Sybase
define BLURB
  Sqsh (pronounced skwish) is short for SQshelL (pronounced s-q-shell), 
  it is intended as a replacement for the venerable 'isql' program 
  supplied by Sybase. It came about due to years of frustration of 
  trying to do real work with a program that was never meant to perform 
  real work.

  Sqsh is much more than a nice prompt, it is intended to provide much 
  of the functionality provided by a good shell, such as variables, 
  redirection, pipes, back-grounding, job control, history, command 
  completion, and dynamic configuration. Also, as a by-product of the 
  design, it is remarkably easy to extend and add functionality. 
endef

SF_PROJ = ganglia
MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(NAME)-$(VERSION).tar.gz
DISTFILES += $(PATCHFILES)
DISTNAME = $(NAME)-$(VERSION)

EXTRA_DOCS = $(PATCHFILES)

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

# If the url used to check for software update is different of MASTER_SITES, then 
# uncomment the next line. Otherwise it is set by default to the value of MASTER_SITES
# UPSTREAM_MASTER_SITES = 

BUILD64 = 1

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --enable-shared --disable-nls

include gar/category.mk
