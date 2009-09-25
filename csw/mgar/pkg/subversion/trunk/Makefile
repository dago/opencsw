GARNAME = subversion
DISTVERSION = 1.6.5
GARVERSION = $(subst -,,$(DISTVERSION))
CATEGORIES = utils

DESCRIPTION = Version control rethought
define BLURB
    The goal of the Subversion project is to build a version control system 
    that is a compelling replacement for CVS in the open source community.
endef

# Vendor site
SPKG_SOURCEURL = http://subversion.tigris.org/

# Release site
MASTER_SITES = http://subversion.tigris.org/downloads/

DISTFILES  = $(GARNAME)-$(DISTVERSION).tar.bz2

# We define upstream file regex so we can be notifed of 
# new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.bz2

EXTRA_LIB = $(SVNLIB) $(prefix)/apache2/lib
EXTRA_INC = $(prefix)/apache2/include

WORKSRC = $(WORKDIR)/$(GARNAME)-$(DISTVERSION)

PACKAGES  = CSWsvn CSWsvn-devel CSWap2svn CSWpmsvn
PACKAGES += CSWpysvn CSWrbsvn CSWjavasvn
ARCHALL_CSWsvn-devel = 1

SPKG_DESC_CSWsvn           = Version control rethought
CATALOGNAME_CSWsvn         = subversion
REQUIRED_PKGS_CSWsvn       = CSWapache2rt CSWbdb CSWexpat CSWggettextrt
REQUIRED_PKGS_CSWsvn      += CSWiconv CSWkrb5lib CSWlibnet CSWneon CSWoldaprt
REQUIRED_PKGS_CSWsvn      += CSWosslrt CSWsasl CSWzlib CSWsqlite3rt
SPKG_DESC_CSWsvn-devel     = Subversion Development Support
CATALOGNAME_CSWsvn-devel   = subversion_devel
REQUIRED_PKGS_CSWsvn-devel = CSWsvn
SPKG_DESC_CSWap2svn        = Subversion Modules for Apache 2.2
CATALOGNAME_CSWap2svn      = ap2_subversion
REQUIRED_PKGS_CSWap2svn    = CSWsvn CSWggettextrt CSWiconv
SPKG_DESC_CSWjavasvn       = Subversion Java Language Binding
CATALOGNAME_CSWjavasvn     = javasvn
REQUIRED_PKGS_CSWjavasvn   = CSWsvn CSWapache2rt CSWneon CSWoldaprt
REQUIRED_PKGS_CSWjavasvn  += CSWbdb CSWexpat CSWggettextrt CSWiconv 
SPKG_DESC_CSWpmsvn         = Subversion Perl Language Binding
CATALOGNAME_CSWpmsvn       = pm_subversion
REQUIRED_PKGS_CSWpmsvn     = CSWsvn CSWperl CSWapache2rt CSWbdb CSWexpat 
REQUIRED_PKGS_CSWpmsvn    += CSWggettextrt CSWiconv CSWoldaprt
SPKG_DESC_CSWpysvn         = Subversion Python Language Binding
CATALOGNAME_CSWpysvn       = pysvn
REQUIRED_PKGS_CSWpysvn     = CSWsvn CSWpython CSWapache2rt CSWbdb CSWexpat 
REQUIRED_PKGS_CSWpysvn    += CSWggettextrt CSWiconv CSWoldaprt
SPKG_DESC_CSWrbsvn         = Subversion Ruby Language Binding
CATALOGNAME_CSWrbsvn       = rbsvn
REQUIRED_PKGS_CSWrbsvn     = CSWsvn CSWruby CSWiconv CSWoldaprt
REQUIRED_PKGS_CSWrbsvn    += CSWapache2rt CSWbdb CSWexpat CSWggettextrt 

PKGFILES_CSWsvn-devel = $(PKGFILES_DEVEL)
PKGFILES_CSWap2svn    = $(prefix)/apache2.*
PKGFILES_CSWjavasvn   = $(SVNLIB)/.*java.*
PKGFILES_CSWpmsvn     = $(libdir)/perl.*
PKGFILES_CSWpmsvn    += $(SVNLIB)/.*perl.*
PKGFILES_CSWpmsvn    += $(mandir)/.*swig_perl.*
PKGFILES_CSWpysvn     = $(libdir)/python.*
PKGFILES_CSWpysvn    += $(SVNLIB)/.*swig_py.*
PKGFILES_CSWrbsvn     = $(libdir)/ruby.*
PKGFILES_CSWrbsvn    += $(SVNLIB)/.*swig_ruby.*

