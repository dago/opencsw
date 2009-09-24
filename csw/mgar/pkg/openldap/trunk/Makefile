GARNAME = openldap
GARVERSION = 2.4.18
CATEGORIES = server
EXTRA_MODULATORS = GARVERSION
MODULATIONS_GARVERSION = 2.3.43 2.4.18

DESCRIPTION = Open source implementation of the Lightweight Directory Access Protocol
define BLURB
  The OpenLDAP Project is a collaborative effort to develop a robust,
  commercial-grade, fully featured, and open source LDAP suite of applications
  and development tools. The project is managed by a worldwide community of
  volunteers that use the Internet to communicate, plan, and develop the
  OpenLDAP Suite and its related documentation.
endef

# Missing lib: ld.so.1: svn: fatal: libldap-2.3.so.0: open failed: No such file or directory

MASTER_SITES = ftp://ftp.openldap.org/pub/OpenLDAP/openldap-release/
SOURCEFILES  = $(foreach VERSION,$(MODULATIONS_GARVERSION),$(GARNAME)-$(VERSION).tgz)
DISTFILES  = $(SOURCEFILES)
DISTFILES += $(call admfiles,CSWoldap)
DISTFILES += README.CSW openldaprc
DISTFILES += cswopenldap openldap.xml svc-openldap

PATCHFILES_isa-sparcv8-garversion-2.4.18 = patch-oldap-2.4.16-ntlm.diff
PATCHFILES_isa-sparcv9-garversion-2.4.18 = patch-oldap-2.4.16-ntlm.diff
PATCHFILES_isa-i386-garversion-2.4.18 = patch-oldap-2.4.16-ntlm.diff
PATCHFILES_isa-amd64-garversion-2.4.18 = patch-oldap-2.4.16-ntlm.diff
DISTFILES += patch-oldap-2.4.16-ntlm.diff


NOEXTRACT = $(filter-out $(GARNAME)-$(GARVERSION).tgz,$(SOURCEFILES))

LICENSE = COPYRIGHT

PACKAGES = CSWoldap CSWoldapclient CSWoldapdevel CSWoldaprt

CATALOGNAME_CSWoldap       = openldap
CATALOGNAME_CSWoldapclient = openldap_client
CATALOGNAME_CSWoldapdevel  = openldap_devel
CATALOGNAME_CSWoldaprt     = openldap_rt

SPKG_DESC_CSWoldap       = OpenLDAP server for Lightweight Directory Access Protocol
SPKG_DESC_CSWoldapclient = OpenLDAP client executables
SPKG_DESC_CSWoldapdevel  = OpenLDAP development support
SPKG_DESC_CSWoldaprt     = OpenLDAP runtime libraries

REQUIRED_PKGS_CSWoldap       = CSWbdb CSWiconv CSWlibnet CSWlibtoolrt CSWoldaprt
REQUIRED_PKGS_CSWoldap      += CSWosslrt CSWsasl CSWtcpwrap CSWunixodbc CSWcswclassutils
REQUIRED_PKGS_CSWoldap      += CSWkrb5lib CSWlibicu CSWperl
REQUIRED_PKGS_CSWoldapclient = CSWlibnet CSWoldaprt CSWosslrt CSWsasl CSWkrb5lib
REQUIRED_PKGS_CSWoldapdevel  = CSWoldaprt
REQUIRED_PKGS_CSWoldaprt     = CSWlibnet CSWosslrt CSWsasl CSWkrb5lib

SPKG_SOURCEURL = http://www.openldap.org

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

EXTRA_DOCS = README.CSW $(PATCHFILES)

# OpenLDAP 2.3 was bound to bdb44
#EXTRA_LIB = $(prefix)/bdb44/lib 
#EXTRA_INC = $(prefix)/bdb44/include

BUILD64 = 1
CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --enable-crypt
CONFIGURE_ARGS += --enable-lmpasswd
CONFIGURE_ARGS += --enable-modules
CONFIGURE_ARGS += --enable-rlookups
CONFIGURE_ARGS += --enable-slp
# Disable TCPwrappers in 64 bit until the libraries are available
#   <http://opencsw.org/mantis/view.php?id=3748>
CONFIGURE_ARGS_32 = --enable-wrappers
# spasswd requires Cyrus SASL
CONFIGURE_ARGS_32 += --enable-spasswd
# Disable Cyrus SASL in 64 bit until the libraries are available
#   <http://opencsw.org/mantis/view.php?id=3749>
CONFIGURE_ARGS_64 += --without-cyrus-sasl
CONFIGURE_ARGS += $(CONFIGURE_ARGS_$(MEMORYMODEL))
CONFIGURE_ARGS += --enable-backends=mod
CONFIGURE_ARGS += --enable-overlays=mod

# Disable MySQL Cluster
CONFIGURE_ARGS += --disable-ndb

TEST_SCRIPTS =

PKGFILES_CSWoldapclient  = $(bindir)/.*
PKGFILES_CSWoldapclient += $(mandir)/man1/.*

PKGFILES_CSWoldapdevel  = $(PKGFILES_DEVEL)
PKGFILES_CSWoldapdevel += $(mandir)/man3/.*

PKGFILES_CSWoldaprt  = $(PKGFILES_RT)
PKGFILES_CSWoldaprt += $(sysconfdir)/ldap.conf
PKGFILES_CSWoldaprt += $(mandir)/man5/ldap.conf.5

INITSMF = /etc/opt/csw/init.d/cswopenldap
#PROTOTYPE_FILTER = awk '$$$$3 ~/\/init.d\/cswopenldap$$$$/ { $$$$2 = "cswinitsmf" } { print }'

include gar/category.mk

CFLAGS := $(filter-out -I%,$(CFLAGS))
DIRECTORY_EXPORTS := $(filter-out includedir,$(DIRECTORY_EXPORTS))

post-merge:
	ginstall -D $(DOWNLOADDIR)/cswopenldap \
		$(PKGROOT)/etc/opt/csw/init.d/cswopenldap
	$(foreach F,$(EXTRA_DOCS),ginstall -D $(DOWNLOADDIR)/$F $(PKGROOT)$(docdir)/$(GARNAME)/$F;)
	#@$(MAKECOOKIE)
