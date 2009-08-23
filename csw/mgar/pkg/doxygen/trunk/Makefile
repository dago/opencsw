# Todo (feel free to take over):
# - gmake docs segfaults, check why 
#   (related to libiconv? Might change with libiconv 1.13+)
# - platform makefile doesn't honor our CCFLAGS
#   work/build-isa-i386/doxygen-1.5.9/tmake/lib/solaris-cc/tmake.conf
#   results in: CC -c -O2 -I..
#
# Adding members to index pages...
# Generating style sheet...
# Generating index page...
# Generating page index...
# Segmentation Fault - core dumped
# gmake[1]: *** [all] Error 139
# gmake[1]: Leaving directory `/home/skayser/mgar/pkg/doxygen/trunk/work/build-isa-i386/doxygen-1.5.9/doc'
# 
# $ pstack work/build-isa-i386/doxygen-1.5.9/doc/core
# core 'work/build-isa-i386/doxygen-1.5.9/doc/core' of 20317:     /home/skayser/mgar/pkg/doxygen/trunk/work/build-isa-i386/doxygen-1.5.9
# df945898 iconv    (ffffffff, 80478d8, 80478d0, 80478dc, 80478d4) + 38
# 083d2e52 portable_iconv (ffffffff, 80478d8, 80478d0, 80478dc, 80478d4) + 1a
# 081c1ec2 __1cIHtmlHelpGrecode6MrknIQdDCString__1_ (804790c, 8da4210, 8047910) + 6a
# 081c1fe6 __1cIHtmlHelpPaddContentsItem6Mbpkc222_v_ (8da4210, 0, 8de85a8, 0, 8de85c8, 0) + b2
# 08198b75 __1cJIndexListHforeach4CbCpkcC2C2C2_6MmJIndexIntf_MTATBTCTDTE_v34567_v_ (85fa380, 81d2af4, 0, 0, 8de85a8, 0, 8de85c8, 0) + 99
# 081ccec6 __1cOwritePageIndex6FrnKOutputList__v_ (8d97f50) + 372
# 081920c3 __1cOgenerateOutput6F_v_ () + a27
# 08169d11 main     (1, 8047ad8, 8047ae0) + 2d
# 08169c56 _start   () + 7a
#

GARNAME = doxygen
GARVERSION = 1.5.9
CATEGORIES = utils

DESCRIPTION = A documentation system for programming languages
define BLURB
  Long description
endef

MASTER_SITES = http://ftp.stack.nl/pub/users/dimitri/
DISTFILES  = $(GARNAME)-$(GARVERSION).src.tar.gz
SPKG_SOURCEURL = http://www.stack.nl/~dimitri/doxygen/

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).src.tar.gz
UPSTREAM_MASTER_SITES = $(SPKG_SOURCEURL)

CONFIGURE_ARGS = $(subst =, ,$(filter --prefix=% , $(DIRPATHS)))
CONFIGURE_ARGS += --docdir $(docdir)
CONFIGURE_ARGS += --platform solaris-cc

TEST_SCRIPTS = 

include gar/category.mk

post-extract-modulated:
	perl -pi -e 'if (/^TMAKE_CXXFLAGS_RELEASE/) { \
			s|= .*|= $(filter-out -I/opt/csw/include, $(CXXFLAGS)) -norunpath|; }' \
		$(WORKSRC)/tmake/lib/solaris-cc/tmake.conf
	perl -pi -e 'if (/^TMAKE_CFLAGS_DEBUG/) { s|= .*|= $(filter-out -I/opt/csw/include,$(CFLAGS))|; }' \
		$(WORKSRC)/tmake/lib/solaris-cc/tmake.conf
	@$(MAKECOOKIE)
