NAME = openldap
VERSION = 2.4.23
CATEGORIES = server
EXTRA_MODULATORS = VERSION
MODULATIONS_VERSION = 2.3.43 2.4.23

DESCRIPTION = Open source implementation of the Lightweight Directory Access Protocol
define BLURB
  The OpenLDAP Project is a collaborative effort to develop a robust,
  commercial-grade, fully featured, and open source LDAP suite of applications
  and development tools. The project is managed by a worldwide community of
  volunteers that use the Internet to communicate, plan, and develop the
  OpenLDAP Suite and its related documentation.
endef

MASTER_SITES = ftp://ftp.openldap.org/pub/OpenLDAP/openldap-release/
SOURCEFILES  = $(foreach VERSION,$(MODULATIONS_VERSION),$(NAME)-$(VERSION).tgz)
DISTFILES  = $(SOURCEFILES)
DISTFILES += CSWoldap.postinstall
DISTFILES += README.CSW openldaprc
DISTFILES += cswopenldap openldap.xml

EXPANDVARS = cswopenldap
EXPANDVARS += CSWoldap.postinstall

PATCHFILES_isa-sparcv8-version-2.4.23 = patch-oldap-2.4.16-ntlm.diff
PATCHFILES_isa-sparcv9-version-2.4.23 = patch-oldap-2.4.16-ntlm.diff
PATCHFILES_isa-i386-version-2.4.23 = patch-oldap-2.4.16-ntlm.diff
PATCHFILES_isa-amd64-version-2.4.23 = patch-oldap-2.4.16-ntlm.diff
PATCHFILES += patch-libtool-64bit.diff
DISTFILES += patch-oldap-2.4.16-ntlm.diff

# Maybe in
#   /opt/csw/share/man/man5/ldap.conf.5
# the string
#   /usr/local/var/ldapi
# should be replaced by something more sane in the future.

NOEXTRACT = $(filter-out $(NAME)-$(VERSION).tgz,$(SOURCEFILES))

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

RUNTIME_DEP_PKGS_CSWoldap  = CSWbdb48 CSWlibnet
RUNTIME_DEP_PKGS_CSWoldap += CSWlibltdl7
RUNTIME_DEP_PKGS_CSWoldap += CSWosslrt CSWsasl CSWtcpwrap CSWunixodbc
RUNTIME_DEP_PKGS_CSWoldap += CSWlibicu CSWperl
RUNTIME_DEP_PKGS_CSWoldap += CSWoldaprt
RUNTIME_DEP_PKGS_CSWoldapclient = CSWlibnet CSWosslrt CSWsasl 
RUNTIME_DEP_PKGS_CSWoldapclient += CSWoldaprt
RUNTIME_DEP_PKGS_CSWoldaprt = CSWlibnet CSWosslrt CSWsasl 

SPKG_SOURCEURL = http://www.openldap.org

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

EXTRA_DOCS = README.CSW $(PATCHFILES) openldaprc

# This is old, stick to BerkeleyDB 4.4
EXTRA_LIB_version-2.3.43 = $(prefix)/bdb44/lib 
EXTRA_INC_version-2.3.43 = $(prefix)/bdb44/include

# This is also used during EXPANDVARS
bdbdir = $(prefix)/bdb48
EXTRA_LIB_version-2.4.23 = $(bdbdir)/lib 
EXTRA_INC_version-2.4.23 = $(bdbdir)/include
EXTRA_LIB = $(EXTRA_LIB_version-$(VERSION))
EXTRA_INC = $(EXTRA_INC_version-$(VERSION))

# Not released yet.
#EXTRA_LDFLAGS = -L$(libdir)/libnet-new

sysconfdir = /etc/opt/csw
localstatedir = /var/opt/csw

MIGRATE_FILES = openldap

# Is this causing this?
#   https://www.opencsw.org/mantis/view.php?id=4555
NOISALIST = 1
LD_OPTIONS =
EXTRA_LINKER_FLAGS = $(RUNPATH_LINKER_FLAGS)

