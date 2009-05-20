#
# Define Package Dependencies
#

REQUIRED_PKGS_CSWphp4bcmath   = CSWphp4cgi
REQUIRED_PKGS_CSWphp4bz2      = CSWphp4cgi CSWbzip2
REQUIRED_PKGS_CSWphp4calendar = CSWphp4cgi 
REQUIRED_PKGS_CSWphp4cgi      = CSWbdb44 CSWexpat
REQUIRED_PKGS_CSWphp4curl     = CSWphp4cgi CSWcurlrt CSWlibidn 
REQUIRED_PKGS_CSWphp4curl    += CSWoldaprt CSWosslrt CSWzlib
REQUIRED_PKGS_CSWphp4dba      = CSWphp4cgi CSWbdb44 CSWgdbm
REQUIRED_PKGS_CSWphp4domxml   = CSWphp4cgi CSWiconv CSWlibxml2 
REQUIRED_PKGS_CSWphp4domxml  += CSWlibxslt CSWzlib
REQUIRED_PKGS_CSWphp4gd       = CSWphp4cgi CSWgd CSWjpeg CSWpng CSWzlib
REQUIRED_PKGS_CSWphp4gettext  = CSWphp4cgi CSWggettextrt
REQUIRED_PKGS_CSWphp4gmp      = CSWphp4cgi CSWlibgmp
REQUIRED_PKGS_CSWphp4iconv    = CSWphp4cgi 
REQUIRED_PKGS_CSWphp4imap     = CSWphp4cgi CSWimaprt CSWkrb5lib CSWosslrt
REQUIRED_PKGS_CSWphp4ldap     = CSWphp4cgi CSWoldaprt
REQUIRED_PKGS_CSWphp4mbstring = CSWphp4cgi 
REQUIRED_PKGS_CSWphp4mcal     = CSWphp4cgi
REQUIRED_PKGS_CSWphp4mssql    = CSWphp4cgi CSWfreetds
REQUIRED_PKGS_CSWphp4mysql    = CSWphp4cgi CSWmysql5rt
REQUIRED_PKGS_CSWphp4ncurses  = CSWphp4cgi CSWncurses
REQUIRED_PKGS_CSWphp4odbc     = CSWphp4cgi CSWunixodbc
REQUIRED_PKGS_CSWphp4openssl  = CSWphp4cgi CSWkrb5lib CSWosslrt
REQUIRED_PKGS_CSWphp4pgsql    = CSWphp4cgi CSWlibpq
REQUIRED_PKGS_CSWphp4zlib     = CSWphp4cgi CSWzlib
REQUIRED_PKGS_CSWap2modphp4   = CSWphp4cgi CSWbdb44 CSWexpat CSWap2prefork
REQUIRED_PKGS_CSWmodphp4core  = CSWphp4cgi CSWbdb44 CSWexpat CSWapache
REQUIRED_PKGS_CSWphp  = CSWphp4cgi CSWphp4bcmath CSWphp4bz2 CSWphp4calendar
REQUIRED_PKGS_CSWphp += CSWphp4curl CSWphp4dba CSWphp4domxml CSWphp4gd
REQUIRED_PKGS_CSWphp += CSWphp4gettext CSWphp4gmp CSWphp4iconv CSWphp4imap
REQUIRED_PKGS_CSWphp += CSWphp4ldap CSWphp4mbstring CSWphp4mcal CSWphp4mssql
REQUIRED_PKGS_CSWphp += CSWphp4mysql CSWphp4ncurses CSWphp4odbc CSWphp4openssl
REQUIRED_PKGS_CSWphp += CSWphp4pgsql CSWphp4zlib CSWmodphp4core
