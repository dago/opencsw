NAME       = clamav
VERSION    = 0.97.6
#VERSION    = 0.97rc
#DISTNAME   = $(NAME)-devel-latest
GARTYPE = v2

DESCRIPTION = Clam AntiVirus
define BLURB
  Clam AntiVirus is an open source (GPL) anti-virus toolkit for UNIX, designed 
  especially for e-mail scanning on mail gateways. It provides a number of 
  utilities including a flexible and scalable multi-threaded daemon, a command 
  line scanner and advanced tool for automatic database updates. The core of 
  the package is an anti-virus engine available in a form of shared library.
endef

#SF_PROJECT      = clamav
#MASTER_SITES = $(SF_MIRRORS)
#MASTER_SITES = http://www.clamav.net/snapshot/
MASTER_SITES = http://www.clamav.net/internal/
DISTFILES    = $(NAME)-$(VERSION).tar.gz
#DISTFILES    = $(NAME)-devel-latest.tar.gz

PACKAGES                   += CSWclamav
CATALOGNAME_CSWclamav       = clamav
SPKG_DESC_CSWclamav         = $(DESCRIPTION)
RUNTIME_DEP_PKGS_CSWclamav  = CSWlibclam6
RUNTIME_DEP_PKGS_CSWclamav += CSWlibz1
RUNTIME_DEP_PKGS_CSWclamav += CSWlibncurses5

PACKAGES                     += CSWlibclam6
CATALOGNAME_CSWlibclam6       = libclam6
SPKG_DESC_CSWlibclam6         = $(DESCRIPTION) Library
RUNTIME_DEP_PKGS_CSWlibclam6  = CSWlibz1
RUNTIME_DEP_PKGS_CSWlibclam6 += CSWlibltdl7
RUNTIME_DEP_PKGS_CSWlibclam6 += CSWlibbz2-1-0
RUNTIME_DEP_PKGS_CSWlibclam6 += CSWlibiconv2
RUNTIME_DEP_PKGS_CSWlibclam6 += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibclam6 += CSWlibstdc++6
INCOMPATIBLE_PKGS_CSWlibclam6 = CSWlibclamav

PACKAGES                         += CSWlibclam6-dev
CATALOGNAME_CSWlibclam6-dev       = libclam6_dev
SPKG_DESC_CSWlibclam6-dev         = $(DESCRIPTION) Development
RUNTIME_DEP_PKGS_CSWlibclam6-dev  = CSWlibclam6
INCOMPATIBLE_PKGS_CSWlibclam6-dev = CSWlibclamav-devel CSWlibclamav6-devel

PATCHFILES  = CSWclamav.freshclam.conf.p
PATCHFILES += CSWclamav.clamd.conf.p
PATCHFILES += CSWclamav.clamav-milter.conf.p
PATCHFILES += CSWclamav.optparser.c.p
# Not needed with 0.97.6
#PATCHFILES += CSWclamav.scanners.c.p

# Must have 64-bit libmilter for this to work
#BUILD64 = 1

#PACKAGING_PLATFORMS  = solaris9-sparc solaris9-i386
#PACKAGING_PLATFORMS += solaris10-sparc solaris10-i386
PACKAGING_PLATFORMS = solaris10-sparc solaris10-i386

GARCOMPILER = GNU

# Seems to be a compiler bug forcing us to use -xO2 instead of -xO3
# http://bugs.sun.com/view_bug.do?bug_id=6683773
# New bug filed since the above one isn't really solved, no bug id yet
#OPT_FLAGS_SOS = -xO2

sysconfdir = /etc/opt/csw

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --disable-clamav
# unrecognized by 0.95rc1? CONFIGURE_ARGS += --with-sendmail=$(libdir)/sendmail
CONFIGURE_ARGS += --with-dbdir=/var/opt/csw/$(NAME)/db
CONFIGURE_ARGS += --localstatedir=/var/opt/csw/$(NAME)
CONFIGURE_ARGS += --sysconfdir=$(sysconfdir)
CONFIGURE_ARGS += --enable-milter
#CONFIGURE_ARGS += --disable-llvm
#CONFIGURE_ARGS += --enable-check
CONFIGURE_ARGS += --enable-clamdtop

# Enable support for files > 2GB in size.
#EXTRA_CFLAGS = -D_FILE_OFFSET_BITS=64 -D_LARGEFILE_SOURCE
#EXTRA_CFLAGS = -D_FILE_OFFSET_BITS=64

EXTRA_MERGE_EXCLUDE_FILES = .*~ $(libdir)/.*\.a $(libdir)/.*\.la

PKGFILES_CSWlibclam6-dev = $(PKGFILES_DEVEL)
PKGFILES_CSWlibclam6     = $(PKGFILES_RT)
PKGFILES_CSWlibclam6    += $(docdir)/libclamav/.*

PROTOTYPE_MODIFIERS = 1
PROTOTYPE_FILES_1   = \/var\/opt\/csw\/clamav.*
PROTOTYPE_CLASS_1   = ugfiles
PROTOTYPE_USER_1    = clamav

INITSMF     = /etc/opt/csw/init.d/cswclamd
INITSMF    += /etc/opt/csw/init.d/cswclamav-milter
SAMPLECONF  = /etc/opt/csw/clamd.conf
SAMPLECONF += /etc/opt/csw/clamav-milter.conf
SAMPLECONF += /etc/opt/csw/freshclam.conf
USERGROUP   = /etc/opt/csw/pkg/CSWclamav/cswusergroup

