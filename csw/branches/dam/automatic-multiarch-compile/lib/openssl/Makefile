# Beware, this Makefile is complex because:
#  - we must also build and include in the package the
#    libraries of the previous version for comptability reason
#  
#  - we also build optimized libraries (amd64, pentium_pro, sparcv9, ...)
#
#
# On x86, amd64 libraries/binaries must be build on Solaris 10 whereas the
# other ones must be built on Solaris 8, so the packaging process must be 
# split in two steps and must use a nfs shared directory.
#
#  - first, on Solaris 10, build only the amd64 optimized binaries/libraries:
#
#     gmake COOKIEROOTDIR="$NFS_SHARED_DIR/cookie" DESTROOT="$NFS_SHARED_DIR" DESTIMG=$LOGNAME-$HOST8 GAROSREL=5.8 ISA=amd64 install-libs install-bin
#
#  - then on solaris 8, finish the build and packaging process:
#
#     gmake COOKIEROOTDIR="$NFS_SHARED_DIR/cookie" DESTROOT="$NFS_SHARED_DIR" package
#
# NFS_SHARED_DIR is the path of the directory nfs shared between the solaris 10
# and the solaris 8 host
# HOST8 is the hostname of the Solaris 8 host
#
#
GARNAME = openssl
GARVERSION = 0.9.8g
CATEGORIES = lib

OPENSSL_VERSION := $(shell echo $(GARVERSION) | sed -e 's/[a-z]//g')
OPENSSL_RELEASE := $(shell echo $(GARVERSION) | sed -e 's/[^a-z]//g')

DESCRIPTION = The Open Source toolkit for SSL and TLS
define BLURB
  The OpenSSL Project is a collaborative effort to develop a robust,
  commercial-grade, fully featured, and Open Source toolkit implementing the
  Secure Sockets Layer (SSL v2/v3) and Transport Layer Security (TLS v1) as well
  as a full-strength general-purpose cryptography library.
endef

MASTER_SITES = http://www.openssl.org/source/ http://openssl.org/news/

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*[a-z]?).tar.gz

DISTNAME   = $(GARNAME)-$(GARVERSION)
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz 
DISTFILES += $(call admfiles,CSWossl,depend prototype)
DISTFILES += $(call admfiles,CSWosslrt,checkinstall depend prototype-i386 prototype-sparc)
DISTFILES += $(call admfiles,CSWossldevel,depend prototype-i386 prototype-sparc)
DISTFILES += $(call admfiles,CSWosslutils,depend prototype)
DISTFILES += changelog.CSW
DISTFILES += i.conf r.conf

SPKG_CLASSES = none conf

PATCHFILES = openssl.$(OPENSSL_VERSION).patch

GARCOMPILER = SOS11

# The list of instructions set for which we will 
# provide optimized libraries and binaries
EXTRA_BUILD_ISAS_i386 = pentium_pro amd64
EXTRA_BUILD_ISAS_sparc = sparcv8plus+vis sparcv9

EXTRA_IGNORED_DIRS = bindir sbindir libexecdir

# The corresponding os/compiler to pass to the
# openssl Configure script
i386_OS_COMPILER 	= solaris-386-cc
pentium_OS_COMPILER	= solaris-pentium-cc
pentium_pro_OS_COMPILER	= solaris-pentium_pro-cc
amd64_OS_COMPILER 	= solaris64-x86_64-cc

sparcv8_OS_COMPILER 		= solaris-sparcv8-cc
sparcv8plus_OS_COMPILER		= solaris-sparcv9-cc
sparcv8plus+vis_OS_COMPILER	= solaris-sparcv9+vis-cc
sparcv9_OS_COMPILER		= solaris64-sparcv9-cc

CONFIGURE_ARGS = --prefix=$(prefix) shared $($(ISA)_OS_COMPILER) --install_prefix=$(DESTDIR)

# We want the csw perl to be used
#CONFIGURE_ENV += PERL="/opt/csw/bin/perl"
# For now we want the sun perl to be used
CONFIGURE_ENV += PERL="/usr/bin/perl"

EXT_CFLAGS   += -mt -xstrconst
EXT_CXXFLAGS += -noex -mt
#
# By default, the install target put man pages under
# /opt/csw/ssl/man, but we want them under /opt/csw/share/man
INSTALL_ARGS += MANDIR=$(mandir)

INSTALL_EXTRA_ISA_SCRIPTS = extra-isa


#########################################################################
# Variable definition for old libraries inclusion
# 
#########################################################################

OLDLIBS		 = 0.9.7m
DISTFILES 	+= oldlibs.list.0.9.7m-i386
DISTFILES 	+= oldlibs.list.0.9.7m-sparc

ifneq (,$(filter $(GARVERSION),$(OLDLIBS)))
EXTRA_BUILD_ISAS_i386 = pentium_pro
INSTALL_SCRIPTS = dynamic-libs
INSTALL_EXTRA_ISA_SCRIPTS = dynamic-libs
endif


