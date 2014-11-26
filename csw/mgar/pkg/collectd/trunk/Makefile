# $Id$
#
NAME = collectd
VERSION = 5.4.1
GARTYPE = v2

DESCRIPTION = The system statistics collection daemon
define BLURB
collectd gathers statistics about the system it is running on and stores this information. 
Those statistics can then be used to find current performance bottlenecks 
(i.e. performance analysis) and predict future system load (i.e. capacity planning). 
Or if you just want pretty graphs of your private server and are fed up with some 
homegrown solution you're at the right place, too ;).
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
EXTRA_MERGE_EXCLUDE_FILES = .*perllocal\.pod

GARCOMPILER = GNU

CONFIGURE_ARGS += $(DIRPATHS)
CONFIGURE_ARGS += --disable-dns
CONFIGURE_ARGS += --disable-nfs
# CONFIGURE_ARGS += --disable-zfs_arc

PACKAGES += CSWlibcollectdclient1
SPKG_DESC_CSWlibcollectdclient1 += $(DESCRIPTION), libcollectdclient.so.1
PKGFILES_CSWlibcollectdclient1 += $(call baseisadirs,$(libdir),libcollectdclient\.so\.1(\.\d+)*)
RUNTIME_DEP_PKGS_CSWlibcollectdclient1 += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibcollectdclient1 += CSWlibgcrypt20

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
RUNTIME_DEP_PKGS_CSWcollectd += CSWlibltdl7
RUNTIME_DEP_PKGS_CSWcollectd += CSWlibpq5
RUNTIME_DEP_PKGS_CSWcollectd += CSWlibrrd-th4
RUNTIME_DEP_PKGS_CSWcollectd += CSWlibxml2-2
RUNTIME_DEP_PKGS_CSWcollectd += CSWperl
RUNTIME_DEP_PKGS_CSWcollectd += CSWlibxmms1
RUNTIME_DEP_PKGS_CSWcollectd += CSWlibpython2-7-1-0
RUNTIME_DEP_PKGS_CSWcollectd += CSWlibmysqlclient18
RUNTIME_DEP_PKGS_CSWcollectd += CSWlibgcrypt20

RUNTIME_DEP_PKGS_CSWcollectd_sparc += CSWlibintl8
RUNTIME_DEP_PKGS_CSWcollectd_sparc += CSWlibgdk1-2-0
RUNTIME_DEP_PKGS_CSWcollectd_sparc += CSWlibglib1-2-0
RUNTIME_DEP_PKGS_CSWcollectd_sparc += CSWlibgtk1-2-0
RUNTIME_DEP_PKGS_CSWcollectd += $(RUNTIME_DEP_PKGS_CSWcollectd_$(GARCH))

RUNTIME_DEP_PKGS_CSWcollectd_i386 += CSWlibmemcached8 CSWlibfl2
RUNTIME_DEP_PKGS_CSWcollectd += $(RUNTIME_DEP_PKGS_CSWcollectd_$(GARCH))

CHECKPKG_OVERRIDES_CSWcollectd += surplus-dependency|CSWlibgdk1-2-0
CHECKPKG_OVERRIDES_CSWcollectd += surplus-dependency|CSWlibintl8
CHECKPKG_OVERRIDES_CSWcollectd += surplus-dependency|CSWlibglib1-2-0
CHECKPKG_OVERRIDES_CSWcollectd += surplus-dependency|CSWlibgtk1-2-0


INITSMF = $(sysconfdir)/init\.d/collectd

include gar/category.mk

post-install-modulated:
	ginstall -m 755 -d $(DESTDIR)/opt/csw/share/man/man3
	cd $(DESTDIR); gmv -v opt/csw/man/man3/* opt/csw/share/man/man3
	grm -f $(DESTDIR)/opt/csw/lib/perl5/sun4-solaris-thread-multi/perllocal.pod
	grm -f $(DESTDIR)/opt/csw/lib/perl5/i86pc-solaris-thread-multi/perllocal.pod
	rmdir $(DESTDIR)/opt/csw/man/man3
	ginstall -m 755 -d $(DESTDIR)$(sysconfdir)/init.d
	ginstall -m 755 $(WORKDIR)/collectd-init-csw $(DESTDIR)$(sysconfdir)/init.d/collectd
	$(MAKECOOKIE)
