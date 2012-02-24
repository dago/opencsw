# $Id$
#
# Building packages from loose files, laid out in a directory.

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS =
INSTALL_SCRIPTS = loose
TEST_SCRIPTS =

MASTER_SITES += $(sort $(addprefix file://$(LOCAL_SRC)/,$(dir $(FILES))))
DISTFILES    += $(notdir $(FILES))

include gar/gar.mk

ifndef LOCAL_SRC
$(error "Please set the LOCAL_SRC variable to the root of your source code tree")
endif

ifndef FILES
$(error "Please set the FILES variable to the list of files to include")
endif

install-loose:
	$(foreach F,$(FILES),ginstall \
		-d $(DESTDIR)$(prefix)/$(dir $F) \
		&& ginstall $(WORKDIR)/$(notdir $F) \
		$(DESTDIR)$(prefix)/$(dir $F);)
	@$(MAKECOOKIE)
