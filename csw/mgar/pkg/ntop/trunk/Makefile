NAME = ntop
VERSION = 4.0.3
CATEGORIES = net

DESCRIPTION = A network traffic usage monitor
define BLURB
  ntop is a network probe that shows network usage in a way similar to what top
  does for processes. In interactive mode, it displays the network status on the
  user's terminal. In Web mode, it acts as a Web server, creating an HTML dump
  of the network status. It sports a NetFlow/sFlow emitter/collector, an
  HTTP-based client interface for creating ntop-centric monitoring applications,
  and RRD for persistently storing traffic statistics.
endef

MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(NAME)-$(VERSION).tgz

DISTFILES  += cswntop
EXPANDVARS += cswntop
DISTFILES  += ntop.conf.CSW
EXPANDVARS += ntop.conf.CSW
DISTFILES  += CSWntop.postinstall CSWntop.postremove CSWntop.request
DISTFILES  += cswreleasemgr

INITSMF = /etc/opt/csw/init.d/cswntop

PATCHFILES  = 0001-Fix-misplaced-endif.patch
PATCHFILES += 0002-Do-not-redeclare-__builtin_alloca.patch
PATCHFILES += 0003-Check-for-uint_-in-addition-to-u_int_.patch
PATCHFILES += 0004-Strip-default-Solaris-library-pathes-as-we-set-our-o.patch
PATCHFILES += 0005-Change-default-PID-file-location-to-var-opt-csw-ntop.patch
PATCHFILES += 0006-Temporary-Fix-for-Broken-sourceforge-CVS-access.patch
PATCHFILES += 0007-Update-defaults-from-usr-local-to-opt-csw-etc-opt-cs.patch

# We define upstream file regex so we can be notifed of new upstream software release
UPSTREAM_MASTER_SITES = $(SF_PROJECT_SHOWFILE)=17233
UPSTREAM_USE_SF = 1
UFILES_REGEX = (\d+(?:\.\d+)*)

RUNTIME_DEP_PKGS_CSWntop += CSWlibpython2-6-1-0
RUNTIME_DEP_PKGS_CSWntop += CSWlibpcap
RUNTIME_DEP_PKGS_CSWntop += CSWosslrt
RUNTIME_DEP_PKGS_CSWntop += CSWrrd
RUNTIME_DEP_PKGS_CSWntop += CSWgeoip
RUNTIME_DEP_PKGS_CSWntop += CSWpython
RUNTIME_DEP_PKGS_CSWntop += CSWlibgdbm3
RUNTIME_DEP_PKGS_CSWntop += CSWzlib
RUNTIME_DEP_PKGS_CSWntop += CSWiconv

## Following package enables optional functionality
#RUNTIME_DEP_PKGS_CSWntop += CSWgraphviz
#CHECKPKG_OVERRIDES_CSWntop += surplus-dependency|CSWgraphviz

BUILD_DEP_PKGS = $(RUNTIME_DEP_PKGS_CSWntop)
BUILD_DEP_PKGS += CSWlibtool CSWautoconf CSWautomake
BUILD_DEP_PKGS += CSWlibpcapdevel CSWossldevel
BUILD_DEP_PKGS += CSWlibgdbm-dev

CONFIGURE_SCRIPTS = $(WORKSRC)/autogen.sh

sysconfdir = /etc/opt/csw
localstatedir = /var/opt/csw

PRESERVECONF = $(sysconfdir)/ntop.conf

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --with-gdbm-lib=/opt/csw/lib
CONFIGURE_ARGS += --with-gdbm-include=/opt/csw/include
CONFIGURE_ARGS += --with-zlib-lib=/opt/csw/lib
CONFIGURE_ARGS += --with-zlib-include=/opt/csw/include
CONFIGURE_ARGS += --with-ossl-lib=/opt/csw/lib
CONFIGURE_ARGS += --with-ossl-include=/opt/csw/include
CONFIGURE_ARGS += --enable-jumbo-frames
# CONFIGURE_ARGS += --enable-fc
# CONFIGURE_ARGS += --enable-mysql

# We don't have a separate devel-package, so this is ok
CHECKPKG_OVERRIDES_CSWntop += shared-lib-package-contains-so-symlink|file=/opt/csw/lib/libcpacketPlugin.so
CHECKPKG_OVERRIDES_CSWntop += shared-lib-package-contains-so-symlink|file=/opt/csw/lib/libicmpPlugin.so
CHECKPKG_OVERRIDES_CSWntop += shared-lib-package-contains-so-symlink|file=/opt/csw/lib/libnetflowPlugin.so
CHECKPKG_OVERRIDES_CSWntop += shared-lib-package-contains-so-symlink|file=/opt/csw/lib/libntop.so
CHECKPKG_OVERRIDES_CSWntop += shared-lib-package-contains-so-symlink|file=/opt/csw/lib/libntopreport.so
CHECKPKG_OVERRIDES_CSWntop += shared-lib-package-contains-so-symlink|file=/opt/csw/lib/librrdPlugin.so
CHECKPKG_OVERRIDES_CSWntop += shared-lib-package-contains-so-symlink|file=/opt/csw/lib/libsflowPlugin.so

