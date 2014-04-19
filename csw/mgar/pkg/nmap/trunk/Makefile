NAME = nmap
VERSION = 6.45
GARTYPE = v2
GARCOMPILER = GCC46 solaris10-sparc

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

MASTER_SITES = http://nmap.org = $(NAME)-$(VERSION).tar.bz2
# Those files are taken from FreeBSD 10.0 and stripped off some #ifdef WHATEVER where necessary.
DISTFILES += file.h asprintf.c vasprintf.c

PATCHFILES += 0000-Add-vasprintf-compatibility.patch
PATCHFILES += 0000-Add-python2.6-site-packages-gtk-2.0-to-python-path-i.patch

BUILD_DEP_PKGS += CSWlibpcre-dev
BUILD_DEP_PKGS += CSWlibpcap-dev
BUILD_DEP_PKGS += CSWlibssl-dev
BUILD_DEP_PKGS += CSWlibasprintf0S += CSWossldevel

PACKAGES += CSWnmap
SPKG_DESC_CSWnmap = A network exploration tool and security/port scanner
RUNTIME_DEP_PKlibpcre1
RUNTIME_DEP_PKGS_CSWnmap += CSWlibssl1-0-0nmap += CSWosslrt
RUNTIME_DEP_PKGS_CSWnmap += CSWlibpcap1
RUNTIME_DEP_PKGibstdc++6
RUNTIME_DEP_PKGS_CSWnmap += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWnmap += CSWliblua5-2
RUNTIME_DEP_PKGS_CSWnmap += CSWpython
CHECKPKG_OVERRIDES_CSWnmap += surplus-dependency|CSWpython

PACKAGES += CSWzenmap
SPKG_DESC_CSWzenmap = zenmap
ARCHALL_CSWzenmap = 1
PKGFILES_CSWzenmap += $(bindir)/zenmap
PKGFILES_CSWzenmap += $(bindir)/nmapfe
PKGFILES_CSWzenmap += $(bindir)/xnmap
PKGFILES_CSWzenmap += $(libdir)/python.*
PKGFILES_CSWzenmap += $(mandir)/.*/zenmap\.1
PKGFILES_CSWzenmap += $(sharedstatedir)/zenmap/.*
# For Zenmap
RUNTIME_DEP_PKGS_CSWzenmap += CSWnmap
RUNTIME_DEP_PKGS_CSWzenmap += CSWpy-gtk
RUNTIME_DEP_PKGS_CSWzenmap += CSWpy-gobject-CHECKPKG_OVERRIDES_CSWzenmap += surplus-dependency|CSWnmap
CHECKPKG_OVERRIDES_CSWzenmap += catalogname-does-not-start-with-py_
CHECKPKG_OVERRIDES_CSWzenmap += pkgname-does-not-start-with-CSWpy-
CHECKPKG_OVERRIDES_CSWzenmap += pkginfo-description-not-starting-with-uppercase|zenmap
CHECKPKG_OVERRIDES_CSWzenmap += file-with-bad-content|/usr/local|root/opt/csw/lib/python2.6/site-packages/zenmapCore/Paths.py
CHECKPKG_OVERRIDES_CSWzenmap += file-with-bad-content|/usr/share|root/opt/csw/lib/python2.6/site-packages/zenmapCore/NmapParser.py-library=stlport4

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --with-libpcre=$(prefix)
CONFIGURE_ARGS += --with-libpcap=$(prefix)
CONFIGURE_ARGS += --with-opCONFIGURE_ARGS += $(CONFIGURE_ARGS_$(GAROSREL)-openssl=$(prefix)

# Use included libdnet as it contains many important fixes as described at
#   http://nmap.org/svn/libdnet-stripped/NMAP_MODIFICATIONS
CONFIGURE_ARGS += --with-lCONFIGURE_ARGS += --with-liblua=$(prefix) --wt4 -norunpath

# There is no testsuite
TEST_SCRIPTS =

PYCOMPILE = 1

EXTRA_MERGE_EXCLUDE_FILES += $(bindir)/uninstall_zenmap
EXTRA_PAX_ARGS += -s ',/ndifinclude gar/category.mk

pre-configure:
	ginstall $(WORKDIR)/asprintf.c $(WORKSRC)/nsock/src
	ginstall $(WORKDIR)/vasprintf.c $(WORKSRC)/nsock/src
	ginstall $(WORKDIR)/file.h $(WORKSRC)/nsock/src
	@$(MAKECOOKIE)

post-configure:
# it happens, that this define isn't set due to missing /dev/ip in solaris zones.
	gsed -i -e 's;^/\* #undef HAVE_STREAMS_MIB2 \*/;#define HAVE_STREAMS_MIB2 1;' $(WORKSRC)/libdnet-stripped/include/config.h
	@$(MAKECOOKIE)
