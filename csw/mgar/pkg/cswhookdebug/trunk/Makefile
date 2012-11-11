# $Id$
NAME = cswhookdebug
VERSION = 1.0
GARTYPE = v2

DESCRIPTION = A set of hooks to ease debugging hook callers
define BLURB
These hooks simply dump the hook name and arguments with ansi colours
to make the calling sequence visible during a package maintenance action.
endef

VENDOR_URL = http://opencsw.org
MASTER_SITES = 
DISTFILES  =
ARCHALL = 1

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS =
TEST_SCRIPTS =
INSTALL_SCRIPTS = custom

include gar/category.mk

post-extract-modulated: $(WORKSRC)
	cp $(FILEDIR)/gpl-3.0.txt $(WORKSRC)/COPYING

HOOKDIR=$(DESTDIR)/etc/opt/csw/pkg-hooks
HOOKS  = postinstall postupgrade postremove
HOOKS += preupgrade preinstall preremove
HOOKS += prebatchupgrade prebatchinstall prebatchremove
HOOKS += postbatchupgrade postbatchinstall postbatchremove
HOOKS += prefetch postfetch preargproc postargproc

install-custom:
	@echo Installing CSW$(NAME) files...
	( ginstall -m 0755 -d $(DESTDIR)/opt/csw/share/doc/$(NAME)/ \
		$(HOOKDIR) $(addprefix $(HOOKDIR)/,$(addsuffix .d,$(HOOKS))); \
	  ginstall -m 0644 $(FILEDIR)/README $(DESTDIR)$(docdir)/$(NAME)/; \
	  ginstall -m 0644 $(FILEDIR)/README $(DESTDIR)$(docdir)/$(NAME)/; \
	  ginstall -m 0644 $(FILEDIR)/README \
		$(DESTDIR)/opt/csw/share/doc/$(NAME)/; \
	  $(foreach H,$(HOOKS),ginstall -m 0755 $(FILEDIR)/99-CSW$(NAME)-postupgrade $(HOOKDIR)/$(H).d/99-CSW$(NAME)-$(H);) )
