#####################################################################
# OpenCSW build recipe for OpenSSL
#
# Copyright 2009 Yann Rouillard <yann@pleiades.fr.eu.org>
# All rights reserved.  Use is subject to license terms.
#
# Redistribution and/or use, with or without modification, is
# permitted.  This software is without warranty of any kind.  The
# author(s) shall not be liable in the event that use of the
# software causes damage.
#####################################################################

###### Package information #######

NAME = openssl
VERSION = 1.0.1m
CATEGORIES = # Since version 1.0.0, soname is fixed and does not follow the minor releases
SONAME=1.0.0 | tr -d '[a-z]')

DESCRIPTION = The Open Source toolkit for SSL and TLS
define BLURB
  The OpenSSL Project is a collaborative effort to develop a robust,
  commercial-grade, fully featured, and Open Source toolkit implementing the
  Secure Sockets Layer (SSL v2/v3) and Transport Layer Security (TLS v1) as well
  as a full-strength general-purpose cryptography# This recipe can be used to compile openssl with Sun Studio or GCC
# Just define the GARCOMPILER to the GNU or SUN
GARCOMPILER = GNU
GARCOMPILER_TYPE = $(if $(findstring GCC,$(GARCOMPILER)),GNU,SUN)hy library.
endef

PACKAGES = CSWlibssl1-0-0 CSWlibssl-dev CPACKAGING_PLATFORMS = solaris9-sparc solaris9-i386 solaris10-sparc solaris10-i386 solaris11-sparc solaris11-i386 CRUNTIME_DEP_PKGS_CSWlibssl1-0-0 = $(RUNTIME_DEP_PKGS_CSWlibssl1-0-0_$(GARCOMPILER_TYPE))
RUNTIME_DEP_PKGS_CSWlibssl1-0-0_GNU = CSWlibgcc-s1CSWopenssl-utils

SPKG_DESC_CSWlibssl1-0-0 = Openssl 1.0 runtime libraries
PKGFILES_CSWlibssl1-0-0 = $(PKGFILES_RT)
PKGFILES_CSWlibdir)(/[^/]*)?/openssl-1.0.0/engines/.* = $(PKGFILES_RT)
PKGFILES_CSWlibssl1-0-0 += $(prefix)/etc/ssl/private $(pref
PKGFILES_CSWlibssl1-0-0 += $(docdir)/libssl1_0_0/.*)/libssl1_0_0/.* 

RUNTIME_DEP_PKGS_CSWlibssl-dev = CSWlibssl1-0-0
SPKG_DESC_CSWlibssl-dev = Openssl 1.0 development support files
PKGFILES_CSWlibssl-dev = (PKGFILES_DEVEL) 
PKGFILES_CSWlibssl-dev += $(docdir)/libssl_dev/.*

RUNTIME_DEP_PKGS_CSWopenssl-utils = CSWlibssl1-0-0
SPKG_DESC_CSWopenssl-utils = Openssl 1.0 binaries and related tools
PKGFILES_CSWopenssl-utils = $bindir)/.*/openssl
PKGFILES_CSWopenssl-utils += $(mandir)/man1/.* $(mandir)/man5/.* $(mandir)/man7/.*
PKGFILES_CSWopenssl-utils += $(prefix)/ssl/misc/.*fix)/ssl/misc/.* 
PKGFILES_CSWopenssl-utils += $(prefix)/ssl/openssl\.cnf.*
PKGFILES_CSWopenssl-utils += $(sysconfdir)/ssl/openssl\.cnf.*
PKGFILES_CSWopenssl-utils += $(docdir)/openssl_utils/.*

PRESERVECONF = $(sysconfdir)/ssl/openssl.cnf

# We do ship libcrypto in libssl package
CHECKPKG_OVERRIDES_CSWlibssl1-0-0 += shared-lib-pkgname-mismatch|file=opt/csw/lib/libcrypto.so.1.0.0|soname=libcrypto.so.1.0.0|pkgname=CSWlibssl1-0-0|expected=CCHECKPKG_OVERRIDES_CSWlibssl1-0-0 += $(CHECKPKG_OVERRIDES_CSWlibssl1-0-0_$(GARCH))