MIGRATE_FILES_CSWclamav      = clamd.conf clamav-milter.conf freshclam.conf
MIGRATE_SOURCE_DIR_CSWclamav = /opt/csw/etc
MIGRATE_DEST_DIR_CSWclamav   = /etc/opt/csw

SPKG_SOURCEURL = http://www.clamav.net

#SKIPTEST = 1

# These are harmless examples
CHECKPKG_OVERRIDES_CSWclamav += file-with-bad-content|/usr/local|root/etc/opt/csw/clamd.conf.CSW
CHECKPKG_OVERRIDES_CSWclamav += file-with-bad-content|/usr/local|root/opt/csw/share/doc/clamav/README
CHECKPKG_OVERRIDES_CSWclamav += file-with-bad-content|/usr/local|root/opt/csw/share/doc/clamav/INSTALL.clamav-milter.CSW
CHECKPKG_OVERRIDES_CSWclamav += file-with-bad-content|/usr/local|root/opt/csw/share/doc/clamav/ChangeLog
CHECKPKG_OVERRIDES_CSWclamav += file-with-bad-content|/usr/local|root/opt/csw/share/doc/clamav/html/node54.html
CHECKPKG_OVERRIDES_CSWclamav += file-with-bad-content|/usr/local|root/opt/csw/share/doc/clamav/html/node56.html
CHECKPKG_OVERRIDES_CSWclamav += file-with-bad-content|/usr/local|root/opt/csw/share/doc/clamav/html/node24.html
CHECKPKG_OVERRIDES_CSWclamav += file-with-bad-content|/usr/local|root/opt/csw/share/doc/clamav/html/node15.html
CHECKPKG_OVERRIDES_CSWlibclam6 += file-with-bad-content|/usr/local|root/opt/csw/lib/libclamav.so.6.1.15            

# We don't split to three separate packages
CHECKPKG_OVERRIDES_CSWlibclam6 += shared-lib-pkgname-mismatch|file=opt/csw/lib/libclamav.so.6.1.15|soname=libclamav.so.6|pkgname=CSWlibclam6|expected=CSWlibclamav6
CHECKPKG_OVERRIDES_CSWlibclam6 += shared-lib-pkgname-mismatch|file=opt/csw/lib/libclamunrar.so.6.1.15|soname=libclamunrar.so.6|pkgname=CSWlibclam6|expected=CSWlibclamunrar6
CHECKPKG_OVERRIDES_CSWlibclam6 += shared-lib-pkgname-mismatch|file=opt/csw/lib/libclamunrar_iface.so.6.1.15|soname=libclamunrar_iface.so.6|pkgname=CSWlibclam6|expected=CSWlibclamunrar-iface6

include gar/category.mk

DOCS  = AUTHORS BUGS ChangeLog
DOCS += FAQ NEWS README UPGRADE
DOCS += docs/clamav-mirror-howto.pdf
DOCS += docs/clamdoc.pdf
DOCS += docs/phishsigs_howto.pdf
DOCS += docs/signatures.pdf

DOCDEST = $(DESTDIR)$(docdir)/$(NAME)

post-install-modulated:
	@echo " ==> Post-install for $(NAME) (custom)"
	@ginstall -d $(DESTDIR)/etc/opt/csw/init.d
	@ginstall -m 755 $(FILEDIR)/CSWclamav.cswclamd $(DESTDIR)/etc/opt/csw/init.d/cswclamd
	@ginstall -m 755 $(FILEDIR)/CSWclamav.cswclamav-milter $(DESTDIR)/etc/opt/csw/init.d/cswclamav-milter
	@ginstall -d $(DESTDIR)$(sysconfdir)/pkg/CSWclamav
	@ginstall -m 644 $(FILEDIR)/CSWclamav.cswusergroup $(DESTDIR)$(sysconfdir)/pkg/CSWclamav/cswusergroup
	@ginstall -d $(DOCDEST)
	@$(foreach DOC,$(DOCS),ginstall -m 644 $(WORKSRC)/$(DOC) $(DOCDEST);)
	@ginstall -m 644 $(FILEDIR)/CSWclamav.INSTALL.clamav-milter.CSW $(DOCDEST)/INSTALL.clamav-milter.CSW
	@ginstall -m 644 $(FILEDIR)/CSWclamav.README.CSW $(DOCDEST)/README.CSW
	@ginstall -d $(DOCDEST)/contrib
#	@ginstall -m 644 $(WORKSRC)/contrib/clamdwatch/* $(DOCDEST)/contrib
#	@ginstall -m 644 $(WORKSRC)/contrib/cleanup-partial.pl $(DOCDEST)/contrib
	@ginstall -d $(DOCDEST)/html
	@ginstall -m 644 $(WORKSRC)/docs/html/* $(DOCDEST)/html
	@chmod 600 $(DESTDIR)$(sysconfdir)/freshclam.conf
#	rm -f $(DESTDIR)/var/opt/csw/$(NAME)/db/*
	@ginstall -d $(DESTDIR)/var/opt/csw/$(NAME)/db
	@$(MAKECOOKIE)
