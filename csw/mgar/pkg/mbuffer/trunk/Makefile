# TODO
# - sparcv9 (64-bit) tests fail with assertion failures (we have had this before,
#   upstream doesn't test 64-bit builds) --> report upstream:
#
# ./mbuffer -q -I :8000 | openssl md5 > test2.md5 &
# sleep 1
# rm -f test2.tar
# ./mbuffer -i test.tar -o /dev/null -O localhost:8000 -o test2.tar -H
# mbuffer: warning: error connecting localhost:8000: Network is unreachable
# 
# mbuffer: warning: error connecting localhost:8000: Network is unreachable
# Assertion failed: (err == 0) && (bsize == sizeof(osize)), file network.c, line 64
# Assertion failed: (err == 0) && (bsize == sizeof(osize)), file network.c, line 64
#

GARNAME = mbuffer
GARVERSION = 20091103
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
LICENSE = LICENSE

# Required during packaging (for the "test" target)
PREREQUISITE_PKGS = CSWmktemp CSWgcc4core

REQUIRED_PKGS = CSWosslrt

# We define upstream file regex so we can be notifed of new upstream software 
# release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

# To build the mixed package for x86 you have to do the following
# 1)  build8x: gmake merge
# 2) build10x: gmake merge
# 3)  build8x: gmake package
BUILD64 = 1

# 64-bit isn't thorougly tested by upstream, default to 32-bit, but still
# deliver 64-bit in case someone might want to play around with 2GB+ buffers
# ISAEXEC_BINS = $(bindir)/mbuffer
NO_ISAEXEC = 1

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
	cp $(WORKSRC)/mbuffer $(WORKSRC)/Makefile $(TMPDIR)/

	# Target test3 is skipped because it contains IPV6 tests which
	# are not supported by the build farm boxes (yet).
	$(MAKE) -C $(TMPDIR) -o test3 check
	rm -rf $(TMPDIR)
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
	@$(foreach DOC,$(DOCS),cp $(WORKSRC)/$(DOC) $(DOCDEST);)
	@cp $(FILEDIR)/changelog.CSW $(DOCDEST)
	@$(MAKECOOKIE)