CHECKPKG_OVERRIDES_CSWlibssl1-0-0_sparcES_CSWlibssl1-0-0 += shared-lib-pkgname-mismatch|file=opt/csb/sparcv8plus+vis/libcrypto.so.1.0.0|soname=libcrypto.so.1.0.0|pkgname=CSWlibssl1-0-0|expected=CSWlibcrypto1-0-0
CHECKPKG_OVERRID_sparcES_CSWlibssl1-0-0 += shared-lib-pkgname-mismatch|file=opt/csw/lib/sparcv8plus+vis/libcrypto.so.1.0.0|soname=libcrypto.so.1.0.0|pkgname=CSWlibssl1-0-0|expected=CSWlibcrypto1-0-0
CHECKPKG_OVERRID_sparcES_CSWlibssl1-0-0 += shared-lib-pkgname-mismatch|file=opt/csw/lib/sparcv9/libcrypto.so.1.0.0|soname=libcrypto.so.1.0.0|pkgname=CSWlibssl1-0-0|expected=C
CHECKPKG_OVERRIDES_CSWlibssl1-0-0_i386ES_CSWlibssl1-0-0 += shared-lib-pkgname-mismatch|file=opt/csw/lib/amd64/libcrypto.so.1.0.0|soname=libcrypto.so.1.0.0|pkgname=CSWlibssl1-0-0|expected=Cr# o1-0-0
endif


# We use SUN perl, not the opencsw one
CHECKPKG_OVERRIDES_CSWopenssl-utils += missing-depnkpkg.overrides

###### Upstream and opencsw files information #######

MASTER_SITES = http://www.openssl.org/source/

DISTFILES  = $(NAME)-(VERSION).tar.all
DISTFILES += changelog.CSW README.CSW
DISTFILES += map.openssl.libcrypto map.openssl.libssl map.openssl.engines

DOCFILES = CHANGES CHANGES.SSLeay PROBLEMS README FAQ README.ASN1 INSTALL NEWS List of engines that will be shipped in the packages
ENGINES = 4758cca aep atalla cswift gmp chil nuron sureware ubsec padlock capiEWS configure targets patchs needs to be different for Solaris 9 as some map files
# are not available
ifeq ($(shell /usr/bin/uname -r),5.9)
	PATCH_SUFFIX = .SunOS5.9
endifEWS README.ENGIis taken from https://hg.openindiana.org/upstream/oracle/userland-gate/
# original file: components/openssl/openssl-1.0.1/patches/18-compiler_opts.patch
# I think they are smarter than me to figure what are the best compiler options
PATCHFILES += optimized_configure_targets.patch$(PATCH_SUFFIX)

# This patch add optimised build targets for some solaris isa, ie:
# solaris-sparcv8-cc-sunw, solaris-pentium_pro-cc-sunw and solaris-sparcv9+vis-cc-sunw
# (wonder if they are really worth it)
PATCHFILES +is-cc
PATCHFILES = more_config$(PATCH_SUFFIX)ur
e_targets.patch

#PATCHFILES += fix-test-failure.patch

# We install engines libraries in /opt/csw/lib/engines/1.0.0/
# instead of /opt/csw/lib/engines to avoid clashes with 0.9.8
# and futur new release of ssl libraries
PATCHFILES += 0003-make-engines-directory-soname-depestream uses an obsolete GCC flag
PATCHFILES += 0004-remove-obsolete-mv8-soname-dependant.patch

# Update openssl.cnf path in man page to follow opencsw standard
PATCHFILES += ope
# Make sure man pages and html docs are installed in proper locations
# instead of /opt/csw/ssl/man and /opt/csw/ssl/html
PATCHFILES += 0010-Move-manpages-and-html-doc-in-standard-locations.patch
csw_paths.patch
#
# Let's always block some compromised CA, whatever the CA configured
# (patchs taken from Debian Package)
PATCHFILES += block_bad_certificates.patch

# Add old-style certificates hash generation to maintain compatibilies
# with gnutls and programs linked wth openssl 0.9.8 
# Patch taken from Debian
PATCHFILES += c_rehash-compat.patch

