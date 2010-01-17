GARNAME = file
GARVERSION = 5.03
CATEGORIES = utils

DESCRIPTION = A file type guesser
define BLURB
  The file command is "a file type guesser", that is, a command-line tool that
  tells you in words what kind of data a file contains. Unlike most GUI systems,
  command-line UNIX systems - with this program leading the charge - don't rely
  on filename extentions to tell you the type of a file, but look at the file's
  actual contents. This is, of course, more reliable, but requires a bit of I/O.
endef

MASTER_SITES = ftp://ftp.astron.com/pub/file/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

SPKG_SOURCEURL = http://www.darwinsys.com/file/

CONFIGURE_ARGS = $(DIRPATHS)

# These flags are not understood by Sun Studio
CONFIGURE_ARGS += --disable-warnings

TEST_TARGET = check

include gar/category.mk
