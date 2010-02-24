# TODO 
# ! strtoimax implementation missing on Solaris 8/9
# ! on repeated gmake build invocations (after build failures), only a subset of the
#   environment is used, in particular CPPFLAGS/LDFLAGS are missing
GARNAME = tmpwatch
GARVERSION = 2.9.17
CATEGORIES = apps

DESCRIPTION = Removes files which haven't been accessed for a period of time
define BLURB
  The tmpwatch utility recursively searches through specified directories
  and removes files which have not been accessed in a specified period of
  time. tmpwatch is normally used to clean up directories which are used
  for temporarily holding files (for example, /tmp). 
endef

VENDOR_URL   = https://fedorahosted.org/tmpwatch/
MASTER_SITES = https://fedorahosted.org/releases/t/m/tmpwatch/
DISTFILES    = $(GARNAME)-$(GARVERSION).tar.bz2
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.bz2

# Taken from libgcrypt's stringhelp.c
DISTFILES    += stpcpy.c

# Tweak Makefile to honor environment variables
PATCHFILES  = 0001-Makefile-honor-defaults-and-use-DESTDIR-instead-of-R.patch
# Include missing stpcpy() implementation
PATCHFILES += 0002-tmpwatch.c-include-stpcpy.c.patch

CONFIGURE_SCRIPTS =
BUILD_ARGS = tmpwatch
TEST_SCRIPTS =

# Link against our OpenCSW getopt lib which has getopt_long
EXTRA_LD_FLAGS = -lgnugetopt

include gar/category.mk

pre-build-modulated:
	cp $(WORKDIR)/stpcpy.c $(WORKSRC)
	@$(MAKECOOKIE)
