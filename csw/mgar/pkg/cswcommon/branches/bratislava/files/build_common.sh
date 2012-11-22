#!/opt/csw/bin/bash

set -x
set -u
set -e

function main {
readonly GARCH=$1
shift
readonly DESTDIR=$1
shift
local prefix="/opt/csw"

mkdir -p "${DESTDIR}${prefix}/bin"
mkdir -p "${DESTDIR}${prefix}/lib"

hooks=(
  postbatchinstall.d
  postbatchremove.d
  postbatchupgrade.d
  postinstall.d
  postremove.d
  postupgrade.d
  prebatchinstall.d
  prebatchremove.d
  prebatchupgrade.d
  preinstall.d
  preremove.d
  preupgrade.d
)

for h in "${hooks[@]}"
do
  ginstall -m 755 -d "${DESTDIR}/etc/opt/csw/pkg-hooks/${h}"
done

base_dirs=(
  /opt/csw
  /opt/csw/bin
  /opt/csw/etc
  /opt/csw/include
  /opt/csw/lib
  /opt/csw/lib/X11
  /opt/csw/lib/X11/app-defaults
  /opt/csw/sbin
  /opt/csw/share
  /opt/csw/share/doc
  /opt/csw/share/info
  /opt/csw/share/locale
  /opt/csw/share/locale/az
  /opt/csw/share/locale/az/LC_MESSAGES
  /opt/csw/share/locale/be
  /opt/csw/share/locale/be/LC_MESSAGES
  /opt/csw/share/locale/bg
  /opt/csw/share/locale/bg/LC_MESSAGES
  /opt/csw/share/locale/ca
  /opt/csw/share/locale/ca/LC_MESSAGES
  /opt/csw/share/locale/cs
  /opt/csw/share/locale/cs/LC_MESSAGES
  /opt/csw/share/locale/da
  /opt/csw/share/locale/da/LC_MESSAGES
  /opt/csw/share/locale/de
  /opt/csw/share/locale/de/LC_MESSAGES
  /opt/csw/share/locale/el
  /opt/csw/share/locale/el/LC_MESSAGES
  /opt/csw/share/locale/en@boldquot
  /opt/csw/share/locale/en@boldquot/LC_MESSAGES
  /opt/csw/share/locale/en@quot
  /opt/csw/share/locale/en@quot/LC_MESSAGES
  /opt/csw/share/locale/es
  /opt/csw/share/locale/es/LC_MESSAGES
  /opt/csw/share/locale/et
  /opt/csw/share/locale/et/LC_MESSAGES
  /opt/csw/share/locale/eu
  /opt/csw/share/locale/eu/LC_MESSAGES
  /opt/csw/share/locale/fi
  /opt/csw/share/locale/fi/LC_MESSAGES
  /opt/csw/share/locale/fr
  /opt/csw/share/locale/fr/LC_MESSAGES
  /opt/csw/share/locale/ga
  /opt/csw/share/locale/ga/LC_MESSAGES
  /opt/csw/share/locale/gl
  /opt/csw/share/locale/gl/LC_MESSAGES
  /opt/csw/share/locale/he
  /opt/csw/share/locale/he/LC_MESSAGES
  /opt/csw/share/locale/hr
  /opt/csw/share/locale/hr/LC_MESSAGES
  /opt/csw/share/locale/hu
  /opt/csw/share/locale/hu/LC_MESSAGES
  /opt/csw/share/locale/id
  /opt/csw/share/locale/id/LC_MESSAGES
  /opt/csw/share/locale/it
  /opt/csw/share/locale/it/LC_MESSAGES
  /opt/csw/share/locale/ja
  /opt/csw/share/locale/ja/LC_MESSAGES
  /opt/csw/share/locale/ko
  /opt/csw/share/locale/ko/LC_MESSAGES
  /opt/csw/share/locale/lt
  /opt/csw/share/locale/lt/LC_MESSAGES
  /opt/csw/share/locale/nl
  /opt/csw/share/locale/nl/LC_MESSAGES
  /opt/csw/share/locale/nn
  /opt/csw/share/locale/nn/LC_MESSAGES
  /opt/csw/share/locale/no
  /opt/csw/share/locale/no/LC_MESSAGES
  /opt/csw/share/locale/pl
  /opt/csw/share/locale/pl/LC_MESSAGES
  /opt/csw/share/locale/pt
  /opt/csw/share/locale/pt/LC_MESSAGES
  /opt/csw/share/locale/pt_BR
  /opt/csw/share/locale/pt_BR/LC_MESSAGES
  /opt/csw/share/locale/ro
  /opt/csw/share/locale/ro/LC_MESSAGES
  /opt/csw/share/locale/ru
  /opt/csw/share/locale/ru/LC_MESSAGES
  /opt/csw/share/locale/sk
  /opt/csw/share/locale/sk/LC_MESSAGES
  /opt/csw/share/locale/sl
  /opt/csw/share/locale/sl/LC_MESSAGES
  /opt/csw/share/locale/sp
  /opt/csw/share/locale/sp/LC_MESSAGES
  /opt/csw/share/locale/sr
  /opt/csw/share/locale/sr/LC_MESSAGES
  /opt/csw/share/locale/sv
  /opt/csw/share/locale/sv/LC_MESSAGES
  /opt/csw/share/locale/tr
  /opt/csw/share/locale/tr/LC_MESSAGES
  /opt/csw/share/locale/uk
  /opt/csw/share/locale/uk/LC_MESSAGES
  /opt/csw/share/locale/vi
  /opt/csw/share/locale/vi/LC_MESSAGES
  /opt/csw/share/locale/wa
  /opt/csw/share/locale/wa/LC_MESSAGES
  /opt/csw/share/locale/zh
  /opt/csw/share/locale/zh/LC_MESSAGES
  /opt/csw/share/locale/zh_CN
  /opt/csw/share/locale/zh_CN.GB2312
  /opt/csw/share/locale/zh_CN.GB2312/LC_MESSAGES
  /opt/csw/share/locale/zh_TW
  /opt/csw/share/locale/zh_TW.Big5
  /opt/csw/share/locale/zh_TW.Big5/LC_MESSAGES
  /opt/csw/share/locale/zh_TW/LC_MESSAGES
  /opt/csw/share/man
  /opt/csw/var
  /var/opt/csw
  /var/opt/csw/pkg-hooks
)

for d in "${base_dirs[@]}"
do
  ginstall -m 755 -d "${DESTDIR}${d}"
done

case ${GARCH} in
  i386)
    dir32="i386"
    dir64="amd64"
    allisas="i486 amd64 pentium pentium_pro"
    ;;
  sparc)
    dir32="sparcv8"
    dir64="sparcv9"
    allisas="sparcv8+ sparcv9"
    ;;
esac

for isa in $allisas
do
  ginstall -m 755 -d "${DESTDIR}${prefix}/bin/$isa"
  ginstall -m 755 -d "${DESTDIR}${prefix}/lib/$isa"
done

ln -s share/doc       ${DESTDIR}/opt/csw/doc
ln -s share/info      ${DESTDIR}/opt/csw/info
ln -s .               ${DESTDIR}/opt/csw/lib/32
ln -s ${dir64}        ${DESTDIR}/opt/csw/lib/64
ln -s .               ${DESTDIR}/opt/csw/lib/${dir32}
ln -s ../share/locale ${DESTDIR}/opt/csw/lib/locale
ln -s share/man       ${DESTDIR}/opt/csw/man

  # 1 f none /opt/csw/share/locale/locale.alias 0644 root bin 2676 12726 1083469567
}

main "$1" "$2"
