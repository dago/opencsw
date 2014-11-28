# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = mupdf
VERSION = 1.6
GARTYPE = v2

DESCRIPTION = Lightweight PDF and XPS viewer
define BLURB
  MuPDF is small, fast, and yet complete. It supports PDF 1.7 with
  transparency, encryption, hyperlinks, annotations, searching and more.
  It also reads XPS and OpenXPS documents.

  The renderer in MuPDF is tailored for high quality anti-aliased
  graphics. It renders text with metrics and spacing accurate to within
  fractions of a pixel for the highest fidelity in reproducing the look of
  a printed page on screen.
endef

MASTER_SITES = http://mupdf.com/downloads/
DISTNAME = $(NAME)-$(VERSION)-source
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*)-source.tar.gz
DISTFILES  = $(DISTNAME).tar.gz
VENDOR_URL = http://mupdf.com/
LICENSE = COPYING

PACKAGES = CSWmupdf CSWmupdf-tools
SPKG_DESC_CSWmupdf = $(DESCRIPTION)
SPKG_DESC_CSWmupdf-tools = Commmand line tools for the MuPDF viewer
PKGFILES_CSWmupdf = $(docdir)/$(NAME)/* $(bindir)/mupdf $(mandir)/man1/mupdf.1
PKGFILES_CSWmupdf-tools = $(bindir)/mudraw $(bindir)/mutool \
  $(mandir)/man1/mudraw.1 $(mandir)/man1/mutool.1

PATCHFILES += 0001-adjust-Makefile-for-Solaris.patch

CONFIGURE_SCRIPTS =
BUILD_ARGS += build=none verbose=yes
INSTALL_ARGS += build=none verbose=yes
TEST_SCRIPTS =
INSTALL_SCRIPTS = custom

install-custom:
	@ginstall -d $(DESTDIR)$(bindir)
	@ginstall -d $(DESTDIR)$(mandir)/man1
	@ginstall -d $(DESTDIR)$(docdir)/$(NAME)
	@ginstall $(WORKSRC)/build/none/mudraw $(DESTDIR)$(bindir)
	@ginstall $(WORKSRC)/build/none/mutool $(DESTDIR)$(bindir)
	@ginstall -T $(WORKSRC)/build/none/mupdf-x11-curl $(DESTDIR)$(bindir)/mupdf
	@ginstall -m 644 $(WORKSRC)/docs/man/*.1 $(DESTDIR)$(mandir)/man1
	@ginstall -m 644 $(WORKSRC)/README $(WORKSRC)/CHANGES $(WORKSRC)/docs/*.txt $(DESTDIR)$(docdir)/$(NAME)
	@$(MAKECOOKIE)


RUNTIME_DEP_PKGS_CSWmupdf += CSWlibcurl4 CSWlibjpeg7 CSWlibssl1-0-0 CSWlibz1 \
    CSWlibjbig2dec0 CSWlibfreetype6
RUNTIME_DEP_PKGS_CSWmupdf-tools += CSWlibjpeg7 CSWlibssl1-0-0 CSWlibz1 \
    CSWlibjbig2dec0 CSWlibfreetype6

include gar/category.mk

post-extract:
	$(RM) $(WORKSRC)/thirdparty/curl/README $(WORKSRC)/thirdparty/jpeg/README \
	  $(WORKSRC)/thirdparty/zlib/README $(WORKSRC)/thirdparty/freetype/README \
	  $(WORKSRC)/thirdparty/openjpeg/CMakeLists.txt \
	  $(WORKSRC)/thirdparty/jbig2dec/README
	@$(MAKECOOKIE)
