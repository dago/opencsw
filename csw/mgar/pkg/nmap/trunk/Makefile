NAME = nmap
VERSION = 6.01
GARTYPE = v26 solaris10-sparc

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
DISTFILES = $(NAME)-$(Vgsvn.patch.patch

BUILD_DEP_PKGS += CSWlibpcre-dev
BUILD_DEP_PKGS += CSWlibpcap-dev
BUILlibssl-devS += CSWossldevel

PACKAGES += CSWnmap
SPKG_DESC_CSWnmap = A network exploration tool and security/port scanner
RUNTIME_DEP_PKlibpcre0
RUNTIME_DEP_PKGS_CSWnmap += CSWlibssl1-0-0nmap += CSWosslrt
RUNTIME_DEP_PKGS_CSWnmap += CSWlibpcap1
RUNTIME_DEP_PKGS_CSWnmap += CSWlua
RUNTIME_DEP_PKGS_CSWnmap += CSWpython
# For Zenmap
RUNTIME_DEP_PKGS_CSWnmap += CSWpygtk

# Tons of docs and identification of programs installed there
CHECKPKG_OVERRIDES_CSWnmap += file-with-bad-content

# The Python module is really embedded here, that is ok
CHECKPKG_OVERRIDES_CSWnmap += pkgname-does-not-start-with-CSWpy-
CHECKPKG_OVERRIDES_CSWnmap += catalogname-does-not-start-with-py_

#PACKAGES += CSWzenmap
SPKG_DESC_CSWzenmap = zenmap
PKGFILES_CSWzenmap += $(bindir)/zenmap
PKGFILES_CSWzenmap += $(libdir)/python/.*
PKGFILES_CSWzenmap += $(mandir)/.*/zenmap\.1
PKGFILES_CSWzenmap += $(sharedstat
# See standards(5) for details
# we disable this (for) now, because we're switching the compiler to GCC4
#s(5) for details
EXTRA_CPPFLAGS += -features=extensions -D_XOPEN_SOURCE -D_XOPEN_SOURCE_EXTENDED=1 #EXTRA_CXXdetails
EXTRA_CPPFLAGS += -features=extensions -D_XOPEN_SOURCE -D_XOPEN_SOURCE_EXTENDED=1 #-D__EXTENSIONS__
EXTRA_CXXFLAGS += -library=stlport4

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --with-libpcre=$(prefix)
CONFIGURE_ARGS += --with-libpcap=$(prefix)
CONFIGURE_ARGS += --with-opCONFIGURE_ARGS += $(CONFIGURE_ARGS_$(GAROSREL)-openssl=$(prefix)

# Use included libdnet as it contains many important fixes as described at
#   http://nmap.org/svn/libdnet-stripped/NMAP_MODIFICATIONS
CONFIGURE_ARGS += --with-libdnet=included

CONFIGURE_ARGS += --with-liblua=$(prefix)

# Not necessary
# CONFIGURE_ARGS += --with-libnbase=
# CONFIGURE_ARGS += --wt4 -norunpath

# There is no testsuite
TEST_SCRIPTS =

PYCOMPILE = 1

EXTRA_MERGE_EXCLUDE_FILES += $(bindir)/uninstall_zenmap
EXTRA_PAX_ARGS += -s ',/ndif
GARCOMPILER = GCC4iff,/nmap-ndiff,'

include #post-extract-modulated:
#tract-modulated:
	-cd $(WORKSRC) && find . -type d | while read d; do touch $$d/ma