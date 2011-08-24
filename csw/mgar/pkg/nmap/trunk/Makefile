NAME = nmap
VERSION = 5.59BETA1
CATEGORIES = net

DESCRIPTION = A network exploration tool and security/port scanner
define BLURB
  Nmap is a utility for network exploration or security auditing. It supports
  ping scanning (determine which hosts are up), many port scanning techniques
  (determine what services the hosts are offering), and TCP/IP fingerprinting
  (remote host OS or device identification). Nmap also offers flexible target
  and port specification, decoy/stealth scanning, sunRPC scanning, and more.
  Most Unix and Windows platforms are supported in both GUI and commandline
  modes.  Several popular handheld devices are also supported, including the
  Sharp Zaurus and the iPAQ.
endef

MASTER_SITES = http://nmap.org/dist/
DISTFILES = $(NAME)-$(VERSION).tar.bz2

PATCHFILES += 0001-Add-definition-for-INT_MAX.patch
PATCHFILES += 0002-Add-definitions-for-CMSG_ALIGN-CMSG_SPACE-and-CMSG_L.patch
PATCHFILES += 0003-Do-not-use-__attribute__.patch
PATCHFILES += 0004-Make-lt_sockaddr_storage-operator-const-or-compiler-.patch
PATCHFILES += 0005-Fix-const-definition-of-route_dst-or-c-linkage-fails.patch

BUILD_DEP_PKGS += CSWlibpcre-dev
BUILD_DEP_PKGS += CSWlibpcap-dev
BUILD_DEP_PKGS += CSWossldevel

PACKAGES += CSWnmap
SPKG_DESC_CSWnmap = A network exploration tool and security/port scanner
RUNTIME_DEP_PKGS_CSWnmap += CSWstlport
RUNTIME_DEP_PKGS_CSWnmap += CSWlibpcre0
RUNTIME_DEP_PKGS_CSWnmap += CSWlua
RUNTIME_DEP_PKGS_CSWnmap += CSWosslrt
RUNTIME_DEP_PKGS_CSWnmap += CSWlibpcap1

# See standards(5) for details
EXTRA_CPPFLAGS += -features=extensions -D_XOPEN_SOURCE -D_XOPEN_SOURCE_EXTENDED=1 -D__EXTENSIONS__
EXTRA_CXXFLAGS += -features=extensions -D_XOPEN_SOURCE -D_XOPEN_SOURCE_EXTENDED=1 -D__EXTENSIONS__
EXTRA_CXXFLAGS += -library=stlport4

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --with-libpcre=$(prefix)
CONFIGURE_ARGS += --with-libpcap=$(prefix)
CONFIGURE_ARGS += --with-openssl=$(prefix)

# Use included libdnet as it contains many important fixes as described at
#   http://nmap.org/svn/libdnet-stripped/NMAP_MODIFICATIONS
CONFIGURE_ARGS += --with-libdnet=included

#
CONFIGURE_ARGS += --with-liblua=$(prefix)
# CONFIGURE_ARGS += --with-libnbase=
#CONFIGURE_ARGS += --with-libnsock=

# Disable most of the tools for now, enable later one by one
CONFIGURE_ARGS += --without-ndiff
CONFIGURE_ARGS += --without-zenmap
CONFIGURE_ARGS += --without-nping
CONFIGURE_ARGS += --without-ncat

# We can't put this in EXTRA_LINKER_FLAGS as LDFLAGS is used for cc too and -library=stlport4 breaks cc
BUILD_OVERRIDE_VARS = STATIC
BUILD_OVERRIDE_VAR_STATIC = -library=stlport4 -norunpath

# There is no testsuite
TEST_SCRIPTS =

# Tons of docs and identification of programs installed there
CHECKPKG_OVERRIDES_CSWnmap += file-with-bad-content

include gar/category.mk

post-extract-modulated:
	-cd $(WORKSRC) && find . -type d | while read d; do touch $$d/makefile.dep; done
