# $Id$
#
NAME = collectd
VERSION = 5.1.0
GARTYPE = v2
CATEGORIES = server

DESCRIPTION = Collects sistema performance statistics periodically
define BLURB
endef

MASTER_SITES = http://collectd.org/files/
DISTFILES  = $(DISTNAME).tar.gz

PACKAGING_PLATFORMS = solaris10-sparc solaris10-i386
VENDOR_URL = http://collectd.org/

PATCHFILES += 0001-work-around-the-s_addr-macro.patch

BUILD_DEP_PKGS += CSWlibgcrypt-dev
EXTRA_CPPFLAGS = -DSOLARIS2=10 -D__EXTENSIONS__

GARCOMPILER = GNU

CONFIGURE_ARGS += $(DIRPATHS)
CONFIGURE_ARGS += --disable-dns
CONFIGURE_ARGS += --disable-nfs
CONFIGURE_ARGS += --disable-zfs_arc

PACKAGES += CSWlibcollectdclient0
PKGFILES_CSWlibcollectdclient0 += $(call baseisadirs,$(libdir),libcollectdclient\.so\.0(\.\d+)*)
SPKG_DESC_CSWlibcollectdclient0 += $(DESCRIPTION), libcollectdclient.so.0
RUNTIME_DEP_PKGS_CSWcollectd += CSWlibcollectdclient0
RUNTIME_DEP_PKGS_CSWlibcollectdclient0 += CSWlibgcc-s1

PACKAGES += CSWcollectd
SPKG_DESC_CSWcollectd += $(DESCRIPTION)

RUNTIME_DEP_PKGS_CSWcollectd += CSWlibltdl7
RUNTIME_DEP_PKGS_CSWcollectd += CSWlibdbi1
RUNTIME_DEP_PKGS_CSWcollectd += CSWlibssl1-0-0
RUNTIME_DEP_PKGS_CSWcollectd += CSWlibz1
RUNTIME_DEP_PKGS_CSWcollectd += CSWlibrrd-th4
RUNTIME_DEP_PKGS_CSWcollectd += CSWlibgpg-error0
RUNTIME_DEP_PKGS_CSWcollectd += CSWlibcurl4
RUNTIME_DEP_PKGS_CSWcollectd += CSWlibgcrypt11
RUNTIME_DEP_PKGS_CSWcollectd += CSWlibstatgrab6
RUNTIME_DEP_PKGS_CSWcollectd += CSWlibpython2-6-1-0
RUNTIME_DEP_PKGS_CSWcollectd += CSWlibxml2-2
RUNTIME_DEP_PKGS_CSWcollectd += CSWperl
RUNTIME_DEP_PKGS_CSWcollectd += CSWlibganglia0
RUNTIME_DEP_PKGS_CSWcollectd += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWcollectd += CSWlibidn11
RUNTIME_DEP_PKGS_CSWcollectd += CSWlibpq5

CHECKPKG_OVERRIDES_CSWcollectd += file-with-bad-content|/usr/share|root/opt/csw/share/man/man1/collectd.1
CHECKPKG_OVERRIDES_CSWcollectd += file-with-bad-content|/usr/share|root/opt/csw/share/man/man5/collectd-unixsock.5

include gar/category.mk

post-install-modulated:
	ginstall -m 755 -d $(DESTDIR)/opt/csw/share/man/man3
	cd $(DESTDIR); gmv -v opt/csw/man/man3/* opt/csw/share/man/man3
	rmdir $(DESTDIR)/opt/csw/man/man3
	grm -v $(DESTDIR)/opt/csw/lib/perl/*/perllocal.pod
	$(MAKECOOKIE)
