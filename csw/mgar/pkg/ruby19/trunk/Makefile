GARNAME = ruby19
GARVERSION = 1.9.1
PATCHLEVEL = p376
CATEGORIES = lang

DISTNAME = ruby-$(GARVERSION)-$(PATCHLEVEL)

DESCRIPTION = Brief description
define BLURB
  Long description
endef

MASTER_SITES = ftp://ftp.ruby-lang.org/pub/ruby/1.9/
DISTFILES  = $(DISTNAME).tar.gz

# We define upstream file regex so we can be notifed of new upstream
# software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

# If the url used to check for software update is different of
# MASTER_SITES, then uncomment the next line. Otherwise it is set by
# default to the value of MASTER_SITES
# UPSTREAM_MASTER_SITES = 

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --program-suffix=19
CONFIGURE_ARGS += --enable-pthread

include gar/category.mk

ifdef USEGCC
GARCOMPILER = GNU
RUNTIME_DEP_PKGS_CSWruby19 += CSWgcc4corert
else
SOS11_LD_FLAGS =
endif
