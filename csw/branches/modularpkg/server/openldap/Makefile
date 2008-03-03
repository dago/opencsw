GARNAME = openldap
GARVERSION = 2.3.39
CATEGORIES = server

DESCRIPTION = Open source implementation of the Lightweight Directory Access Protocol
define BLURB
  The OpenLDAP Project is a collaborative effort to develop a robust,
  commercial-grade, fully featured, and open source LDAP suite of applications
  and development tools. The project is managed by a worldwide community of
  volunteers that use the Internet to communicate, plan, and develop the
  OpenLDAP Suite and its related documentation.
endef

MASTER_SITES = ftp://ftp.openldap.org/pub/OpenLDAP/openldap-release/
DISTFILES  = $(GARNAME)-$(GARVERSION).tgz
DISTFILES += $(call admfiles,CSWoldap,depend prototype)
DISTFILES += cswopenldap openldap.xml svc-openldap
DISTFILES += $(call admfiles,CSWoldapclient,depend prototype)
DISTFILES += $(call admfiles,CSWoldapdevel,depend prototype)
DISTFILES += $(call admfiles,CSWoldaprt,depend prototype)
DISTFILES += README.CSW openldaprc

PATCHFILES = patch-oldap-2.3.24-ntlm.diff
EXTRA_DOCS = README.CSW openldaprc $(PATCHFILES)

EXTRA_LIB = $(prefix)/bdb4/lib 
EXTRA_INC = $(prefix)/bdb4/include

CONFIGURE_ARGS = $(DIRPATHS)

INSTALL_SCRIPTS += custom

TEST_SCRIPTS =

# -- 64 Bit generation --

sparc_ARCH  = sparc
# TODO: pentium optimization
i386_ARCH   = i386
sparc_ARCH64 = sparcv9
i386_ARCH64  = amd64

ARCH=$($(GARCH)_ARCH)
ARCH64=$($(GARCH)_ARCH64)

ifdef ISA
ISALIST = $(ISA)
else
ifndef DO64
ISA = $(ARCH)
else
ISA = $(ARCH64)
endif
endif

WORKDIR       = $(WORKROOTDIR)/$(DESTIMG).d/$(ISA)
COOKIEROOTDIR = cookies.$(ISA)
COOKIEDIR     = $(COOKIEROOTDIR)

## For x86 ##
# for x86, we must share cookie work dir between sol10 and sol8
# so we make them arch-dependant instead of hostname dependant
DESTIMG = $(LOGNAME)-$(GARCH)
# we also make the target build directory (which looks like build.$(GAROSREL)-$(GARCH))
# identical between sol10 and sol8 by forcing the OS name used
GAROSREL = 5.8
# we force the OS for pkginfo, pkg filename so the final package step 
# performed on solaris 10 x86 really produce SunOS5.8 labelled packages.
SPKG_OSNAME = SunOS5.8

CONFIGURE_ARGS = $(DIRPATHS)

# Optimizer flags for architecture
OPTARCH_sparcv9 = v9
OPTARCH_amd64   = amd64

CLEAN_SCRIPTS = custom

ifdef DO64
	bindir = $(exec_prefix)/bin/$(ISA)
	libdir = $(exec_prefix)/lib/$(ISA)
endif

include ../category.mk

OPTARCH = $(OPTARCH_$(ISA))

build64:
	@echo " ==> Building 64 bit version"
	gmake DO64=1 build
	$(MAKECOOKIE)

install-custom:
	@for file in $(EXTRA_DOCS); do \
		ginstall -D $(WORKDIR)/$$file $(DESTDIR)$(docdir)/$(GARNAME)/$$file; \
	done
	@$(MAKECOOKIE)

install64: build64
	@echo " ==> Installing 64 bit version"
	gmake DO64=1 install-custom
	$(MAKECOOKIE)

pre-package: install64

clean64:
	gmake DO64=1 clean-all

clean-custom: clean64 clean-all

