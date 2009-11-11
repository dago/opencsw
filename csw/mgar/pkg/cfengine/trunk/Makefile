GARNAME = cfengine
GARVERSION = 2.2.10
CATEGORIES = utils

DESCRIPTION = A tool for administering Networks of Diverse Machines
define BLURB
  Cfengine is a tool for setting up and maintaining BSD and System-5-like
  operating system optionally attached to a TCP/IP network. You can think of
  cfengine as a very high level language, much higher level than Perl or shell:
  a single statement can result in many hundreds of operations being performed
  on multiple hosts. Cfengine is good at performing a lot of common system
  administration tasks, and allows you to build on its strengths with your own
  scripts. You can also use it as a netwide front-end for `cron'.
endef

MASTER_SITES = http://www.cfengine.org/tarballs/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz 

PACKAGES = CSWcfengine CSWcfenginedoc
PKGFILES_CSWcfenginedoc  = .*/share/info/.*
PKGFILES_CSWcfenginedoc += .*/share/cfengine/.*

CATALOGNAME_CSWcfengine = cfengine
SPKG_DESC_CSWcfengine = A tool for administering Networks of Diverse Machines
REQUIRED_PKGS_CSWcfengine = CSWosslrt CSWbdb3

CATALOGNAME_CSWcfenginedoc = cfengine_doc
SPKG_DESC_CSWcfenginedoc = Cfengine documentation
ARCHALL_CSWcfenginedoc = 1

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --enable-DCE
CONFIGURE_ARGS += --with-docs
CONFIGURE_ARGS += --with-berkeleydb=/opt/csw/bdb33

GARCOMPILER = GCC3

TEST_TARGET = check

include gar/category.mk
