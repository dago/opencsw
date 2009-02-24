GARNAME = recode
GARVERSION = 3.6
CATEGORIES = utils

DESCRIPTION = GNU recode character set conversion
define BLURB
  The program recognizes or produces approx. 150 character
  sets and can convert almost any character set to almost
  any other. When exact translations are not possible, the
  program may get rid of offending characters or use approximations.
  Particular attention has been paid to the proper representation
  of French language diacritics.
endef

MASTER_SITES = $(GNU_MIRROR)
DISTFILES = $(GARNAME)-$(GARVERSION).tar.gz 

REQUIRED_PKGS = CSWggettextrt CSWiconv

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

# I did some more tests. The faulted tests have something to do
# with compiler optimization:
# 
# The tests 90-96 fail on Solaris 10 Sparc with Sun Studio 11 and -xO2
# The tests 90-96 fail on Solaris 10 Sparc with Sun Studio 12 and -xO2
# All tests succeed on Solaris 10 Sparc with Sun Studio 11 and -xO1
# All tests succeed on Solaris 10 Sparc with Sun Studio 12 and -xO1
# The tests 59 fails and 90-96 don't terminate on Solaris 10 x86 with Sun Studio 11 and -xO0
# The tests 59 fails and 90-96 don't terminate on Solaris 10 x86 with Sun Studio 12 and -xO0
# All tests succeed on Solaris 10 x86 with Sun Studio 11 without optimization
# All tests succeed on Solaris 10 x86 with Sun Studio 12 without optimization
# 
# I just discovered that this is already on the list in the file TODO:
# 
# . + Solaris cc 4.2 with option "-O" miscompiles src/libiconv.c, probably
#     the function module_libiconv. The symptom is that
#     "src/recode --quiet --force ascii-bs..ebcdic < COPYING > output"
#     creates an output file smaller than COPYING. The only known workaround
#     is to not use "-O".

OPT_FLAGS_SOS =

CONFIGURE_ARGS = $(DIRPATHS) \
	--enable-static=no

TEST_TARGET = check

EXTRA_MERGE_EXCLUDE_FILES = $(libdir)/charset.alias

include gar/category.mk

LDFLAGS += -lintl
