NAME = exim
VERSION = 4.76
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
DISTFILES  = $(NAME)-$(VERSION).tar.bz2
DISTFILES += CSWexim.postinstall CSWexim.postremove CSWexim.preremove
DISTFILES += CSWexim.request CSWexim.cswreleasenotes

# NOTE TO FUTURE MAINTAINERS:
# This patch should be thoroughly reviewed for each update so as not to
# miss any new config options of interest...
PATCHFILES += 0003-Set-OpenCSW-build-options.patch
PATCHFILES += 0004-Force-Compiler-and-a-few-compilation-options.patch

BUILD_DEP_PKGS = CSWlibspf2-dev

RUNTIME_DEP_PKGS_CSWexim  = CSWiconv CSWoldaprt CSWosslrt CSWsasl
RUNTIME_DEP_PKGS_CSWexim += CSWmysql5rt CSWlibpq CSWlibspf2
RUNTIME_DEP_PKGS_CSWexim += CSWgzip CSWgzipextras
RUNTIME_DEP_PKGS_CSWexim += CSWlibpcre0

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.bz2

# They supply the GPL in a non-standard file.
LICENSE = LICENCE

LD_OPTIONS = -R/opt/csw/lib/\$$ISALIST -R/opt/csw/lib

INITSMF = /etc/opt/csw/init.d/cswexim

# scripts/exim_install has been patched to use this variable
EXIM_VERSION = $(VERSION)
export EXIM_VERSION

# This is needed for the SPF2 workaround:
PWD = $(shell pwd)

# Local/Makefile has been patched to use these:
CSW_CC = $($(GARCOMPILER)_CC)
CSW_OPT = $(CFLAGS)
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

UGPATH=/etc/opt/csw/pkg/CSWexim
UGENTRY = exim:exim:CSW Exim User:/var/opt/csw/spool/exim:/bin/false:::NP
USERGROUP = $(UGPATH)/cswusergroup

CHECKPKG_OVERRIDES_CSWexim += surplus-dependency|CSWgzipextras
CHECKPKG_OVERRIDES_CSWexim += surplus-dependency|CSWgzip
CHECKPKG_OVERRIDES_CSWexim += discouraged-path-in-pkgmap|/opt/csw/var/log
CHECKPKG_OVERRIDES_CSWexim += discouraged-path-in-pkgmap|/opt/csw/var/log/exim
CHECKPKG_OVERRIDES_CSWexim += file-with-bad-content|/usr/local|root/opt/csw/sbin/exim

PROTOTYPE_MODIFIERS = eximsuid eximlogs
PROTOTYPE_PERMS_eximsuid = 4755
PROTOTYPE_FILES_eximsuid = $(sbindir)/exim
PROTOTYPE_USER_eximlogs = exim
PROTOTYPE_GROUP_eximlogs = exim
PROTOTYPE_PERMS_eximlogs = 750
PROTOTYPE_FILES_eximlogs = $(prefix)/var/log/exim

include gar/category.mk

pre-patch-modulated:
	(cd $(WORKSRC); \
	test -r Local/Makefile || cp -p src/EDITME Local/Makefile; \
	test -r Local/eximon.conf || cp -p exim_monitor/EDITME Local/eximon.conf; \
	git add Local/; git ci -m 'Setup Local build default files'; \
	test -d spf2 || cp -pr /opt/csw/include/spf2 .; \
	git add spf2; git ci -m 'import spf2 header files' )
	@$(MAKECOOKIE)

pre-build-modulated:
	(cd $(WORKSRC); make makefile)
	@$(MAKECOOKIE)

DOC_LIST = ChangeLog Exim3.upgrade Exim4.upgrade NewStuff OptionLists.txt
DOC_LIST += README README.SIEVE dbm.discuss.txt filter.txt pcrepattern.txt
DOC_LIST += pcretest.txt spec.txt

post-install-modulated:
	(cd $(DESTDIR)$(prefix)/sbin; \
	mv exim-$(VERSION)-1 exim; \
	/usr/ccs/bin/strip $(BINS); \
	/usr/ccs/bin/mcs -d $(BINS))
	(cd $(DESTDIR)$(prefix)/etc/exim; \
	for i in aliases exim.conf; do \
		if [ -r "$$i" ]; then \
			echo "$$i -> $$i.CSW"; \
			mv "$$i" "$$i.CSW";	\
		fi \
	done)
	(cd $(DESTDIR); mkdir -p etc/opt/csw/init.d; \
		cp $(abspath $(FILEDIR)/cswexim) etc/opt/csw/init.d )
	mkdir -p $(DESTDIR)$(prefix)/share/doc/exim
	cp -p files/README.CSW  $(DESTDIR)$(prefix)/share/doc/exim/README.CSW
	cp -p files/exim-env.sh $(DESTDIR)$(prefix)/etc/exim/exim-env.sh.CSW
	(cd $(WORKSRC)/doc; \
	cp -p $(DOC_LIST) $(DESTDIR)$(prefix)/share/doc/exim)
	gzip -f $(DESTDIR)$(prefix)/share/doc/exim/ChangeLog
	gzip -f $(DESTDIR)$(prefix)/share/doc/exim/spec.txt
	@$(MAKECOOKIE)

post-merge:
	( cd $(PKGROOT); mkdir -p ./$(UGPATH); \
		echo "$(UGENTRY)" > ./$(UGPATH)/cswusergroup )
	( cd $(PKGROOT); mkdir -p opt/csw/var/log/exim )
	@$(MAKECOOKIE)
