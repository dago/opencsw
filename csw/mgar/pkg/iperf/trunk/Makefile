# Todo:
#
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

MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz

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

# We define upstream file regex so we can be notifed of new upstream software release
UPSTREAM_MASTER_SITES = $(SF_PROJECT_SHOWFILE)=128336
UPSTREAM_USE_SF = 1
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

TEST_SCRIPTS = 

CONFIGURE_ARGS = $(DIRPATHS)

# Tell CC not to include additional directories in R*PATH, otherwise we end
# up with something like
# [11]    RUNPATH         /opt/csw/lib/$ISALIST:/opt/csw/lib:/opt/studio/SOS11/SUNWspro/lib/rw7:/opt/studio/SOS11/SUNWspro/lib:/opt/SUNWspro/lib:/usr/ccs/lib:/lib:/usr/lib
# [12]    RPATH           /opt/csw/lib/$ISALIST:/opt/csw/lib:/opt/studio/SOS11/SUNWspro/lib/rw7:/opt/studio/SOS11/SUNWspro/lib:/opt/SUNWspro/lib:/usr/ccs/lib:/lib:/usr/lib
EXTRA_CXX_FLAGS = -norunpath

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
