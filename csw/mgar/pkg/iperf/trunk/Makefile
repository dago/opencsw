# Todo:
# * Check sf project page for patches and threads related to CPU saturation
# * Run some real world performance tests
# * Submit feedback upstream: 
#   - Add AC_CHECK_FUNC or AC_SEARCH_LIBS for sched_yield() so that we get -lrt
#   - Use PTHREAD_{LIBS,CFLAGS} to amend CFLAGS so that we get -lpthreads
#   - Submit language linkage declarations patch for review
# * Add changelog.CSW
#
GARNAME = iperf
GARVERSION = 2.0.4
CATEGORIES = net

DESCRIPTION = Internet Protocol bandwidth measuring tool 
define BLURB
  Iperf was developed by NLANR/DAST as a modern alternative for measuring
  maximum TCP and UDP bandwidth performance. Iperf allows the tuning of
  various parameters and UDP characteristics. Iperf reports bandwidth,
  delay jitter, datagram loss. 
endef

VENDOR_URL   = http://iperf.sourceforge.net/
MASTER_SITES = $(SF_MIRRORS)
DISTFILES    = $(GARNAME)-$(GARVERSION).tar.gz
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

UPSTREAM_MASTER_SITES = $(SF_PROJECT_SHOWFILE)=128336
UPSTREAM_USE_SF = 1

# Add some explicit language linkage declarations. 
#
# See C++ Migration Guide, 3.11.1 "Language Linkage"
# http://dlc.sun.com/pdf/819-3689-10/819-3689-10.pdf
#
# "In compatibility mode, the compiler implements the ARM rule that the 
# language linkage is not part of the function type. In particular, you can
# declare a pointer to a function without regard to the linkage of the pointer 
# or a function assigned to it. 
# In standard mode, the compiler implements the new rule that the language 
# linkage is part of its type, and is part of the type of a pointer to 
# function. The linkages must therefore match."
PATCHFILES = gar-base.diff

TEST_SCRIPTS = 

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk

# * Get rid of gcc -Walls 
# * LIBS: Append -lrt for sched_yield()
# * LIBS: Append -lpthread (upstream should use $PTHREAD_{LIBS,CFLAGS} instead
pre-configure-modulated:
	@perl -pi -e 's|-Wall||; s|\@LIBS\@|\@LIBS\@ -lrt -lpthread|' \
		$(WORKSRC)/Makefile.in \
		$(WORKSRC)/compat/Makefile.in \
		$(WORKSRC)/src/Makefile.in
	@$(MAKECOOKIE)

post-install-modulated: DOCDEST = $(DESTDIR)$(docdir)/$(GARNAME)
post-install-modulated:
	@ginstall -d $(DOCDEST)
	@(cd $(WORKSRC) && cp Changelog AUTHORS $(DOCDEST))
	@$(MAKECOOKIE)
