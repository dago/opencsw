GARNAME = mbuffer
GARVERSION = 20091227
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
DISTFILES      = $(GARNAME)-$(GARVERSION).tgz
UFILES_REGEX   = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz
SPKG_SOURCEURL = http://www.maier-komor.de/mbuffer.html

LICENSE = LICENSE

# The tests use background process and wait, but don't issue the wait
# in the same shell as the background processes were launched in. Fix this.
# Already submitted to upstream, maybe integrated in future versions.
PATCHFILES = 0001-Makefile-put-background-jobs-in-same-shell-as-the-wa.patch

# Required during packaging (for the "test" target)
PREREQUISITE_PKGS  = CSWmktemp
PREREQUISITE_PKGS += CSWgcc4core

REQUIRED_PKGS = CSWlibmhash

# 64-bit build enables buffers >= 2GB (see README).
BUILD64 = 1

CONFIGURE_ARGS = $(DIRPATHS)

TEST_TARGET = check

# Required for updated libmhash (mbuffer builds against it) which allows for
# flexible const/non-const definitions.  There should be a more intelligent 
# way to do this than to just put it into every build recipe which requires
# libmhash though ...
EXTRA_CPPFLAGS = -D__const=const

include gar/category.mk

post-install-modulated: DOCS = ChangeLog README AUTHORS
post-install-modulated: DOCDEST = $(DESTDIR)$(docdir)/$(GARNAME)
post-install-modulated:
	ginstall -d $(DOCDEST)
	cp $(addprefix $(WORKSRC)/,$(DOCS)) $(DOCDEST)
	cp $(FILEDIR)/changelog.CSW $(DOCDEST)
	@$(MAKECOOKIE)
