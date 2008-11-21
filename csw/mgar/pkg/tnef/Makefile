GARNAME = tnef
GARVERSION = 1.4.5
CATEGORIES = utils

DESCRIPTION = Unpacks Microsoft TNEF MIME attachments
define BLURB
  TNEF provides a way to unpack those pesky Microsoft MS-TNEF MIME attachments.
  It operates like tar in order to upack any files which may have been put into
  the MS-TNEF attachment instead of being attached seperately.
endef

MASTER_SITES = http://downloads.sourceforge.net/tnef/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += $(call admfiles,CSWtnef,)

CONFIGURE_ARGS = $(DIRPATHS)

TEST_SCRIPTS = custom
INSTALL_SCRIPTS = custom

include ../category.mk

SPKG_SOURCEURL = http://sourceforge.net/projects/tnef

test-custom:
	@echo " ==> Testing $(GARNAME) (custom)"
	@( cd $(WORKSRC) ; \
	   gmake check )
	@$(MAKECOOKIE)

install-custom:
	@echo " ==> Installing $(GARNAME) (custom)"
	@rm -rf $(DESTDIR)
	@ginstall -d $(DESTDIR)$(bindir)
	@ginstall -d $(DESTDIR)$(docdir)/$(GARNAME)
	@ginstall -d $(DESTDIR)$(mandir)/man1
	@( cd $(WORKSRC) ; \
	   cp -r src/$(GARNAME) $(DESTDIR)$(bindir)/$(GARNAME) ; \
	   cp -r doc/$(GARNAME).1 $(DESTDIR)$(mandir)/man1/$(GARNAME).1 ; \
	   cp -r COPYING $(DESTDIR)$(docdir)/$(GARNAME)/LICENSE )
	@$(MAKECOOKIE)
