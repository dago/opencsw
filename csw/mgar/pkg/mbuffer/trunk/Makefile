GARNAME = mbuffer
GARVERSION = 20081207
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

MASTER_SITES = http://www.maier-komor.de/software/mbuffer/
DISTFILES  = $(GARNAME)-$(GARVERSION).tgz
DISTFILES += $(call admfiles,CSWpackage,)

# We define upstream file regex so we can be notifed of new upstream software 
# release
UFILES_REGEX = -(\d+(?:\.\d+)*).tar.gz

# If the url used to check for software update is different of MASTER_SITES, 
# then uncomment the next line. Otherwise it is set by default to the 
# value of MASTER_SITES
# UPSTREAM_MASTER_SITES = 

CONFIGURE_ARGS = $(DIRPATHS)

TEST_TARGET = check

include gar/category.mk