# Upstream has chosen it that way...
CHECKPKG_OVERRIDES_CSWntop += soname-not-part-of-filename|soname=libcpacketPlugin-4.0.3.so|filename=cpacketPlugin.so
CHECKPKG_OVERRIDES_CSWntop += soname-not-part-of-filename|soname=libicmpPlugin-4.0.3.so|filename=icmpPlugin.so
CHECKPKG_OVERRIDES_CSWntop += soname-not-part-of-filename|soname=libnetflowPlugin-4.0.3.so|filename=netflowPlugin.so
CHECKPKG_OVERRIDES_CSWntop += soname-not-part-of-filename|soname=librrdPlugin-4.0.3.so|filename=rrdPlugin.so
CHECKPKG_OVERRIDES_CSWntop += soname-not-part-of-filename|soname=libsflowPlugin-4.0.3.so|filename=sflowPlugin.so
#CHECKPKG_OVERRIDES_CSWntop += shared-lib-pkgname-mismatch|sonames=['libcpacketPlugin-4.0.3.so',|'libicmpPlugin-4.0.3.so',|'libnetflowPlugin-4.0.3.so',|'libntop-4.0.3.so',|'libntopreport-4.0.3.so',|'librrdPlugin-4.0.3.so',|'libsflowPlugin-4.0.3.so']|pkgname=CSWntop|expected=['CSWlib4-0-3']|
CHECKPKG_OVERRIDES_CSWntop += shared-lib-pkgname-mismatch

# Bad content files - Documentation
CHECKPKG_OVERRIDES_CSWntop += file-with-bad-content|/usr/local|root/opt/csw/share/ntop/html/faq.html
CHECKPKG_OVERRIDES_CSWntop += file-with-bad-content|/usr/share|root/opt/csw/share/ntop/html/faq.html
CHECKPKG_OVERRIDES_CSWntop += file-with-bad-content|/usr/local|root/opt/csw/share/ntop/html/ntop.html
CHECKPKG_OVERRIDES_CSWntop += file-with-bad-content|/usr/local|root/opt/csw/share/man/man8/ntop.8

# Bad content files - Shared libraries (Captured Build Info for Version Output)
CHECKPKG_OVERRIDES_CSWntop += file-with-bad-content|/usr/local|root/opt/csw/lib/libicmpPlugin-4.0.3.so
CHECKPKG_OVERRIDES_CSWntop += file-with-bad-content|/usr/local|root/opt/csw/lib/libsflowPlugin-4.0.3.so
CHECKPKG_OVERRIDES_CSWntop += file-with-bad-content|/usr/local|root/opt/csw/lib/libntop-4.0.3.so
CHECKPKG_OVERRIDES_CSWntop += file-with-bad-content|/usr/local|root/opt/csw/lib/libntopreport-4.0.3.so
CHECKPKG_OVERRIDES_CSWntop += file-with-bad-content|/usr/local|root/opt/csw/lib/libnetflowPlugin-4.0.3.so
CHECKPKG_OVERRIDES_CSWntop += file-with-bad-content|/usr/local|root/opt/csw/lib/librrdPlugin-4.0.3.so
CHECKPKG_OVERRIDES_CSWntop += file-with-bad-content|/usr/local|root/opt/csw/lib/libcpacketPlugin-4.0.3.so
CHECKPKG_OVERRIDES_CSWntop += file-with-bad-content|/usr/local|root/opt/csw/lib/ntop/plugins/sflowPlugin.so
CHECKPKG_OVERRIDES_CSWntop += file-with-bad-content|/usr/local|root/opt/csw/lib/ntop/plugins/cpacketPlugin.so
CHECKPKG_OVERRIDES_CSWntop += file-with-bad-content|/usr/local|root/opt/csw/lib/ntop/plugins/rrdPlugin.so
CHECKPKG_OVERRIDES_CSWntop += file-with-bad-content|/usr/local|root/opt/csw/lib/ntop/plugins/netflowPlugin.so
CHECKPKG_OVERRIDES_CSWntop += file-with-bad-content|/usr/local|root/opt/csw/lib/ntop/plugins/icmpPlugin.so

include gar/category.mk

pre-configure-modulated:
	@# This brainded autogen.sh script search in /usr and /usr/local *only*
	cp /opt/csw/share/aclocal/libtool.m4 $(WORKSRC)/libtool.m4.in
	@$(MAKECOOKIE)

post-install-modulated:
	ginstall -d $(DESTDIR)/etc/opt/csw/init.d
	ginstall $(WORKDIR)/cswntop $(DESTDIR)/etc/opt/csw/init.d/cswntop
	ginstall $(WORKDIR)/ntop.conf.CSW $(DESTDIR)$(sysconfdir)/ntop/ntop.conf.CSW
	@$(MAKECOOKIE)
