NAME = mbuffer
VERSION = 20100526
CATEGORIES = utils

DESCRIPTION = A tool for buffering data streams
define BLURB
  mbuffer is a tool for buffering data streams. Its special feature is to show
  the I/O rate and summary to the user. It is especially useful, if you are
  writing backups to fast tape drives or libraries. Those drives tend to stop
  and rewind if they have a buffer underrun. This so called tape screwing
  reduces the lifetime of the motors. mbuffer can prevent buffer underruns,
  if used correctly and speed up the whole backup process.
endef

MASTER_SITES   = http://www.maier-komor.de/software/mbuffer/
DISTFILES      = $(NAME)-$(VERSION).tgz
UFILES_REGEX   = $(NAME)-(\d+(?:\.\d+)*).tar.gz
SPKG_SOURCEURL = http://www.maier-komor.de/mbuffer.html

LICENSE = LICENSE

# Required during packaging (for the "test" target)
BUILD_DEP_PKGS  = CSWmktemp
BUILD_DEP_PKGS += CSWgcc4core

RUNTIME_DEP_PKGS = CSWlibmhash

# 64-bit build enables buffers >= 2GB (see README).
BUILD64 = 1

CONFIGURE_ARGS = $(DIRPATHS)

TEST_TARGET = check

# Required for updated libmhash (mbuffer builds against it) which allows for
# flexible const/non-const definitions.  There should be a more intelligent 
# way to do this than to just put it into every build recipe which requires
# libmhash though ...
EXTRA_CPPFLAGS = -D__const=const

# current9x doesn't know about libm.so.2 from the 64-bit modulated build
CHECKPKG_OVERRIDES_CSWmbuffer += soname-not-found|libm.so.2

EXTRA_PAX_ARGS = '-s,ChangeLog$$,changelog,p'

include gar/category.mk

post-install-modulated: DOCS = ChangeLog README AUTHORS
post-install-modulated: DOCDEST = $(DESTDIR)$(docdir)/$(NAME)
post-install-modulated:
	ginstall -d $(DOCDEST)
	cp $(addprefix $(WORKSRC)/,$(DOCS)) $(DOCDEST)
	cp $(FILEDIR)/changelog.CSW $(DOCDEST)
	@$(MAKECOOKIE)
