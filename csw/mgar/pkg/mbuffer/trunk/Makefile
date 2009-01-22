GARNAME = mbuffer
GARVERSION = 20090113
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
DISTFILES += $(call admfiles,CSWmbuffer,)

REQUIRED_PKGS = CSWosslrt

# Required for the test target
PREREQUISITE_PKGS = CSWmktemp CSWgcc4core

# We define upstream file regex so we can be notifed of new upstream software 
# release
UFILES_REGEX = -(\d+(?:\.\d+)*).tar.gz

# If the url used to check for software update is different of MASTER_SITES, 
# then uncomment the next line. Otherwise it is set by default to the 
# value of MASTER_SITES
# UPSTREAM_MASTER_SITES = 

# There had been a reason once to build the 64-bit version (all the way down)
# http://opensolaris.org/jive/thread.jspa?messageID=293647&tstart=0
#
# To build the mixed package for x86 you have to do the following
# 1)  build8x: gmake build-isa-i386
# 2) build10x: gmake merge
# 3)  build8x: gmake package
#
# As this is a bit of a hassle and mbuffer has frequent release cycles i
# prefer to leave it out until someone actually needs it.
#
# BUILD64 = 1
# ISAEXEC_BINS = $(bindir)/mbuffer

CONFIGURE_ARGS = $(DIRPATHS)

TEST_SCRIPTS = custom

include gar/category.mk

# The test scripts do file IO and this is so sloooooow when being run 
# in a NFS mounted $HOME. The local disk on build8x is no better, so
# just do the testing from /tmp instead.
#
# TODO: 
# * Clean up $TMPDIR even when the nested make fails.
# * Somehow assert that the isa-amd64 test is run on build10x
#
test-custom: TMPDIR := $(shell mktemp -d -p /tmp)
test-custom:
	echo "Running target test-custom, TMPDIR = $(TMPDIR)"
	@cp $(WORKSRC)/mbuffer $(WORKSRC)/Makefile $(TMPDIR)/
	@$(MAKE) -C $(TMPDIR) check
	@rm -rf $(TMPDIR)
	@$(MAKECOOKIE)

# Solaris 10 on build10x has libm.so which points to libm.so.2. libm.so.2 
# is however not available on Solaris 8. So we have to explicitly use 
# libm.so.1 during linking and get rid of the -lm reference. Otherwise
# the package check on build8x (when running "gmake package") fails.
post-configure-isa-amd64:
	@echo "Patching Makefile to use /lib/64/libm.so.1 instead of -lm"
	@perl -pi -e 's#-lm#/lib/64/libm.so.1#' $(WORKSRC)/Makefile
	@$(MAKECOOKIE)

post-install-modulated: DOCS = ChangeLog README AUTHORS
post-install-modulated: DOCDEST = $(DESTDIR)$(docdir)/$(GARNAME)
post-install-modulated:
	@ginstall -d $(DOCDEST)
	@$(foreach DOC,$(DOCS),ginstall -m 644 $(WORKSRC)/$(DOC) $(DOCDEST);)
	@$(MAKECOOKIE)