DISTFILES += CSWsvn.checkinstall
DISTFILES += CSWap2svn.postinstall CSWap2svn.preremove
DISTFILES += httpd-svn.conf.CSW svn_access.conf.CSW
DISTFILES += fixme.sh

# Fix: Add java headers for nested classes
# https://lists.ubuntu.com/archives/ubuntu-devel-discuss/2008-June/004633.html
PATCHFILES += javahl_headers_for_nested_classes.diff
PATCHFILES += subversion161.diff

DEPENDS = server/apache2
DEPENDS = lib/neon

NODIRPATHS = --libdir --libexecdir
JDK = /usr/jdk1.5.0_15
EXTRA_INC += $(JDK)/include
SVNLIB = $(prefix)/lib/svn

NOISALIST = 1
LDFLAGS  = -R/opt/csw/lib -L/opt/csw/lib -R/opt/csw/apache2/lib 
LDFLAGS += -L/opt/csw/apache2/lib -L$(SVNLIB) -lintl -liconv 
export LDFLAGS

EXTRA_MERGE_EXCLUDE_FILES = .*\.pyo .*\.pyc
PROTOTYPE_FILTER = awk '$$$$3 ~/.*\.py$$$$/ { $$$$2 = "cswpycompile" } { print }'
SPKG_CLASSES_CSWpysvn = none cswpycompile
REQUIRED_PKGS_CSWpysvn += CSWcswclassutils

CONFIGURE_ARGS  = $(DIRPATHS) --libdir=$(SVNLIB) --libexecdir=$(SVNLIB)
CONFIGURE_ARGS += --disable-mod-activation
CONFIGURE_ARGS += --disable-static
CONFIGURE_ARGS += --with-berkeley-db=db.h:/opt/csw/include:/opt/csw/lib:db
CONFIGURE_ARGS += --enable-javahl
CONFIGURE_ARGS += --with-apr=$(prefix)/apache2/bin/apr-config
CONFIGURE_ARGS += --with-apr-util=$(prefix)/apache2/bin/apu-config
CONFIGURE_ARGS += --with-apxs=$(prefix)/apache2/sbin/apxs
CONFIGURE_ARGS += --with-jdk=$(JDK)
CONFIGURE_ARGS += --with-sasl=$(prefix)
CONFIGURE_ARGS += --with-ssl=$(prefix)
CONFIGURE_ARGS += --with-zlib=$(prefix)

TEST_TARGET = check
# Tests take *forever*
TEST_SCRIPTS = skip

test-skip:
	@$(MAKECOOKIE)

include gar/category.mk

BINDING_LANGS   = java perl python ruby
BINDING_TARGETS = $(foreach LANG,$(BINDING_LANGS),svn-$(LANG))

PI_DEPENDS  = install-extras
PI_DEPENDS += fix-ra_dav
PI_DEPENDS += $(BINDING_TARGETS)
PI_DEPENDS += copy-templates
PI_DEPENDS += fix-install

post-install-modulated: $(PI_DEPENDS)
	$(MAKECOOKIE)

