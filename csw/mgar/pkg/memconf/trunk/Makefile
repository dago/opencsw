# Delete source files first since they are not versioned
# rm /home/src/memconf*

NAME = memconf
VERSION = 3.08
GARTYPE = v2

DESCRIPTION = Perl script that displays memory modules installed
define BLURBpty memory sockets.
endef

MASTER_SITES = http://www.4schmidts.com/unix/
DISTFILES  = $(NAME).gz
DISTFILES += memconf.man
DISTFILES += COPYING

SPKG_DESC = $(DESCRIPTION)
ARCHALL = 1

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS =
TEST_SCRIPTS =
INSTALL_SCRIPTS = custom

# We prepended /opt/csw/bin but keep /usr/local/bin
CHECKPKG_OVERRIDES_CSWmemconf += file-with-bad-content|/usr/local|root/opt/csw/bin/memconf

include gar/category.mk

WORKSRC = $(WORKDIR)
SPKG_SOURCEURL = http://www.4schmidts.com/memconf.html

install-custom:
	@echo " ==> Installing $(NAME) (custom)"
	@rm -rf $(DESTDIR)
	@ginstall -d $(DESTDIR)$(bindir)
	@ginstall -d $(DESTDIR)$(mandir)/man1
	@# Make sure /opt/csw/bin is used before /usr/local/bin, but keep /usr/local/bin anyway
	@cat $(WORKSRC)/$(NAME) | \
		perl -npe 's,(:/usr/local/bin),:$(bindir)$$1,' \
		> $(DESTDIR)$(bindir)/$(NAME)
	@cp $(WORKSRC)/$(NAME).man $(DESTDIR)$(mandir)/man1/$(NAME).1
	@chmod 755 $(DESTDIR)$(bindir)/$(NAME)
	@chmod 644 $(DESTDIR)$(mandir)/man1/$(NAME)