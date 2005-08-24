GARNAME = HTTP-Webdav
GARVERSION = 0.1.18-0.17.1
CATEGORIES = cpan
AUTHOR = GRICHTER

DESCRIPTION = interface to Neon HTTP and WebDAV client library
define BLURB
  This is the Perl interface to the neon HTTP and WebDAV client library. Most
  of the documentation is automaticly generated from the C header files of
  neon. So it looks a little bit C-ish, but is better than nothing. See also
  the examples in the eg directory. If you not sure how it works consult the
  neon include files.
endef

DISTFILES += CSWpmhttpwebdav.gspec

DEPENDS += lib/neon

NEON_INC = $(shell $(DESTDIR)$(bindir)/neon-config --cflags)
CONFIGURE_ARGS = INC="-I$(DESTDIR)$(includedir)/neon $(NEON_INC)"

.DEFAULT:
	@echo "$@: $(GARNAME) does not build with current neon version"
	@true

#include ../category.mk
