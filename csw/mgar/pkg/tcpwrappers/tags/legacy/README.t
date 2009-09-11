TCP-Wrappers, from http://www.porcupine.org

Note  that the library is compiled to use LOG_LOCAL1 as the
syslog facility, NOT "LOG_MAIL", the default.

ALSO, it uses /opt/csw/etc/hosts.xxx, NOT /etc/hosts.XXX

man hosts_access(3), hosts_access(5), hosts_options(5)
for syntax on those.

The compile has been hacked to provide a shared-library version instead
of libwrap.a
There is an extra hack, in that there are default variable definitions of
deny_severity and allow_severity, set to 0.
This is to allow for ./configure style tests, that break in the transition
from lib.a to lib.so


Note also that there are TWO versions of libwrap.so: 
libwrap-std.so.1      The "standard" tcp wrapper library
libwrap-ext.so.1      The "extended" tcp wrapper library

By default, /opt/csw/lib/libwrap.so.1 is linked to the std version.
To use the extended syntax in hosts_options(5), you need to change
the link to point to libwrap-ext.so.1
Unfortunately, the syntax for the two versions, is slightly incompatible,
which is why there are two versions.

