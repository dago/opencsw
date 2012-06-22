# TBD:
# - SMF manifest missing
# - user and group for icecast server, make config in icecast.xml

NAME = icecast
VERSION = 2.3.3
CATEGORIES = apps

DESCRIPTION = A free server software for streaming multimedia
define BLURB
endef

MASTER_SITES = http://downloads.xiph.org/releases/icecast/
DISTFILES += $(NAME)-$(VERSION).tar.gz

VENDOR_URL = http://www.icecast.org/

PACKAGING_PLATFORMS = solaris10-sparc solaris10-i386

PACKAGES += CSWicecast
SPKG_DESC_CSWicecast = A free server software for streaming multimedia
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWicecast += CSWlibiconv2
RUNTIME_DEP_PKGS_CSWicecast += CSWlibssl1-0-0
RUNTIME_DEP_PKGS_CSWicecast += CSWlibz1
RUNTIME_DEP_PKGS_CSWicecast += CSWlibogg0
RUNTIME_DEP_PKGS_CSWicecast += CSWlibcurl4
RUNTIME_DEP_PKGS_CSWicecast += CSWlibidn11
RUNTIME_DEP_PKGS_CSWicecast += CSWlibvorbis0
RUNTIME_DEP_PKGS_CSWicecast += CSWlibxslt1
RUNTIME_DEP_PKGS_CSWicecast += CSWlibxml2-2
RUNTIME_DEP_PKGS_CSWicecast += CSWliboggkate1
RUNTIME_DEP_PKGS_CSWicecast += CSWlibtheora0
RUNTIME_DEP_PKGS_CSWicecast += CSWlibspeex1
RUNTIME_DEP_PKGS_CSWicecast += CSWlibkate1


# These are just docs, override for now
CHECKPKG_OVERRIDES_CSWicecast += file-with-bad-content|/usr/local|root/opt/csw/share/doc/icecast/index.html
CHECKPKG_OVERRIDES_CSWicecast += file-with-bad-content|/usr/local|root/opt/csw/share/doc/icecast/README

REINPLACEMENTS += cfglogs
REINPLACE_MATCH_cfglogs = /usr/local/icecast/logs
REINPLACE_WITH_cfglogs = $(localstatedir)/log/icecast
REINPLACE_FILES_cfglogs += src/cfgfile.c

REINPLACEMENTS += cfgadmin
REINPLACE_MATCH_cfgadmin = /usr/local/icecast/admin
REINPLACE_WITH_cfgadmin = $(sharedstatedir)/icecast/admin
REINPLACE_FILES_cfgadmin += src/cfgfile.c

REINPLACEMENTS += cfgweb
REINPLACE_MATCH_cfgweb = /usr/local/icecast/webroot
REINPLACE_WITH_cfgweb = $(sharedstatedir)/icecast/web
REINPLACE_FILES_cfgweb += src/cfgfile.c

REINPLACEMENTS += cfg
REINPLACE_MATCH_cfg = /usr/local/icecast
REINPLACE_WITH_cfg = $(sharedstatedir)/icecast
REINPLACE_FILES_cfg += src/cfgfile.c

PRESERVECONF = $(sysconfdir)/icecast.xml

# CSWicecast_usergroup = icecast:icecast:Icecast Server:/var/opt/csw/log/icecast:

include gar/category.mk

post-install-modulated:
	@ginstall -d $(DESTDIR)$(localstatedir)/log/icecast