NODIRPATHS = --docdir

BUILD64 = 1
CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --enable-crypt
CONFIGURE_ARGS += --enable-lmpasswd
CONFIGURE_ARGS += --enable-modules
CONFIGURE_ARGS += --enable-rlookups
CONFIGURE_ARGS += --enable-slp
CONFIGURE_ARGS += --enable-backends=mod
CONFIGURE_ARGS += --enable-overlays=mod

# Is the absence of this arg causing https://www.opencsw.org/mantis/view.php?id=4468 ?
CONFIGURE_ARGS += --enable-dynamic

# Disable MySQL Cluster
CONFIGURE_ARGS += --disable-ndb

# Disable TCPwrappers in 64 bit until the libraries are available
#   <http://opencsw.org/mantis/view.php?id=3748>
CONFIGURE_ARGS_32 = --enable-wrappers
# spasswd requires Cyrus SASL
CONFIGURE_ARGS_32 += --enable-spasswd

# Disable Cyrus SASL in 64 bit until the libraries are available
#   <http://opencsw.org/mantis/view.php?id=3749>
CONFIGURE_ARGS_64 += --without-cyrus-sasl

# We have Perl only for 32 bit:
#   <http://opencsw.org/mantis/view.php?id=4484>
CONFIGURE_ARGS_32 += --enable-perl=mod
CONFIGURE_ARGS_64 += --enable-perl=no

CONFIGURE_ARGS += $(CONFIGURE_ARGS_$(MEMORYMODEL))

SKIPTEST ?= 1

MERGE_SCRIPTS_isa-default-version-2.3.43 = copy-only
MERGE_DIRS_isa-default-version-2.3.43 = $(libdir)
MERGE_SCRIPTS_isa-default64-version-2.3.43 = copy-relocated-only
MERGE_DIRS_isa-default64-version-2.3.43 = $(libdir)

MERGE_SCRIPTS_isa-default-version-2.4.23 = copy-all
MERGE_SCRIPTS_isa-default64-version-2.4.23 = copy-relocated-only
MERGE_DIRS_isa-default64-version-2.4.23 = $(bindir) $(sbindir) $(libexecdir) $(libdir)

# Perl backend is built, although it has been told not to.
EXTRA_PAX_ARGS = -s ,.*/opt/csw/libexec/sparcv9/openldap/back_perl.*,,
EXTRA_PAX_ARGS = -s ,.*/opt/csw/libexec/amd64/openldap/back_perl.*,,

# Make sure we do not use the 2.3 .so-links in any case
EXTRA_MERGE_EXCLUDE_FILES_isa-i386-version-2.3.43 = .*\.so
EXTRA_MERGE_EXCLUDE_FILES_isa-amd64-version-2.3.43 = .*\.so
EXTRA_MERGE_EXCLUDE_FILES_isa-sparcv8-version-2.3.43 = .*\.so
EXTRA_MERGE_EXCLUDE_FILES_isa-sparcv9-version-2.3.43 = .*\.so

# These are the config templates. As we have preserveconf which takes
# care of this we exclude them in the package.
EXTRA_MERGE_EXCLUDE_FILES = .*\.default

PRESERVECONF  = /etc/opt/csw/openldap/ldap.conf
PRESERVECONF += /etc/opt/csw/openldap/slapd.conf

PKGFILES_CSWoldapclient  = $(bindir)/.*
PKGFILES_CSWoldapclient += $(mandir)/man1/.*

PKGFILES_CSWoldapdevel  = $(PKGFILES_DEVEL)
PKGFILES_CSWoldapdevel += $(mandir)/man3/.*

PKGFILES_CSWoldaprt  = $(PKGFILES_RT)
PKGFILES_CSWoldaprt += $(sysconfdir)/ldap.conf
PKGFILES_CSWoldaprt += $(mandir)/man5/ldap.conf.5

INITSMF = /opt/csw/etc/init.d/cswopenldap

CHECKPKG_OVERRIDES_CSWoldap += init-file-wrong-location|/opt/csw/etc/init.d/cswopenldap

