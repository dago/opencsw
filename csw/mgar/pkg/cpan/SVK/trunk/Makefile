NAME = SVK
VERSION = 2.2.3
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = CLKAO

DESCRIPTION = A distributed version control system
define BLURB
  SVK is a decentralized version control system written in Perl. It uses the
  Subversion filesystem but provides additional features.
endef

DISTFILES += COPYING

RUNTIME_DEP_PKGS  = CSWpmalgannotate CSWpmalgdiff CSWpmappcli CSWpmclone CSWpmclsaccessor CSWpmclsautouse
RUNTIME_DEP_PKGS += CSWpmclsdtainherit CSWpmiocompress CSWpmdatahier CSWpmfiletype CSWpmfreezethaw CSWpmiodigest
RUNTIME_DEP_PKGS += CSWpmiopager CSWpmlclemktxtlex CSWpmlclemktxtsimple CSWpmlistmoreutils CSWpmlog4perl
RUNTIME_DEP_PKGS += CSWpmpathclass CSWpmperlioeol CSWpmperlioviadyn CSWpmperlioviasym
RUNTIME_DEP_PKGS += CSWpmpodsimple CSWpmregexpshellish CSWpmsvn CSWpmsvnmirror CSWpmsvnsimple CSWpmtermreadkey
RUNTIME_DEP_PKGS += CSWpmtimedate CSWpmunivrequire CSWpmuri CSWpmyaml CSWpmyamlsyck

MODDIST = $(NAME)-v$(VERSION).tar.gz
WORKSRC = $(WORKDIR)/$(NAME)-v$(VERSION)

PACKAGES = CSWsvk
CATALOGNAME = svk
ARCHALL = 1

SKIPTEST = 1

include gar/category.mk
