GARNAME = exim
GARVERSION = 4.68
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
	preinstall preremove request space checkinstall)
DISTFILES += Makefile.patch exim_install.patch spf2.patch
DISTFILES += i.smfyes i.smfno

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.bz2

PATCHFILES = Makefile.patch exim_install.patch spf2.patch

LD_OPTIONS = -R/opt/csw/lib/\$$ISALIST -R/opt/csw/lib

# scripts/exim_install has been patched to use this variable
EXIM_VERSION = $(GARVERSION)
export EXIM_VERSION

# This is needed for the SPF2 workaround:
PWD = $(shell pwd)

# Local/Makefile has been patched to use these:
CSW_CC = $(SUN_CC)
CSW_OPT = $(SUN_CC_OPT)
CSW_WORKSRC = $(PWD)/$(WORKSRC)
export CSW_CC CSW_OPT CSW_WORKSRC

# exim doesn't use configure
CONFIGURE_SCRIPTS =

# We don't want exim_install to create the exim symlink or run chown
INSTALL_ARGS = "INSTALL_ARG=-no_symlink -no_chown"

# exim doesn't have a test target
TEST_TARGET =

# We use this to strip binaries after we're done building
BINS =  exim exim_dbmbuild exim_dumpdb exim_fixdb exim_lock exim_tidydb
BINS += eximon.bin

include gar/category.mk

pre-patch:
	(cd $(WORKSRC); \
	test -r Local/Makefile || cp -p src/EDITME Local/Makefile; \
	test -r Local/eximon.conf || cp -p exim_monitor/EDITME Local/eximon.conf; \
	test -d spf2 || cp -pr /opt/csw/include/spf2 .)

post-patch:
	(cd $(WORKSRC); make makefile)

DOC_LIST = ChangeLog Exim3.upgrade Exim4.upgrade NewStuff OptionLists.txt
DOC_LIST += README README.SIEVE dbm.discuss.txt filter.txt pcrepattern.txt
DOC_LIST += pcretest.txt spec.txt

post-install:
	(cd $(DESTDIR)$(prefix)/sbin; \
	mv exim-$(GARVERSION) exim; \
	/usr/ccs/bin/strip $(BINS); \
	/usr/ccs/bin/mcs -d $(BINS))
	(cd $(DESTDIR)$(prefix)/etc/exim; \
	for i in aliases exim.conf; do \
		if [ -r "$$i" ]; then \
			echo "$$i -> $$i.CSW"; \
			mv "$$i" "$$i.CSW";	\
		fi \
	done)
	files/create_rc.d.sh $(DESTDIR)
	mkdir -p $(DESTDIR)$(prefix)/var/svc/manifest/network
	cp -p files/exim.xml  $(DESTDIR)$(prefix)/var/svc/manifest/network
	mkdir -p $(DESTDIR)$(prefix)/lib/svc/method
	cp -p $(DESTDIR)/etc/init.d/cswexim \
		$(DESTDIR)$(prefix)/lib/svc/method/svc-exim
	mkdir -p $(DESTDIR)$(prefix)/share/doc/exim
	cp -p files/README.CSW  $(DESTDIR)$(prefix)/share/doc/exim/README.CSW
	cp -p files/exim-env.sh $(DESTDIR)$(prefix)/etc/exim/exim-env.sh.CSW
	(cd $(WORKSRC)/doc; \
	cp -p $(DOC_LIST) $(DESTDIR)$(prefix)/share/doc/exim)
	gzip -f $(DESTDIR)$(prefix)/share/doc/exim/ChangeLog
	gzip -f $(DESTDIR)$(prefix)/share/doc/exim/spec.txt
