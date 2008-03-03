GARNAME = Tk
GARVERSION = 804.027
CATEGORIES = cpan
AUTHOR = NI-S

DESCRIPTION = write Tk applications in Perl.
define BLURB
  In writing the perl Tk extension, the goals were to provide a complete
  interface to the latest production version of John Ousterhout's Tk, while
  providing an Object Oriented interface to perl code.
endef

DISTFILES += CSWpmtk.gspec

# Use Solaris zlib/png/jpeg
#PATCHFILES = syslibs.diff

# Fix problems with ISO646 mapping to 'US-ASCII'
PATCHFILES += nl_langinfo.diff

include gar/category.mk
