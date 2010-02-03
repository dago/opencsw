#
# Define Package Dependencies
#

RUNTIME_DEP_PKGS_CSWphp4bcmath   = CSWphp4cgi
RUNTIME_DEP_PKGS_CSWphp4bz2      = CSWphp4cgi CSWbzip2
RUNTIME_DEP_PKGS_CSWphp4calendar = CSWphp4cgi 
RUNTIME_DEP_PKGS_CSWphp4cgi      = CSWbdb44 CSWexpat
RUNTIME_DEP_PKGS_CSWphp4curl     = CSWphp4cgi CSWcurlrt CSWlibidn 
RUNTIME_DEP_PKGS_CSWphp4curl    += CSWoldaprt CSWosslrt CSWzlib
RUNTIME_DEP_PKGS_CSWphp4dba      = CSWphp4cgi CSWbdb44 CSWgdbm
RUNTIME_DEP_PKGS_CSWphp4dbase    = CSWphp4cgi
RUNTIME_DEP_PKGS_CSWphp4domxml   = CSWphp4cgi CSWiconv CSWlibxml2 
RUNTIME_DEP_PKGS_CSWphp4domxml  += CSWlibxslt CSWzlib
RUNTIME_DEP_PKGS_CSWphp4gd       = CSWphp4cgi CSWgd CSWjpeg CSWpng CSWzlib
RUNTIME_DEP_PKGS_CSWphp4gettext  = CSWphp4cgi CSWggettextrt
RUNTIME_DEP_PKGS_CSWphp4gmp      = CSWphp4cgi CSWlibgmp
RUNTIME_DEP_PKGS_CSWphp4iconv    = CSWphp4cgi 
RUNTIME_DEP_PKGS_CSWphp4imap     = CSWphp4cgi CSWimaprt CSWkrb5lib CSWosslrt
RUNTIME_DEP_PKGS_CSWphp4ldap     = CSWphp4cgi CSWoldaprt
RUNTIME_DEP_PKGS_CSWphp4mbstring = CSWphp4cgi 
RUNTIME_DEP_PKGS_CSWphp4mcal     = CSWphp4cgi
RUNTIME_DEP_PKGS_CSWphp4mssql    = CSWphp4cgi CSWfreetds
RUNTIME_DEP_PKGS_CSWphp4mysql    = CSWphp4cgi CSWmysql5rt
RUNTIME_DEP_PKGS_CSWphp4ncurses  = CSWphp4cgi CSWncurses
RUNTIME_DEP_PKGS_CSWphp4odbc     = CSWphp4cgi CSWunixodbc
RUNTIME_DEP_PKGS_CSWphp4openssl  = CSWphp4cgi CSWkrb5lib CSWosslrt
RUNTIME_DEP_PKGS_CSWphp4pgsql    = CSWphp4cgi CSWlibpq
RUNTIME_DEP_PKGS_CSWphp4zlib     = CSWphp4cgi CSWzlib
RUNTIME_DEP_PKGS_CSWap2modphp4   = CSWphp4cgi CSWbdb44 CSWexpat CSWap2prefork
RUNTIME_DEP_PKGS_CSWmodphp4      = CSWphp4cgi CSWbdb44 CSWexpat CSWapache
RUNTIME_DEP_PKGS_CSWphp  = CSWphp4cgi CSWphp4bcmath CSWphp4bz2 CSWphp4calendar
RUNTIME_DEP_PKGS_CSWphp += CSWphp4curl CSWphp4dba CSWphp4domxml CSWphp4gd
RUNTIME_DEP_PKGS_CSWphp += CSWphp4gettext CSWphp4gmp CSWphp4iconv CSWphp4imap
RUNTIME_DEP_PKGS_CSWphp += CSWphp4ldap CSWphp4mbstring CSWphp4mcal CSWphp4mssql
RUNTIME_DEP_PKGS_CSWphp += CSWphp4mysql CSWphp4ncurses CSWphp4odbc CSWphp4openssl
RUNTIME_DEP_PKGS_CSWphp += CSWphp4pgsql CSWphp4zlib CSWphp4dbase CSWmodphp4
