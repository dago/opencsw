NAME = orainstclient
VERSION = 10.2.0.4.0
CATEGORIES = apps

DESCRIPTION = Oracle Instant Client
define BLURB
endef

# There is no MASTER_SITES because the software must be downloaded
# manually and put into /home/src before packaging.
MASTER_SITES = manual://

DISTFILES_sparc-32-instantclient = basic-10.2.0.4.0-solaris-sparc32.zip
DISTFILES_sparc-32-sdk           = sdk-10.2.0.4.0-solaris-sparc32.zip
DISTFILES_sparc-32-sqlplus       = sqlplus-10.2.0.4.0-solaris-sparc32.zip
DISTFILES_sparc-64-instantclient = basic-10.2.0.4.0-solaris-sparc64.zip
DISTFILES_sparc-64-sdk           = sdk-10.2.0.4.0-solaris-sparc64.zip
DISTFILES_sparc-64-sqlplus       = sqlplus-10.2.0.4.0-solaris-sparc64.zip
DISTFILES_i386-32-instantclient  = instantclient-basic-solaris-x86-6432-10.2.0.2-20060526.zip
DISTFILES_i386-32-sdk            = instantclient-sdk-solaris-x86-6432-10.2.0.2-20060526.zip
DISTFILES_i386-32-sqlplus        = sqlplus-10.2.0.4.0-solaris-x86.zip
DISTFILES_i386-64-instantclient  = instantclient-basic-solaris-x86-64-10.2.0.2-2006-05-26.zip
DISTFILES_i386-64-sdk            = instantclient-sdk-solaris-x86-64-10.2.0.2-2006-05-26.zip
DISTFILES_i386-64-sqlplus        = sqlplus-10.2.0.4.0-solaris-x86-64.zip

DISTFILES  = $(foreach A,sparc i386,$(foreach S,32 64,$(foreach T,instantclient sdk sqlplus,$(DISTFILES_$A-$S-$T))))
NOEXTRACT  = $(filter-out $(foreach S,32 64,$(foreach T,instantclient sdk sqlplus,$(DISTFILES_$(GARCH)-$S-$T)) COPYING),$(DISTFILES))

# From http://www.oracle.com/technology/software/popup-license/instant_client_lic.html
DISTFILES += instant_client_lic.html
# This is done with html2text.pl and some manual aditing from the above
DISTFILES += COPYING

BUILD_DEP_PKGS = CSWchrpath

SPKG_SOURCEURL = http://www.oracle.com/technology/software/tech/oci/instantclient/index.html

PACKAGES = CSWorainstclient102
CATALOGNAME = orainstclient102

# LICENSE = LICENSE


BUILD64_LIBS_ONLY = 1
CONFIGURE_SCRIPTS =
BUILD_SCRIPTS =
TEST_SCRIPTS =
INSTALL_SCRIPTS = custom

# Tell the user to download the file manually
manual//%:
	@echo
	@echo "Please download the file"
	@echo "  $*"
	@echo "manually from"
	@echo "  $(SPKG_SOURCEURL)"
	@echo "and copy it to"
	@echo "  $(GARCHIVEDIR)"
	@echo

define custom-zip-extract
zip-extract-$(1):
	ginstall -d $$(EXTRACTDIR)/$(2)
	unzip $$(DOWNLOADDIR)/$$(notdir $(1)) -d $$(EXTRACTDIR)/$(2)
	@mkdir -p $$(COOKIEDIR)/$$(@D) && date >> $$(COOKIEDIR)/$$@
endef

TARGETDIR_32 = .
TARGETDIR_64 = 64

MERGE_SCRIPTS_isa-default = copy-all
MERGE_SCRIPTS_isa-default64 = copy-all

# Libraries are cluttered all over the place, we can't change that.
CHECKPKG_OVERRIDES_CSWorainstclient102 += binary-architecture-does-not-match-placement

# The runpath entries are for Oracle- and Sun-Cluster and therefor don't conform to OpenCSW specs.
CHECKPKG_OVERRIDES_CSWorainstclient102 += bad-rpath-entry

# The libraries are relocated. It is expected from the client to set
# LD_LIBRARY_PATH as described by Oracle.
CHECKPKG_OVERRIDES_CSWorainstclient102 += soname-not-found

include gar/category.mk

$(foreach A,sparc i386,$(foreach S,32 64,$(foreach T,instantclient sdk sqlplus,$(foreach F,$(DISTFILES_$A-$S-$T),$(eval $(call custom-zip-extract,$F,$A-$S))))))

install-custom:
	@echo " ==> Installing $(NAME)"
	#ginstall -d $(DESTDIR)$(bindir)
	#ginstall $(WORKDIR)/$(GARCH)-$(MEMORYMODEL)/instantclient_10_2/genezi $(DESTDIR)$(bindir)
	#chrpath -r $(libdir) $(DESTDIR)$(bindir)/genezi
	#ginstall -d $(DESTDIR)$(libdir)
	#ginstall $(WORKDIR)/$(GARCH)-$(MEMORYMODEL)/instantclient_10_2/*.so* $(DESTDIR)$(libdir)
	#ginstall $(WORKDIR)/$(GARCH)-$(MEMORYMODEL)/instantclient_10_2/*.jar $(DESTDIR)$(libdir)
	#ginstall -d $(DESTDIR)$(includedir)/oracle/10.2/
	#ginstall $(WORKDIR)/$(GARCH)-$(MEMORYMODEL)/instantclient_10_2/sdk/include/* $(DESTDIR)$(includedir)/oracle/10.2/
	ginstall -d $(DESTDIR)$(prefix)/instantclient_10_2/$(TARGETDIR_$(MEMORYMODEL))
	cp -r $(WORKDIR)/$(GARCH)-$(MEMORYMODEL)/instantclient_10_2/* $(DESTDIR)$(prefix)/instantclient_10_2/$(TARGETDIR_$(MEMORYMODEL))/
	gln -s libclntsh.so.10.1 $(DESTDIR)$(prefix)/instantclient_10_2/$(TARGETDIR_$(MEMORYMODEL))/libclntsh.so
	gln -s libocci.so.10.1 $(DESTDIR)$(prefix)/instantclient_10_2/$(TARGETDIR_$(MEMORYMODEL))/libocci.so
	@$(MAKECOOKIE)
