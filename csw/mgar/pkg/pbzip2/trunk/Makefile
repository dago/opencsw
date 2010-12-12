NAME = pbzip2
VERSION = 1.1.1
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

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

# If the url used to check for software update is different of MASTER_SITES, then 
# uncomment the next line. Otherwise it is set by default to the value of MASTER_SITES
# UPSTREAM_MASTER_SITES = 

# we require
RUNTIME_DEP_PKGS = CSWbzip2

# since there is no configure script, this is intentionally left empty
CONFIGURE_SCRIPTS =

# no build tests
SKIPTEST = 1

# custom install
INSTALL_SCRIPTS = custom

# After some testing. Using a special ISA modulation does *not* speed
# up bzip2. Therefor i will just stick to a regular 32bit build here.

include gar/category.mk

pre-build-modulated:
	@gsed -i'' 's,-lpthread,-norunpath -lpthread,g;s,-pthread,-I$(includedir) -L$(libdir),g;s,g++,$(CXX),;s,-O2,-fast $(filter-out -xnorunpath,$(CFLAGS)),' $(WORKSRC)/Makefile

install-custom:
	[ ! -d "$(DESTDIR)$(mandir)/man1" ] && \
		ginstall -d $(DESTDIR)$(mandir)/man1
	ginstall -m 0644 $(WORKSRC)/pbzip2.1 $(DESTDIR)$(mandir)/man1
	[ ! -d "$(DESTDIR)$(bindir)" ] && \
		ginstall -d $(DESTDIR)$(bindir)
	ginstall -m 0755 $(WORKSRC)/$(NAME) $(DESTDIR)$(bindir)
	ln -s -f $(bindir)/$(NAME) $(DESTDIR)$(bindir)/pbunzip2
	ln -s -f $(bindir)/$(NAME) $(DESTDIR)$(bindir)/pbzcat
