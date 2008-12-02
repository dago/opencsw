GARNAME = synergy
GARVERSION = 1.3.1
CATEGORIES = apps

DESCRIPTION = Software-based TCP/IP "KVM" switch
define BLURB
 Synergy lets you easily share a single mouse and keyboard between multiple
 computers with different operating systems, each with its own display, 
 without special hardware. It's intended for users with multiple computers 
 on their desk since each system uses its own monitor(s). 
endef

MASTER_SITES = $(SF_MIRRORS)
SF_PROJ = $(GARNAME)2
DISTFILES  = synergy-$(GARVERSION).tar.gz
DISTFILES += $(call admfiles,CSWsynergy)

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = synergy-(\d+(?:\.\d+)*).tar.gz

# Adjust code so that it compiles with Sun Studio Compiler
# https://sourceforge.net/tracker/index.php?func=detail&aid=1574331&group_id=59275&atid=490469
PATCHFILES = suncc.diff

# Adjust configure.in to properly use --x-libraries option
# http://sf.net/tracker/index.php?func=detail&aid=2359359&group_id=59275&atid=490469
PATCHFILES += link-xlibs.diff

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --x-includes=/usr/openwin/include
CONFIGURE_ARGS += --x-libraries=/usr/openwin/lib

TEST_SCRIPTS =

# fix missing user write permissions
post-extract:
	@chmod -R u+w $(WORKSRC)
	@$(MAKECOOKIE)

pre-configure:
	cd $(WORKSRC) && autoreconf
	@$(MAKECOOKIE)

post-install:
	@ginstall -d $(DESTDIR)$(sysconfdir)
	@ginstall -m 644 $(WORKSRC)/examples/synergy.conf \
		$(DESTDIR)$(sysconfdir)/synergy.conf.example
	@ginstall -d $(DESTDIR)$(docdir)/images
	@ginstall -m 644 $(WORKSRC)/README $(DESTDIR)$(docdir)
	@ginstall -m 644 $(WORKSRC)/AUTHORS $(DESTDIR)$(docdir)
	@ginstall -m 644 $(WORKSRC)/NEWS $(DESTDIR)$(docdir)
	@ginstall -m 644 $(WORKSRC)/doc/*.html $(DESTDIR)$(docdir)
	@ginstall -m 644 $(WORKSRC)/doc/images/* $(DESTDIR)$(docdir)/images
	@$(MAKECOOKIE)

include gar/category.mk