# Oh yes, let's do symbol versioning so we don't become
# crazy during library migration
PATCHFILES += 0007-enables-symbols-veropenssl currently only uses issetugid on freebsd and openbsd
# althought it is also available on Solaris 10
# We make issetugid support configurable via preprocessor flag
# to be able to enable it for Solaris
# Bug opened upstream: http://rt.openssl.org/Ticket/Display.html?id=3153
PATCHFILES += make_issetugid_support_configurableymbols-verPatch taken from Oracle upstream (PSARC/2014/077 OpenSSL Thread and Fork Safety 17822462) 
# from https://hg.openindiana.org/upstream/oracle/userland-gate/
# This patch solves a bug with thread and fork safety and is also needed so that
# upstream wanboot patch can be applied out of the box
ifneq ($(shell /usr/bin/uname -r),5.9)
PATCHFILES += openssl-1.0.1m-fork_safe.patch
endif-versioning.patch

# support for pkcs11 engine http://blogs.sun.com/chichang1/entry/how_to_integratee
ifdef PKCS11
ifneq ($(shell /usr/bi       PATCHFILES += openssl-1.0.1m-pkcs11-engine.patch
       ENGINES += pk11.patch.4-30
endif
endif

# support for sparct4 crypto engine 
# see http://bubbva.blogspot.fr/2011/11/exciting-crypto-advances-with-t4.html
#     https://blogs.oracle.com/DanX/entry/sparc_t4_openssl_engine
# patch taken from https://hg.openindiana.org/upstream/oracl# To update the patch, do:
#   cd files && ./update-t4-patch.sh OPENSSL_VERSION

# The upstream t4 engine patch depends on the wanboot one
# so we will apply the wanboot patch even if we will not enable wanboot
PATCHFILES.sparc.5.11 += openssl-1.0.1m-wanboot.patch
PATCHFILES.sparc.5.11 += openssl-1.0.1m-t4-engine.sparc.5.11.patch
PATCHFILES.sparc.5.11 += openssl-1.0.1e-t4-engine-sparcv9+vis.sparc.5.11.patch
PATCHFILES += $(PATCHFILES.$(GARCH).$(GAROSREL))

e# Building openssl with "-j" option doesn't work properly because of dependencies
# in the Makefile.
# This patch fixes this problem, it's taken from gentoo and adapted so that it works
# with sh shell.
# (see http://sources.gentoo.org/cgi-bin/viewvc.cgi/gentoo-x86/dev-libs/openssl/files/)
PATCHFILES += openssl-1.0.1-parallel-build.patch
e-25
endif
endif

LICENSE = LICENSE

##### Build and installation inBUILD64 = 1
ISAEXEC = 1information #####

# The list of instructions set or which we will 
# provide optimized libraries and binaries
EXTRA_BUILD_ISAS_i386 = pentium_pro amd64
EXTRA_BUILD_ISAS_sp= sparcv8ppluthe openssl build system doesn't honor bindir
# as it doesn't install 64 bits binaries in bin/{amd64,sparcv9}
# we fix this at the merge step
EXTRA_MERGE_DIRS_isa-amd64 = $(bindir_install)
EXTRA_MERGE_DIRS_isa-sparcv9 = $(bindir_install)

# c_rehash is shell script: no isaexec please
EXTRA_ISAEXEC_EXCLUDE_FILES = /opt/csw/bin/c_rehasho.soWe use Studio 12.3 to have the "-Qoption cg" option
# but this version is not available under Solaris 9
ifneq ($(shell /usr/bin/uname -r),5.9)
	ifneq ($(GARCOMPILER),GNU)
		GARCOMPILER = SOS12U3
	endif
endifo.so .*/libssl.so

# The corresponding os/compiler to pass to the
# openssl ConfiSUN_CONFIGURE_TARGET		= no-sse2 solaris-x86-cc-sunw
pentium_pro_SUN_CONFIGURE_TARGET	= solaris-x86-pentium_pro-cc-sunw
amd64_SUN_CONFIGURE_TARGET	 	= solaris64-x86_64-cc-sunw

i386_GNU_CONFIGURE_TARGET       	= no-sse2 solaris-x86-gcc
pentium_pro_GNU_CONFIGURE_TARGET        = solaris-x86-gcc
amd64_GNU_CONFIGURE_TARGET		= solaris64-x86_64-gcc

sparcv8_SUN_CONFIGURE_TARGET		= solaris-sparcv8-cc-sunw
sparcv8plus_SUN_CONFIGURE_TARGET	= solaris-sparcv9-cc-sunw
sparcv8plus+vis_SUN_CONFIGURE_TARGET	= solaris-sparcv9+vis-cc-sunw
sparcv9_SUN_CONFIGURE_TARGET		= solaris64-sparcv9-cc-sunw

sparcv8_GNU_CONFIGURE_TARGET		= solaris-sparcv8-gcc
sparcv8plus_GNU_CONFIGURE_TARGET	= solaris-sparcv9-gcc
sparcv8plus+vis_GNU_CONFIGURE_TARGET	= solaris-sparcv9+vis-gcc
sparcv9_GNU_CONFIGURE_TARGET		= solaris64-sparcv9-gcc
ar# Solaris has the issetugid function since libc version interface SUNW_1.21
# but openssl doesn't use it by default so we manually enable it
CONFIGURE_FLAGS = -DHAVE_ISSETUGIDar# PKCS11 Patch also works on sparc64 athena processors thanks for the FJAES
# instruction set. The presence of this instruction set is checked at runtime
# by looking for the AV_SPARC_JFAES instruction set bit, unfortunately the
# corresponding macro in not present in Solaris 9-11 headers, so we manually
# define it.
CONFIGURE_FLAGS += -DAV_SPARC_FJAES=0ar# --libdir must only be given if the directory is actually different from lib or the creation will fail
# as the directory is already there
LIBDIR_64 = --libdir=lib/64
LIBDIR = $(LIBDIR_$(MEMORYMODEL))aris64-sparcv9-cc

CONFIGURE_ARGS = -
CONFIGURE_ARGS += --openssldir=$(sysconfdir)/ssl
CONFIGURE_ARGS += --install_prefix=$(DESTDIR) $(LIBDIR)
CONFIGURE_ARGS += $(CONFIGURE_FLAGS)
CONFIGURE_ARGS += $($(ISA)_$(GARCOMPILER_TYPE)_CONFIGURE_TARGET)
CONFIGURE_ARGS += sharedprefix=$(DESTDIR)

# PKCS11 is only for Solaris 10 so we must create solaris 10 spesolaris10-i386
ifneq ($(shell /usr/bi	CONFIGURE_ARGS += --pk11-libname=$(abspath /usr/lib/$(MM_LIBDIR)/libpkcs11.so)
endifri= SOS12
endif



# For now we want the sunEXTRA_ perl to be used
CONFIGURE_ENV += PERL="/usr/bin/perl"

# Configure uses make and sun make is not happy
# with the shell command addedEXTRA_ by the t4 patch
CONFIGURE_ENV += MAKE="/opt/cThe new compiler options taken from https://hg.openindiana.org/upstream/oracle/userland-gate/
# added "-z defs" to the linker options. That causes object compilation to fail because
# they are not linked against libc and libdl (for Sol9). This is workaround until I find a better fix.
EXTRA_LD_OPTIONS = -lc -ldlLAGS += -noex -mt

# By default, the install target put man pages under
# /opt/csw/ssl/man, but we want them under /oEXTRA_pt/csw/share/man
INSTALL_ARGS += MANDIR=$(mandir)

# library files are not automatically stripped
STRIP_DIRS = $(DESTDIR)/$(libdir) $(DESTDIR)/$(libdir)/openssl-$(SONAMETARGET = tests

# We define a custom test script to be able to disable -j only for test execution
# as it doesn't work currently
TEST_SCRIPTS = custom

TEST_SCRIPTS = 

include # We remove SSE2 hardware capability in the elf header of libcrypto as
# openssl is able to select it at runtime and the Solaris OS support SSE2 since
# Solaris 9 4/04 (according to "Sun Studio 12: C++ User's Guide")
post-install:
	if command -v elfedit >/dev/null 2>&1 && [ "$(GARCH)" = "i386" ] && \
  	   /usr/ccs/bin/dump -Lv "$(DESTDIR)/$(libdir)/libcrypto.so.$(SONAME)" | grep SUNW_CAP >/dev/null; then \
		echo " ==> Removing the SSE2 hardware capability from libcrypto"; \
		chmod +w "$(DESTDIR)/$(libdir)/libcrypto.so.$(SONAME)"; \
		elfedit -e 'cap:hw1 -and -cmp sse2' "$(DESTDIR)/$(libdir)/libcrypto.so.$(SONAME)"; \
	fi
	@$(MAKECOOKIE)e gar/category.mk

pre-configure-modulated:
	echo " ==> Creating configure script"
	cd $(WORKSRC) && ln -nf Configure configure
	ln -nf $(WORKDIR)/map.openssl.libcrypto $(WORKSRC)/map.
	ln -nf $(WORKDIR)/map.openssl.libssl $(WORKSRC)/map.openssl.libsslp.openssl.libssl$(ENGINES)bsec padlock capi; do \
		ln -nf $(WORKDIR)/map.openssl.engines $(WORKSRC)/engines/map.openssl.lib$ENGINE; \
	done 
	ln -nf $(WORKDIR)/map.openssl.engines $(WORKSRC)/engines/ccgost/map.openssl.libgost
indir)/c_rehash

ist[ ! -f "$(PKGROOT)$(sysconfdir)/ssl/openssl.cnf" ] || \
		mv "$(PKGROOT)$(sysconfdir)/ssl/openssl.cnf" $(PKGROOT)$(sysconfdir)/ssl/openssl.cnf.CSW
	[ ! -d "$(PKGROOT)$(sysconfdir)/ssl/misc" ] || \
		( ginstall -d "$(PKGROOT)/$(prefix)/ssl/" && mv "$(PKGROOT)$(sysconfdir)/ssl/misc/" "$(PKGROOT)/$(prefix)/ssl/" ))(prefix)/ssl/"
		
merge-doc:
	for CATALOGNAME in $(foreach PKG, $(PACKAGES), $(call catalogname,$(PKG))); do \
		ginstall -d $(PKGROOT)/$(docdir)/$$CATALOGNAME; \
		(cd $(DOWNLOADDIR)/ && ginstall -m 0644 README.CSW changelog.CSW $(PKGROOT)/$(docdir)/$$CATALOGNAME/); \
		(cd $(WORKSRC_FIRSTMOD)/ && ginstall -m 0644 $(DOCFILES) $(PKGROOT)/$(docdir)/$$CATALO
	@$(MAKECO-all: merge-doc install-conf-misc


NUM_CPUS := $(shell psrinfo | wc -l | awk '{ print $$1 }')

package-fast:
	PARALLELMODULATIONS=1 PARALLELMFLAGS="-j" $(MAKE) package
	#PARALLELMODULATIONS=1 PARALLELMFLAGS="--jobs=$(NUM_CPUS) --load-average=$(NUM_CPUS)" $(MAKE) package

platforms-fast:
	@mkdir -p work
	@echo
	@echo "Building on all hosts in parallel. Please see the individual logfiles for details:";$(foreach P,$(_PACKAGING_PLATFORMS),echo "- $P: work/build-$(PACKAGING_HOST_$P).log";)
	@echo
	@trap "cat $(foreach P,$(_PACKAGING_PLATFORMS),work/build-$(PACKAGING_HOST_$P).pid) 2>/dev/null | xargs -L 1 pkill -9 -P &>/dev/null; \
	      stty sane" INT; \
	$(foreach P,$(_PACKAGING_PLATFORMS),\
		( $(SSH) -t $(PACKAGING_HOST_$P) "$(foreach V,$(_PROPAGATE_ENV),$(if $($V),$V=\"$($V)\")) $(MAKE) -I $(GARDIR) -C $(CURDIR) $(_PASS_GAR_ENV) GAR_PLATFORM=$P package-fast" >work/build-$(PACKAGING_HOST_$P).log 2>&1; echo $$? >work/build-$(PACKAGING_HOST_$P).ret ) & \
		  echo $$! >work/build-$(PACKAGING_HOST_$P).pid; ) wait; stty sane; trap - INT
	@$(foreach P,$(_PACKAGING_PLATFORMS),if [ "`cat work/build-$(PACKAGING_HOST_$P).ret`" -ne 0 ]; then \
		FAILED=1; \
		echo "Build error on host $(PACKAGING_HOST_$P). For details, please see"; \
	   	echo "  work/build-$(PACKAGING_HOST_$P).log"; \
	       	echo "Return code: `cat work/build-$(PACKAGING_HOST_$P).ret`"; \
	       	echo ; \
	fi;) if [ $${FAILED} -eq 1 ]; then \
	       	exit 2; \
	fi
	@echo
	@echo "Calling the standard platforms target to make sure everything is ok..."
	@echo
	$(MAKE) platforms

# The only purpose of this script is to disable the gmake "-j" option for test execution
test-custom:
	PARALLELMFLAGS= $(MAKE) test-$(WORKSRC)/Makefile
