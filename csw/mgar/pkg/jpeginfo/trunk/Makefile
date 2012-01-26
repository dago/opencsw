NAME = jpeginfo
VERSION = 1.6.1
CATEGORIES = utils
GARTYPE = v2

DESCRIPTION = Info and error checking of jpeg files
define BLURB
  Utility to generate informative listings from jpeg files, and to check jpeg files
  for errors. Program also supports automagic deletion of broken jpegs.
endef

MASTER_SITES = http://www.kokkonen.net/tjko/src/
DISTFILES  = $(NAME)-$(VERSION).tar.gz

RUNTIME_DEP_PKGS = CSWjpeg

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

CONFIGURE_ARGS = $(DIRPATHS)

TEST_TARGET =
INSTALL_SCRIPTS = custom

include gar/category.mk

SPKG_SOURCEURL = http://www.kokkonen.net/tjko/projects.html#jpeginfo

install-custom:
	@echo " ==> Installing $(NAME) (custom)"
	@rm -rf $(DESTDIR)
	@ginstall -d $(DESTDIR)$(bindir)
	@ginstall -d $(DESTDIR)$(docdir)/$(NAME)
	@ginstall -d $(DESTDIR)$(mandir)/man1
	@( cd $(WORKSRC) ; \
	   cp -r $(NAME) $(DESTDIR)$(bindir)/$(NAME) ; \
	   cp -r README $(DESTDIR)$(docdir)/$(NAME) ; \
	   cp -r $(NAME).1 $(DESTDIR)$(mandir)/man1/$(NAME).1 )
	@$(MAKECOOKIE)
