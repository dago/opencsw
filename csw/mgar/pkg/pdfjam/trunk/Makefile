NAME = pdfjam
VERSION = 1.21
CATEGORIES = utils
GARTYPE = v2

DESCRIPTION = Small collection of shell scripts to enhance pdflatex
define BLURB
  PDFjam is a small collection of shell scripts which provide a simple interface
  to some of the functionality of the excellent pdfpages package (by Andreas Matthias)
  for pdfLaTeX.
endef

MASTER_SITES = http://www.warwick.ac.uk/go/pdfjam/
DISTFILES  = $(NAME)_$(VERSION).tar.gz
PATCHFILES  = 0001-Hardcode-CSW-tools-and-pathes.patch
PATCHFILES += 0002-Step-out-of-tempdir-before-removing-it.patch
PATCHFILES += 0003-Use-CSW-bash-because-the-Solaris-shipped-one-is-too-.patch

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

SPKG_SOURCEURL = http://www2.warwick.ac.uk/fac/sci/statistics/staff/academic/firth/software/pdfjam

RUNTIME_DEP_PKGS = CSWtetex CSWbash

DISTNAME = pdfjam

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS =
TEST_SCRIPTS =
INSTALL_SCRIPTS = custom

ARCHALL = 1

include gar/category.mk

install-custom:
	ginstall -d $(DESTDIR)$(bindir)
	(cd $(WORKSRC) && ginstall scripts/* $(DESTDIR)$(bindir))
	ginstall -d $(DESTDIR)$(docdir)/pdfjam
	(cd $(WORKSRC) && ginstall VERSION PDFjam-README.html pdfdroplets.png $(DESTDIR)$(docdir)/pdfjam)
	ginstall -d $(DESTDIR)$(mandir)/man1
	(cd $(WORKSRC) && ginstall man1/* $(DESTDIR)$(mandir)/man1)
	@$(MAKECOOKIE)
