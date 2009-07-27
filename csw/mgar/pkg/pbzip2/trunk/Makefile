GARNAME = pbzip2
GARVERSION = 1.0.5
CATEGORIES = utils

DESCRIPTION = Parallel BZIP2 Data Compression Software
define BLURB
  PBZIP2 is a parallel implementation of the bzip2 block-sorting file 
  compressor that uses pthreads and achieves near-linear speedup on SMP 
  machines. The output of this version is fully compatible with 
  bzip2 v1.0.2 or newer
endef

MASTER_SITES = http://compression.ca/pbzip2/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

# If the url used to check for software update is different of MASTER_SITES, then 
# uncomment the next line. Otherwise it is set by default to the value of MASTER_SITES
# UPSTREAM_MASTER_SITES = 

# we require
REQUIRED_PKGS = CSWbzip2

# since there is no configure script, this is intentionally left empty
CONFIGURE_SCRIPTS =

# no build tests
SKIPTEST = 1

# custom install
INSTALL_SCRIPTS = custom

include gar/category.mk

pre-build-modulated:
	@gsed -i'' \
	's,-pthread,-I$(includedir) -L$(libdir),g;s,g++,$(CXX),;s,-O2,$(CFLAGS),' \
	$(WORKSRC)/Makefile

install-custom:
	[ ! -d "$(DESTDIR)$(mandir)/man1" ] && \
		ginstall -d $(DESTDIR)$(mandir)/man1
	ginstall -m 0644 $(WORKSRC)/pbzip2.1 $(DESTDIR)$(mandir)/man1
	[ ! -d "$(DESTDIR)$(bindir)" ] && \
		ginstall -d $(DESTDIR)$(bindir)
	ginstall -m 0755 $(WORKSRC)/$(GARNAME) $(DESTDIR)$(bindir)
	ln -s -f $(bindir)/$(GARNAME) $(DESTDIR)$(bindir)/pbunzip2
	ln -s -f $(bindir)/$(GARNAME) $(DESTDIR)$(bindir)/pbzcat
