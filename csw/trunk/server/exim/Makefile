GARNAME = exim
GARVERSION = 4.62
CATEGORIES = server

DESCRIPTION = The Exim Mail Transfer Agent
define BLURB
  Exim is a message transfer agent (MTA) developed at the University of
  Cambridge for use on Unix systems connected to the Internet. It is freely
  available under the terms of the GNU General Public Licence. In style it
  is similar to Smail 3, but its facilities are more general. There is a
  great deal of flexibility in the way mail can be routed, and there are
  extensive facilities for checking incoming mail. Exim can be installed in
  place of sendmail, although the configuration of exim is quite different
  to that of sendmail.
endef

MASTER_SITES = ftp://ftp.exim.org/pub/exim/exim4/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.bz2
DISTFILES += $(call admfiles,CSWexim,depend prototype postinstall postremove \
	preinstall preremove request)
DISTFILES += i.smfyes i.smfno space

PATCHFILES = Makefile.patch exim_install.patch

LD_OPTIONS = -R/opt/csw/lib/\$$ISALIST -R/opt/csw/lib

# scripts/exim_install has been patched to use this variable
EXIM_VERSION = $(GARVERSION)
export EXIM_VERSION

# Local/Makefile has been patched to use these:
CSW_CC = $(SUN_CC)
CSW_OPT = $(SUN_CC_OPT)
export CSW_CC CSW_OPT

# exim doesn't use configure
CONFIGURE_SCRIPTS =

# We don't want exim_install to create the exim symlink or run chown
INSTALL_ARGS = "INSTALL_ARG=-no_symlink -no_chown"

# exim doesn't have a test target
TEST_TARGET =

# We use this to strip binaries after we're done building
BINS =  exim exim_dbmbuild exim_dumpdb exim_fixdb exim_lock exim_tidydb
BINS += eximon.bin


include ../category.mk

pre-patch:
	(cd $(WORKSRC); \
	test -r Local/Makefile || cp -p src/EDITME Local/Makefile; \
	test -r Local/eximon.conf || cp -p exim_monitor/EDITME Local/eximon.conf)
post-patch:
	(cd $(WORKSRC); make makefile)

post-install:
	(cd $(DESTDIR)$(prefix)/sbin; \
	mv exim-$(GARVERSION) exim; \
	/usr/ccs/bin/strip $(BINS); \
	/usr/ccs/bin/mcs -d $(BINS))
	(cd $(DESTDIR)$(prefix)/etc/exim; \
	for i in *; do \
		echo "$$i -> $$i.CSW"; \
		mv "$$i" "$$i.CSW";	\
	done)
