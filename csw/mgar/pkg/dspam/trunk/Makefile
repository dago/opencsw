# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = dspam
VERSION = 3.10.2
GARTYPE = v2

DESCRIPTION = Antispam Filter
define BLURB
  DSPAM is an adaptive spam filter which means it is capable of learning and adapting to each user's email. Instead of working off of a list of "rules" to identify spam, DSPAM's probabilistic engine examines the content of each message and learns what type of content the user deems as spam (or nonspam). 
endef

MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(DISTNAME).tar.gz
LICENSE = LICENSE

REINPLACE_USRLOCAL += src/config.h

PACKAGES += CSWlibdspam7
CATALOGNAME_CSWlibdspam7 = libdspam7
PKGFILES_CSWlibdspam7 += $(call baseisadirs,$(libdir),libdspam\.so\.7\.0\.0)
PKGFILES_CSWlibdspam7 += $(call baseisadirs,$(libdir),libdspam\.so\.7(\.\d+)*)
SPKG_DESC_CSWlibdspam7 += $(DESCRIPTION), libdspam.so.7

PACKAGES += CSWdspam
SPKG_DESC_CSWdspam += $(DESCRIPTION), tools
RUNTIME_DEP_PKGS_CSWdspam += CSWlibdspam7
CHECKPKG_OVERRIDES_CSWdspam += file-with-bad-content|/usr/local|root/etc/opt/csw/dspam.conf

PACKAGES += CSWdspam-dev
CATALOGNAME_CSWdspam-dev = dspam_dev
SPKG_DESC_CSWdspam-dev += $(DESCRIPTION), development files
PKGFILES_CSWdspam-dev += $(PKGFILES_DEVEL)
RUNTIME_DEP_PKGS_CSWdspam-dev += CSWlibdspam7

USERGROUP = /etc/opt/csw/pkg/CSWdspam/cswusergroup

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --with-dspam-home=$(localstatedir)/dspam
CONFIGURE_ARGS += --enable-daemon
CONFIGURE_ARGS += --enable-split-configuration
CONFIGURE_ARGS += --enable-syslog
CONFIGURE_ARGS += --enable-clamav
CONFIGURE_ARGS += --enable-preferences-extension
CONFIGURE_ARGS += --enable-domain-scale
CONFIGURE_ARGS += --with-dspam-home-owner=dspam
CONFIGURE_ARGS += --with-dspam-home-group=dspam
CONFIGURE_ARGS += --with-dspam-owner=dspam
CONFIGURE_ARGS += --with-dspam-group=dspam
CONFIGURE_ARGS += --with-storage-driver=hash_drv,pgsql_drvmysql_drv
CONFIGURE_ARGS += --enable-long-usernames
CONFIGURE_ARGS += --enable-virtual-users

include gar/category.mk

post-install:
	ginstall -d $(DESTDIR)$(docdir)/$(NAME)
	ginstall -m 444 $(WORKSRC)/RELEASE.NOTES $(DESTDIR)$(docdir)/$(NAME)
	ginstall -m 444 $(WORKSRC)/README $(DESTDIR)$(docdir)/$(NAME)
	ginstall -m 444 $(WORKSRC)/UPGRADING $(DESTDIR)$(docdir)/$(NAME)
	ginstall -d $(DESTDIR)$(sysconfdir)/pkg/CSWdspam/cswusergroup
	ginstall -m 644 $(FILEDIR)/CSWdspam.cswusergroup $(DESTDIR)$(sysconfdir)/pkg/CSWdspam/cswusergroup
	@$(MAKECOOKIE)
