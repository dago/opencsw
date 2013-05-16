NAME = leafnode
VERSION = 1.11.8
CATEGORIES = apps
GARTYPE = v2

DESCRIPTION = An NNTP server for small leaf sites
define BLURB
endef

MASTER_SITES = $(SF_M+= $(DISTNAME).tar.xz$(VERSION).tar.bz2

UPSTREAM_MASTER_SITES = $(SF_PROJECT_SHOWFILE)=57767
UPSTREAM_USE_SF = 1
UFILES_REGEX = (\d+(?:\.\d+)*)_CSWleafnode += CSWlibpcre1

BUILD64 = 1
ISAEXEC = 1
CONFIGURE_ARGS = $(DIRPATHS)

sysconfdir = /etc$(prefix)/leafnode

EXTRA_MERGE_EXCLUDE_FILES += $(sysconfdir)/Makefile.dist
EXTRA_MERGE_EXCLUDE_FILES += $(sysconfdir)/UNINSTALL-daemontools
EXTRA_MERGE_EXCLUDE_FILES += $(sysconfdir)/run.tcpd.dist
EXTRA_MERGE_EXCLUDE_FILES += $(sysconfdir)/run.tcpserver.dist

PRESERVECONF += $(sysconfdir)/config
PRESERVECONF += $(sysconfdir)/filters
PRESERVECONF += $(sysconfdir)/nntp.rules

include gar/category.mk

post-install:
	cd $(DESTDIR)$(sysconfdir) && mv config.example config
	cd $(DESTDIR)$(sysconfdir) && mv filters.example filters
	cd $(DESTDIR)$(sysconfdir) && mv nntp.rules.dist nntp.rules
	@$(MAKECOOKIE)
