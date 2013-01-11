# $Id$
#
NAME = collectd
VERSION = 5.2.0
GARTYPE = v2

DESCRIPTION = Collects sistema performance statistics periodically
define BLURB
endef

MASTER_SITES = http://collectd.org/files/
DISTFILES  = $(DISTNAME).tar.gz
DISTFILES += collectd-init-csw

PACKAGING_PLATFORMS = solaris10-sparc solaris10-i386
VENDOR_URL = http://collectd.org/

# PATCHFILES += 0001-work-around-the-s_addr-macro.patch

BUILD64 = 1

BUILD_DEP_PKGS += CSWlibgcrypt-dev
EXTRA_CPPFLAGS = -DSOLARIS2=10 -D__EXTENSIONS__
EXTRA_LINKER_FLAGS = -R/opt/csw/lib/collectd -R/usr/openwin/lib -lrt

GARCOMPILER = GNU

CONFIGURE_ARGS += $(DIRPATHS)
CONFIGURE_ARGS += --disable-dns
CONFIGURE_ARGS += --disable-nfs
CONFIGURE_ARGS += --disable-zfs_arc

PACKAGES += CSWlibcollectdclient1
PKGFILES_CSWlibcollectdclient1 += $(call baseisadirs,$(libdir),libcollectdclient\.so\.1(\.\d+)*)
SPKG_DESC_CSWlibcollectdclient1 += $(DESCRIPTION), libcollectdclient.so.1
RUNTIME_DEP_PKGS_CSWlibcollectdclient1 += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibcollectdclient1 += CSWlibgcrypt11

PACKAGES += CSWcollectd-dev
CATALOGNAME_CSWcollectd-dev = collectd_dev
SPKG_DESC_CSWcollectd-dev += $(DESCRIPTION), development files
PKGFILES_CSWcollectd-dev += $(PKGFILES_DEVEL)
RUNTIME_DEP_PKGS_CSWcollectd-dev += CSWlibcollectdclient1

PACKAGES += CSWcollectd
SPKG_DESC_CSWcollectd += $(DESCRIPTION)

RUNTIME_DEP_PKGS_CSWcollectd += CSWlibcollectdclient1
RUNTIME_DEP_PKGS_CSWcollectd += CSWlibcurl4
RUNTIME_DEP_PKGS_CSWcollectd += CSWlibdbi1
RUNTIME_DEP_PKGS_CSWcollectd += CSWlibganglia0
RUNTIME_DEP_PKGS_CSWcollectd += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWcollectd += CSWlibgcrypt11
RUNTIME_DEP_PKGS_CSWcollectd += CSWlibltdl7
RUNTIME_DEP_PKGS_CSWcollectd += CSWlibpq5
RUNTIME_DEP_PKGS_CSWcollectd += CSWlibpython2-6-1-0
RUNTIME_DEP_PKGS_CSWcollectd += CSWlibrrd-th4
RUNTIME_DEP_PKGS_CSWcollectd += CSWlibstatgrab6
RUNTIME_DEP_PKGS_CSWcollectd += CSWlibxml2-2
RUNTIME_DEP_PKGS_CSWcollectd += CSWperl

CHECKPKG_OVERRIDES_CSWcollectd += file-with-bad-content|/usr/share|root/opt/csw/share/man/man1/collectd.1
CHECKPKG_OVERRIDES_CSWcollectd += file-with-bad-content|/usr/share|root/opt/csw/share/man/man5/collectd-unixsock.5

INITSMF = $(sysconfdir)/init\.d/collectd

include gar/category.mk

post-install-modulated:
	ginstall -m 755 -d $(DESTDIR)/opt/csw/share/man/man3
	cd $(DESTDIR); gmv -v opt/csw/man/man3/* opt/csw/share/man/man3
	grm -f $(DESTDIR)/opt/csw/lib/perl5/sun4-solaris-thread-multi/perllocal.pod
	rmdir $(DESTDIR)/opt/csw/man/man3
	ginstall -m 755 -d $(DESTDIR)$(sysconfdir)/init.d
	ginstall -m 755 $(WORKDIR)/collectd-init-csw $(DESTDIR)$(sysconfdir)/init.d/collectd
	$(MAKECOOKIE)
