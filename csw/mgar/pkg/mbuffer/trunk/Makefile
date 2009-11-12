# STATUS/TODO
# - 20090628 contained assertion failures in 64-bit code which have been fixed
#   with 20091012, 20091012 introduced hickups with non-IPv6 systems when using
#   -I / -O (and not explicitly specifying -4)
# - 20091110 does not work on Solaris 8 / 9 any more .. upstream informed
# - 20091110 dumps core on connection refused .. upstream informed

GARNAME = mbuffer
GARVERSION = 20091110
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

# Required during packaging (for the "test" target)
PREREQUISITE_PKGS = CSWmktemp CSWgcc4core

REQUIRED_PKGS = CSWosslrt CSWlibmhash

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

# Required for updated libmhash (mbuffer builds against it) which allows for
# flexible const/non-const definitions.  There should be a more intelligent 
# way to do this than to just put it into every build recipe which requires
# libmhash though ...
EXTRA_CPPFLAGS = -D__const=const

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

post-install-modulated: DOCS = ChangeLog README AUTHORS
post-install-modulated: DOCDEST = $(DESTDIR)$(docdir)/$(GARNAME)
post-install-modulated:
	ginstall -d $(DOCDEST)
	$(foreach DOC,$(DOCS),cp $(WORKSRC)/$(DOC) $(DOCDEST);)
	cp $(FILEDIR)/changelog.CSW $(DOCDEST)
	@$(MAKECOOKIE)