#########################################################################
# Makefile instructions to handle old libraries inclusion (part I)
# 
# This should rather be handled by making a distinct package for each
# incompatible library version.
#########################################################################

ifneq (,$(filter $(GARVERSION),$(OLDLIBS)))
CHECKSUM_FILE	= checksums.$(GARVERSION)
WORKDIR	    	= $(WORKROOTDIR)/$(ISA).$(GARVERSION)
COOKIEDIR       = $(COOKIEROOTDIR)/$(ISA).$(GARVERSION)
endif

#########################################################################

include ../category.mk

SPKG_REVSTAMP := $(SPKG_REVSTAMP)_rev=$(OPENSSL_RELEASE)

pre-configure: 
	echo " ==> Creating configure script"
	cd $(WORKSRC) && ln -nf Configure configure
	$(MAKECOOKIE)

# we remove every debug information except symbol table
# (should rather be done in the gar scripts)
striplib:
	chmod -R u+w $(DESTDIR)$(libdir)
	find $(DESTDIR)$(libdir) -name "*.so*" -exec strip -x '{}' ';'

install-certs: 
	[ -f $(DESTDIR)$(prefix)/ssl/openssl.cnf ] && \
		ginstall -D $(DESTDIR)$(prefix)/ssl/openssl.cnf $(DESTDIR)$(sysconfdir)/ssl/openssl.cnf
	cp -r $(WORKSRC)/certs/* $(DESTDIR)$(prefix)/ssl/certs
	$(MAKECOOKIE)


install-extra-isa: install-static-libs install-dynamic-libs install-bin

install-static-libs:
	@if test ! -f "$(COOKIEDIR)/install-static-libs"; then \
		echo " ==> Installing static libraries from $(WORKSRC)"; \
		ginstall -d $(DESTDIR)$(libdir); \
		cd $(WORKSRC) && ginstall libcrypto.a libssl.a $(DESTDIR)$(libdir); \
		$(MAKECOOKIE); \
	fi

install-dynamic-libs:
	@if test ! -f $(COOKIEDIR)/install-dynamic-libs; then \
		echo " ==> Installing dynamic libraries from $(WORKSRC)"; \
		ginstall -d $(DESTDIR)$(libdir); \
		cd $(WORKSRC) && ginstall libcrypto.so.$(OPENSSL_VERSION) libssl.so.$(OPENSSL_VERSION) $(DESTDIR)$(libdir); \
		$(MAKECOOKIE); \
	fi

install-bin: 
	@if test ! -f $(COOKIEDIR)/install-bin; then \
		echo " ==> Installing binaries from $(WORKSRC)"; \
		ginstall -d $(DESTDIR)$(bindir); \
		cd $(WORKSRC) && ginstall apps/openssl $(DESTDIR)$(bindir); \
		$(MAKECOOKIE); \
	fi

pre-package: striplib install-certs install-oldlibs


#########################################################################
# Makefile instructions to handle old libraries inclusion (part II)
# 
# This should rather be handled by making a distinct package for each
# incompatible library version.
#########################################################################

update-oldlibs-archive: $(addprefix update-oldlibs-archive-,$(OLDLIBS))
update-oldlibs-archive-%: clean-oldlibs-archive-% install-oldlibs-%
	@echo " ==> Creating old libraries archive oldlibs.$*-$(GARCH).tar.gz"
	@cd $(DESTDIR) && tar cvf - `cat $(CURDIR)/$(DOWNLOADDIR)/oldlibs.list.$*-$(GARCH)` | gzip > $(CURDIR)/$(FILEDIR)/oldlibs.$*-$(GARCH).tar.gz

clean-oldlibs-archive: $(addprefix clean-oldlibs-archive-,$(OLDLIBS))	
clean-oldlibs-archive-%:
	@echo " ==> Removing old libraries archive oldlibs.$*-$(GARCH).tar.gz"
	@rm -f $(FILEDIR)/oldlibs.$*-$(GARCH).tar.gz 
	@rm -f $(COOKIEDIR)/install-oldlibs*

install-oldlibs: $(addprefix install-oldlibs-,$(OLDLIBS))
install-oldlibs-%: 
	@if [ -f $(FILEDIR)/oldlibs.$*-$(GARCH).tar.gz ]; then \
		echo " ==> Installing old libraries $* from existing old libraries archive oldlibs.$*-$(GARCH).tar.gz"; \
		cd $(DESTDIR) && gunzip -c $(CURDIR)/$(FILEDIR)/oldlibs.$*-$(GARCH).tar.gz | tar xvf -; \
	else \
		echo " ==> Build old libraries $*"; \
		$(MAKE) GARVERSION=$* install; \
	fi
	@$(MAKECOOKIE)
