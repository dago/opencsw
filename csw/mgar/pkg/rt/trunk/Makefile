# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = rt
VERSION = 4.2.0
GARTYPE = v2

DESCRIPTION = RT: Request Tracker, an enterprise-grade issue tracking system.
define BLURB
  RT is an enterprise-grade issue tracking system. It allows organizations
to keep track of what needs to get done, who is working on which tasks,
what's already been done, and when tasks were (or weren't) completed.
endef

GARCOMPILER = GCC4

VENDOR_URL = http://bestpractical.com/rt/
MASTER_SITES = http://download.bestpractical.com/pub/rt/release/
DISTFILES  = $(DISTNAME).tar.gz
DISTFILES += cswusergroup

USERGROUP = $(sysconfdir)/pkg/CSW$(NAME)/cswusergroup

BUILD_DEP_PKGS += CSWgraphviz-dev
BUILD_DEP_PKGS += CSWlibgd-dev
BUILD_DEP_PKGS += CSWpmcryptblowfish
BUILD_DEP_PKGS += CSWpmfcgi
BUILD_DEP_PKGS += CSWpmhtmlscrubber
BUILD_DEP_PKGS += CSWpmmimetypes
BUILD_DEP_PKGS += CSWpmperlioeol
BUILD_DEP_PKGS += CSWpmregexpcommon
BUILD_DEP_PKGS += CSWpmtextwikiformat
BUILD_DEP_PKGS += CSWpmtextwrapper
BUILD_DEP_PKGS += CSWpmtreesimple
BUILD_DEP_PKGS += CSWpmxmlrssø
BUILD_DEP_PKGS += CSWpm-cgi-emulate-psgi
BUILD_DEP_PKGS += CSWpm-css-squish
BUILD_DEP_PKGS += CSWpm-devel-stacktrace
BUILD_DEP_PKGS += CSWpm-devel-globaldestruction
BUILD_DEP_PKGS += CSWpm-datetime
BUILD_DEP_PKGS += CSWpm-dbd-mysql
BUILD_DEP_PKGS += CSWpm-dbi
BUILD_DEP_PKGS += CSWpm-dbix-searchbuilder
BUILD_DEP_PKGS += CSWpm-email-address
BUILD_DEP_PKGS += CSWpm-gd
BUILD_DEP_PKGS += CSWpm-html-format
BUILD_DEP_PKGS += CSWpm-ipc-run
BUILD_DEP_PKGS += CSWpm-ipc-run3
BUILD_DEP_PKGS += CSWpm-json
BUILD_DEP_PKGS += CSWpm-log-dispatch
BUILD_DEP_PKGS += CSWpm-lwp-protocol-https
BUILD_DEP_PKGS += CSWpm-mime-tools
BUILD_DEP_PKGS += CSWpm-module-refresh
BUILD_DEP_PKGS += CSWpm-net-cidr
BUILD_DEP_PKGS += CSWpm-plack
BUILD_DEP_PKGS += CSWpm-text-template
BUILD_DEP_PKGS += CSWpm-universal-require

PACKAGES += CSWrt
SPKG_DESC_CSWrt = $(DESCRIPTION)
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWrt += CSWperl

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --enable-graphviz
CONFIGURE_ARGS += --enable-gd
CONFIGURE_ARGS += --enable-gpg
CONFIGURE_ARGS += --enable-smime
CONFIGURE_ARGS += --with-web-user=webservd
CONFIGURE_ARGS += --with-web-group=webservd
CONFIGURE_ARGS += --with-rt-group=rt

include gar/category.mk

TEST_TARGET = test

post-merge:
	ginstall -m 644 $(FILEDIR)/cswusergroup \
		$(PKGROOT)$(sysconfdir)/pkg/CSW$(NAME)

