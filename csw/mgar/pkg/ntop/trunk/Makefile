GARNAME = ntop
GARVERSION = 3.3.10
CATEGORIES = net

DESCRIPTION = A network traffic usage monitor.
define BLURB
  ntop is a network probe that shows network usage in a way similar to what top
  does for processes. In interactive mode, it displays the network status on the
  user's terminal. In Web mode, it acts as a Web server, creating an HTML dump
  of the network status. It sports a NetFlow/sFlow emitter/collector, an
  HTTP-based client interface for creating ntop-centric monitoring applications,
  and RRD for persistently storing traffic statistics.
endef

MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz

PATCHFILES = configure.in.diff
PATCHFILES += configureextra_opencsw.diff

# We define upstream file regex so we can be notifed of new upstream software release
UPSTREAM_MASTER_SITES = $(SF_PROJECT_SHOWFILE)=17233
UPSTREAM_USE_SF = 1
UFILES_REGEX = (\d+(?:\.\d+)*)

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --with-pcap-lib=/opt/csw/lib
CONFIGURE_ARGS += --with-pcap-include=/opt/csw/include
CONFIGURE_ARGS += --with-gdbm-lib=/opt/csw/lib
CONFIGURE_ARGS += --with-gdbm-include=/opt/csw/include
CONFIGURE_ARGS += --with-zlib-lib=/opt/csw/lib
CONFIGURE_ARGS += --with-zlib-include=/opt/csw/include
CONFIGURE_ARGS += --with-ossl-lib=/opt/csw/lib
CONFIGURE_ARGS += --with-ossl-include=/opt/csw/include

include gar/category.mk

pre-configure-modulated:
	( cd $(WORKSRC) ; ./autogen.sh --noconfig)
	@$(MAKECOOKIE)