post-configure-modulated:
	@echo "~~~ Fixing Libtool ~~~"
	@$(DOWNLOADDIR)/fixme.sh $(WORKSRC)
	@echo "~~~ Creating GCC Makefile and libtool for javahl and ruby ~~~"
	@gcp $(WORKSRC)/Makefile $(WORKSRC)/Makefile.gcc
	@gcp $(WORKSRC)/libtool $(WORKSRC)/libtool.gcc
	@perl -i -pe 's/-mt\|*//' $(WORKSRC)/*.gcc
	@perl -i -pe 's|-xO3|-pipe -O2|' $(WORKSRC)/*.gcc
	@perl -i -pe 's|/opt/studio/SOS11/SUNWspro/bin/cc|/opt/csw/gcc4/bin/gcc|' \
		             $(WORKSRC)/*.gcc
	@perl -i -pe 's|/opt/studio/SOS11/SUNWspro/bin/CC|/opt/csw/gcc4/bin/g++|' \
		             $(WORKSRC)/*.gcc
	@perl -i -pe 's|libtool|libtool.gcc|' $(WORKSRC)/Makefile.gcc
	@perl -i -pe 's|KPIC|fPIC|' $(WORKSRC)/libtool.gcc
	@perl -i -pe 's|postdeps=.*|postdeps=""|' $(WORKSRC)/libtool.gcc
	@( if [ "`uname -p`" = "sparc" ]; then \
    	perl -i -pe 's|-xarch=v8|-mcpu=v8|' $(WORKSRC)/*.gcc; \
	else \
	    perl -i -pe 's|-xarch=386|-march=i386|' $(WORKSRC)/*.gcc; \
	fi )
	$(MAKECOOKIE)

fix-install:
	@(grm -fr $(DESTDIR)$(prefix)/lib/perl/5.8.8)

copy-templates:
	ginstall -d $(DESTDIR)$(prefix)/apache2/etc/extra
	ginstall -m 0644 \
		$(WORKDIR)/httpd-svn.conf.CSW \
		$(DESTDIR)$(prefix)/apache2/etc/extra
	ginstall -m 0644 \
		$(WORKDIR)/svn_access.conf.CSW \
		$(DESTDIR)$(prefix)/apache2/etc
	$(MAKECOOKIE)

fix-ra_dav:
	@# libsvn_ra_dav-1* has been renamed to libsvn_ra_neon-1* 
	@# in the new versions of subversion, 
	@# we need to link for backward compatability
	@(gln -s $(DESTDIR)$(libdir)/libsvn_ra_neon-1.so.0.0.0 \
		$(DESTDIR)$(libdir)/libsvn_ra_dav-1.so.0)
	@(gln -s $(DESTDIR)$(libdir)/libsvn_ra_neon-1.so.0.0.0 \
		$(DESTDIR)$(libdir)/libsvn_ra_dav-1.so)
	@$(MAKECOOKIE)

install-extras:
	@(ginstall -d $(DESTDIR)$(docdir)/subversion/tools)
	@(ginstall -d $(DESTDIR)$(docdir)/subversion/contrib)
	@(gcp -R $(WORKSRC)/tools/* $(DESTDIR)$(docdir)/subversion/tools/)
	@(gcp -R $(WORKSRC)/contrib/* $(DESTDIR)$(docdir)/subversion/contrib/)
	@$(BUILD_ENV) $(INSTALL_ENV) gmake -C $(WORKSRC) install-tools
	@$(BUILD_ENV) $(INSTALL_ENV) gmake -C $(WORKSRC) install-contrib
	@$(MAKECOOKIE)

svn-python:
	@echo " ==> Building Python bindings"
	@touch \
		$(WORKSRC)/subversion/bindings/swig/python/*.c \
		$(WORKSRC)/subversion/bindings/swig/python/*.py
	@$(BUILD_ENV)   gmake -C $(WORKSRC) swig-py
	@$(INSTALL_ENV) gmake -C $(WORKSRC) install-swig-py 
	$(MAKECOOKIE)

svn-perl:
	@echo " ==> Building Perl bindings"
	@touch \
		$(WORKSRC)/subversion/bindings/swig/perl/native/*.c \
		$(WORKSRC)/subversion/bindings/swig/perl/native/*.pm
	@$(BUILD_ENV)   gmake -C $(WORKSRC) swig-pl
	@$(INSTALL_ENV) gmake DESTDIR=$(DESTDIR) -C $(WORKSRC) install-swig-pl
	$(MAKECOOKIE)

svn-ruby:
	@echo " ==> Building Ruby bindings"
	@touch $(WORKSRC)/subversion/bindings/swig/ruby/*.c
	$(BUILD_ENV) gmake -f Makefile.gcc -C $(WORKSRC) swig-rb
	@$(INSTALL_ENV) gmake -f Makefile.gcc -C $(WORKSRC) install-swig-rb
	$(MAKECOOKIE)

svn-java:
	@echo " ==> Building Java bindings"
	@touch $(WORKSRC)/subversion/bindings/javahl/native/*.c
	$(BUILD_ENV)   gmake -C $(WORKSRC) javahl;
	$(INSTALL_ENV) gmake -C $(WORKSRC) install-javahl;
	$(MAKECOOKIE)