# New libnet not released yet
CHECKPKG_OVERRIDES_CSWoldap += deprecated-library
CHECKPKG_OVERRIDES_CSWoldapclient += deprecated-library
CHECKPKG_OVERRIDES_CSWoldaprt += deprecated-library

# Split libraries later
CHECKPKG_OVERRIDES_CSWoldaprt += non-uniform-lib-versions-in-package

# These are all overrides because the new libnet is not in place yet.
CHECKPKG_OVERRIDES_CSWoldapclient += soname-not-found|libnet.so|is|needed|by|opt/csw/bin/ldapdelete
CHECKPKG_OVERRIDES_CSWoldapclient += soname-not-found|libnet.so|is|needed|by|opt/csw/bin/ldappasswd
CHECKPKG_OVERRIDES_CSWoldapclient += soname-not-found|libnet.so|is|needed|by|opt/csw/bin/ldapmodrdn
CHECKPKG_OVERRIDES_CSWoldapclient += soname-not-found|libnet.so|is|needed|by|opt/csw/bin/ldapmodify
CHECKPKG_OVERRIDES_CSWoldapclient += soname-not-found|libnet.so|is|needed|by|opt/csw/bin/ldapwhoami
CHECKPKG_OVERRIDES_CSWoldapclient += soname-not-found|libnet.so|is|needed|by|opt/csw/bin/ldapexop
CHECKPKG_OVERRIDES_CSWoldapclient += soname-not-found|libnet.so|is|needed|by|opt/csw/bin/ldapcompare
CHECKPKG_OVERRIDES_CSWoldapclient += soname-not-found|libnet.so|is|needed|by|opt/csw/bin/ldapsearch
CHECKPKG_OVERRIDES_CSWoldapclient += soname-not-found|libnet.so|is|needed|by|opt/csw/bin/ldapurl
CHECKPKG_OVERRIDES_CSWoldapclient += surplus-dependency|CSWlibnet
CHECKPKG_OVERRIDES_CSWoldaprt += soname-not-found|libnet.so|is|needed|by|opt/csw/lib/libldap_r-2.3.so.0.2.31
CHECKPKG_OVERRIDES_CSWoldaprt += soname-not-found|libnet.so|is|needed|by|opt/csw/lib/liblber-2.4.so.2.5.6
CHECKPKG_OVERRIDES_CSWoldaprt += soname-not-found|libnet.so|is|needed|by|opt/csw/lib/libldap-2.3.so.0.2.31
CHECKPKG_OVERRIDES_CSWoldaprt += soname-not-found|libnet.so|is|needed|by|opt/csw/lib/libldap_r-2.4.so.2.5.6
CHECKPKG_OVERRIDES_CSWoldaprt += soname-not-found|libnet.so|is|needed|by|opt/csw/lib/libldap-2.4.so.2.5.6
CHECKPKG_OVERRIDES_CSWoldaprt += surplus-dependency|CSWlibnet
CHECKPKG_OVERRIDES_CSWoldap += soname-not-found|libnet.so|is|needed|by|opt/csw/libexec/slapd
CHECKPKG_OVERRIDES_CSWoldap += surplus-dependency|CSWlibnet


include gar/category.mk

CFLAGS := $(filter-out -I%,$(CFLAGS))
DIRECTORY_EXPORTS := $(filter-out includedir,$(DIRECTORY_EXPORTS))

post-merge:
	ginstall -D $(WORKDIR)/cswopenldap \
		$(PKGROOT)/opt/csw/etc/init.d/cswopenldap
	$(foreach F,$(EXTRA_DOCS),ginstall --mode=644 -D $(WORKDIR)/$F $(PKGROOT)$(docdir)/$(NAME)/$F;)
	@# Enable BDB backend so OpenLDAP can start
	perl -pi -e 's/#\s*(modulepath)/$$1/; s/#\s*(moduleload\s*back_bdb.la)/$$1/' $(PKGROOT)$(sysconfdir)/openldap/slapd.conf
	@$(MAKECOOKIE)
