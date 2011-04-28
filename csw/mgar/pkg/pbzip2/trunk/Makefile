NAME = pbzip2
VERSION = 1.1.4
CATEGORIES = utils

DESCRIPTION = Parallel BZIP2 Data Compression Software
define BLURB
  PBZIP2 is a parallel implementation of the bzip2 block-sorting file 
  compressor that uses pthreads and achieves near-linear speedup on SMP 
  machines. The output of this version is fully compatible with 
  bzip2 v1.0.2 or newer
endef

MASTER_SITES = http://compression.ca/pbzip2/
DISTFILES  = $(NAME)-$(VERSION).tar.gz

PACKAGES += CSWpbzip2
CATALOGNAME_CSWpbzip2 = pbzip2
SPKG_DESC_CSWpbzip2 = Parallel BZIP2 Data Compression Software
RUNTIME_DEP_PKGS_CSWpbzip2 += CSWbzip2

# Since there is no configure script, this is intentionally left empty
CONFIGURE_SCRIPTS =

# There is no testsuite
TEST_SCRIPTS =

INSTALL_SCRIPTS = custom

# After some testing. Using a special ISA modulation does *not* speed
# up bzip2. Therefor i will just stick to a regular 32bit build here.

include gar/category.mk

pre-build-modulated:
	gsed -i'' 's,-lpthread,-norunpath -lpthread,g;s,-pthread,-I$(includedir) -L$(libdir),g;s,g++,$(CXX),;s,-O2,-fast $(filter-out -xnorunpath,$(CFLAGS)),' $(WORKSRC)/Makefile

install-custom:
	[ ! -d "$(DESTDIR)$(mandir)/man1" ] && \
		ginstall -d $(DESTDIR)$(mandir)/man1
	ginstall -m 0644 $(WORKSRC)/pbzip2.1 $(DESTDIR)$(mandir)/man1
	[ ! -d "$(DESTDIR)$(bindir)" ] && \
		ginstall -d $(DESTDIR)$(bindir)
	ginstall -m 0755 $(WORKSRC)/$(NAME) $(DESTDIR)$(bindir)
	ln -s -f $(bindir)/$(NAME) $(DESTDIR)$(bindir)/pbunzip2
	ln -s -f $(bindir)/$(NAME) $(DESTDIR)$(bindir)/pbzcat
