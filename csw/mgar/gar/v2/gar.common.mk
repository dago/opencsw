# vim: ft=make ts=4 sw=4 noet
#
# $Id$
#
# Copyright 2006 Cory Omand
#
# Redistribution and/or use, with or without modification, is
# permitted.  This software is without warranty of any kind.  The
# author(s) shall not be liable in the event that use of the
# software causes damage.
#
# gar.common.mk - General routines used by multiple packages.  For instance,
#                 setting up server instances prior to testing.
#

#
# Power up MySQL for testing purposes (used by DBI/DBD CPAN modules)
#
mysql-powerup:
	@echo " ==> Cleaning up mysql directory"
	@( $(DESTDIR)$(sharedstatedir)/mysql/mysql.server stop || true )
	@rm -rf $(DESTDIR)$(localstatedir)
	@echo " ==> Configuring mysql db for tests"
	@$(DESTDIR)$(bindir)/mysql_install_db
	@echo " ==> Adding $(DB_USER) user"
	@if test "X$(shell getent group $(DB_GROUP))" = "X"; then \
		groupadd $(DB_GROUP) ; \
	fi
	@if test "X$(shell getent passwd $(DB_USER))" = "X"; then \
		useradd -g $(DB_GROUP) \
				-d $(DESTDIR)$(localstatedir) \
				-s /bin/false $(DB_USER) ; \
		passwd -l $(DB_USER) ; \
	fi
	@chown -R $(DB_USER):$(DB_GROUP) $(DESTDIR)$(localstatedir)
	@$(DESTDIR)$(sharedstatedir)/mysql/mysql.server start
	@echo " ==> Mysql started and ready for testing"

#
# Power down MySQL after testing (used by DBI/DBD CPAN modules)
#
mysql-powerdown:
	@echo " ==> Cleaning up mysql directory"
	@( $(DESTDIR)$(sharedstatedir)/mysql/mysql.server stop || true )
	@echo " ==> Removing $(DB_USER) user"
	@( userdel $(DB_USER)  || true )
	@( userdel $(DB_GROUP) || true )
	@rm -rf $(DESTDIR)$(localstatedir)

