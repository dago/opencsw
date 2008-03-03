GARNAME = Net-SSH-Perl
GARVERSION = 1.25
CATEGORIES = cpan
AUTHOR = DROLSKY

DESCRIPTION = client Interface to SSH
define BLURB
  Net::SSH::Perl is an all-Perl module implementing an SSH (Secure Shell)
  client. It is compatible with both the SSH-1 and SSH-2 protocols.

  Net::SSH::Perl enables you to simply and securely execute commands on remote
  machines, and receive the STDOUT, STDERR, and exit status of that remote
  command. It contains built-in support for various methods of authenticating
  with the server (password authentication, RSA challenge-response
  authentication, etc.). It completely implements the I/O buffering, packet
  transport, and user authentication layers of the SSH protocol, and makes use
  of external Perl libraries (in the Crypt:: family of modules) to handle
  encryption of all data sent across the insecure network. It can also read
  your existing SSH configuration files (/etc/ssh_config, etc.), RSA identity
  files, DSA identity files, known hosts files, etc.
endef

DISTFILES += CSWpmnetsshperl.gspec CSWpmnetsshperl.depend

DEPENDS += cpan/Crypt-DH cpan/Convert-PEM cpan/Math-GMP cpan/String-CRC32
DEPENDS += cpan/Crypt-DSA cpan/Crypt-Blowfish cpan/Crypt-RSA
DEPENDS += cpan/Digest-BubbleBabble

# Don't prompt during install
PATCHFILES = auto_install.diff

include gar/category.mk
