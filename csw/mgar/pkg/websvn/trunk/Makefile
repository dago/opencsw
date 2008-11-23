GARNAME = websvn
GARVERSION = 2.0
CATEGORIES = apps

DESCRIPTION = PHP based web interface of Subversion repositories
define BLURB
  WebSVN offers a view onto your subversion repositories that's been
  designed to reflect the Subversion methodology. You can view the
  log of any file or directory and see a list of all the files changed,
  added or deleted in any given revision. You can also view the differences
  between 2 versions of a file so as to see exactly what was changed in
  a particular revision.
endef

MASTER_SITES  = svn-http://websvn.tigris.org/svn/$(GARNAME)/tags/
DISTFILES = $(GARVERSION)
NOCHECKSUM = $(GARVERSION)
SVNHTTP_CO_ARGS = --no-auth-cache --username guest --password guest

SPKG_SOURCEURL = http://websvn.tigris.org/

DISTFILES += $(call admfiles,CSWwebsvn,depend postinstall preremove)
PATCHFILES = websvn-csw-config.patch

WORKSRC = $(WORKDIR)/$(GARVERSION)

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS =
TEST_SCRIPTS =
INSTALL_SCRIPTS = custom

include gar/category.mk

post-extract:
	@echo " ==> Preparing include/config.php.CSW"
	@cp $(WORKSRC)/include/distconfig.php \
		$(WORKSRC)/include/config.php.CSW
	@$(MAKECOOKIE)

install-custom:
	@echo " ==> Installing $(GARNAME)"
	@rm -rf $(DESTDIR)$(sharedstatedir)/www/websvn
	@ginstall -d $(DESTDIR)$(sharedstatedir)/www/websvn
	@cp -rp $(WORKSRC) $(DESTDIR)$(sharedstatedir)/www/websvn/htdocs
	@find $(DESTDIR)$(prefix) -name .svn -exec rm -rf \{\} \;
	@rm -rf $(DESTDIR)$(prefix)/apache2/share/htdocs/websvn
	@ginstall -d $(DESTDIR)$(prefix)/apache2/share/htdocs
	@ln -s $(sharedstatedir)/www/websvn/htdocs $(DESTDIR)$(prefix)/apache2/share/htdocs/websvn
