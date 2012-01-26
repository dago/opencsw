NAME = mimedefang
VERSION = 2.71
CATEGORIES = net
GARTYPE = v2

DESCRIPTION = Framework for filtering e-mail using Sendmail milter API, C and Perl
define BLURB
  Framework for filtering e-mail using Sendmail milter API, C and Perl
endef

MASTER_SITES = http://www.mimedefang.com/static/
DISTFILES  = $(NAME)-$(VERSION).tar.gz

SPKG_SOURCEURL = http://www.mimedefang.com

UPSTREAM_MASTER_SITES = http://www.mimedefang.com/static/
UFILES_REGEX = (\d+(?:\.\d+)*)

RUNTIME_DEP_PKGS += CSWperl CSWsendmail CSWlibmilter
RUNTIME_DEP_PKGS += CSWpmmimetools CSWpmiostringy
RUNTIME_DEP_PKGS += CSWpmmimebase64 CSWpmmailtools
RUNTIME_DEP_PKGS += CSWpmdigestsha1 CSWpmhtmlparser

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --with-sendmail=/opt/csw/lib/sendmail
CONFIGURE_ARGS += --with-milterinc=/opt/csw/include
CONFIGURE_ARGS += --with-milterlib=/opt/csw/lib
CONFIGURE_ARGS += --with-spooldir=/var/opt/csw/mimedefang/MIMEDefang
CONFIGURE_ARGS += --with-quarantinedir=/var/opt/csw/mimedefang/MD-Quarantine

# No tests included
SKIPTEST = 1

PROTOTYPE_MODIFIERS = 1
PROTOTYPE_FILES_1 = /var/opt/csw/mimedefang/.*
PROTOTYPE_CLASS_1 = ugfiles
PROTOTYPE_USER_1 = defang
PROTOTYPE_GROUP_1 = defang
PROTOTYPE_PERMS_1 = 0700

INITSMF = /etc/opt/csw/init.d/cswmimedefang
USERGROUP = /etc/opt/csw/pkg/CSWmimedefang/cswusergroup
SAMPLECONF  = /etc/mail/mimedefang-filter /etc/mail/sa-mimedefang.cf   
SAMPLECONF += /etc/opt/csw/pkg/CSWmimedefang/mimedefang
POSTMSG = /opt/csw/share/doc/mimedefang/README.CSW

CHECKPKG_OVERRIDES_CSWmimedefang += surplus-dependency|CSWpmdigestsha1
CHECKPKG_OVERRIDES_CSWmimedefang += surplus-dependency|CSWpmiostringy
CHECKPKG_OVERRIDES_CSWmimedefang += surplus-dependency|CSWsendmail
CHECKPKG_OVERRIDES_CSWmimedefang += surplus-dependency|CSWlibmilter
CHECKPKG_OVERRIDES_CSWmimedefang += surplus-dependency|CSWpmmimebase64
CHECKPKG_OVERRIDES_CSWmimedefang += surplus-dependency|CSWpmmailtools
CHECKPKG_OVERRIDES_CSWmimedefang += surplus-dependency|CSWpmmimetools
CHECKPKG_OVERRIDES_CSWmimedefang += surplus-dependency|CSWpmhtmlparser

include gar/category.mk

DOCLIST = Changelog README README.NONROOT README.SECURITY README.SOPHIE README.SPAMASSASSIN README.VEXIRA examples contrib SpamAssassin tests gen-ip-validator.pl

post-install-modulated:
	@echo " ==> Post-install $(NAME) (custom)"
	@ginstall -m 755 -d $(DESTDIR)/etc/opt/csw/init.d
	@ginstall -m 755 $(FILEDIR)/cswmimedefang $(DESTDIR)/etc/opt/csw/init.d/
	@ginstall -m 755 -d $(DESTDIR)/etc/opt/csw/pkg/CSWmimedefang
	@ginstall -m 444 $(FILEDIR)/cswusergroup $(DESTDIR)/etc/opt/csw/pkg/CSWmimedefang/
	@ginstall -m 644 $(FILEDIR)/mimedefang $(DESTDIR)/etc/opt/csw/pkg/CSWmimedefang/
	@ginstall -m 755 -d $(DESTDIR)$(docdir)/$(NAME)
	@$(foreach DOC,$(DOCLIST),cp -r $(WORKSRC)/$(DOC) $(DESTDIR)$(docdir)/$(NAME);)
	@ginstall -m 444 $(FILEDIR)/README.CSW $(DESTDIR)/opt/csw/share/doc/mimedefang/
	@$(MAKECOOKIE)
