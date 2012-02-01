#!/opt/csw/bin/bash

set -x
set -u
set -e

readonly arch=$1
readonly workdir=$2
readonly pkgroot=$3
readonly libdir="/opt/csw/lib"
readonly v="2.3.so.0.2.31"
readonly libnames=(liblber libldap libldap_r)

function get_soname {
  /usr/ccs/bin/dump -Lv "${1}" \
    | gawk '$2 == "SONAME" {print $3}'
}

ginstall -d -m 755 ${pkgroot}${libdir}
if [[ "$arch" == i386 ]]; then
  ginstall -d -m 755 ${pkgroot}${libdir}/amd64
  for l in "${libnames[@]}"; do
    destf="${pkgroot}${libdir}/${l}-${v}"
    ginstall -m 755 "${workdir}/${l}-${v}-i386" "${destf}"
    soname=$(get_soname "${destf}")
    if [[ ! -h "${pkgroot}${libdir}/${soname}" ]]; then
      gln -sv "${l}-${v}" "${pkgroot}${libdir}/${soname}"
    fi
    [[ -h "${pkgroot}${libdir}/${soname}" ]]

    ginstall -m 755 "${workdir}/${l}-${v}-amd64" "${pkgroot}${libdir}/amd64/${l}-${v}"
    if [[ ! -h "${pkgroot}${libdir}/amd64/${soname}" ]]; then
      gln -sv "${l}-${v}" "${pkgroot}${libdir}/amd64/${soname}"
    fi
    [[ -h "${pkgroot}${libdir}/amd64/${soname}" ]]
  done
elif [[ "$arch" == sparc ]]; then
  ginstall -d -m 755 ${pkgroot}${libdir}/sparcv9
  for l in "${libnames[@]}"; do
    destf="${pkgroot}${libdir}/${l}-${v}"
    ginstall -m 755 ${workdir}/${l}-${v}-sparcv8 ${pkgroot}${libdir}/${l}-${v}
    soname=$(get_soname "${destf}")
    if [[ ! -h "${pkgroot}${libdir}/${soname}" ]]; then
      gln -sv "${l}-${v}" "${pkgroot}${libdir}/${soname}"
    fi
    [[ -h "${pkgroot}${libdir}/${soname}" ]]

    ginstall -m 755 ${workdir}/${l}-${v}-sparcv9 ${pkgroot}${libdir}/sparcv9/${l}-${v}
    if [[ ! -h "${pkgroot}${libdir}/sparcv9/${soname}" ]]; then
      gln -sv "${l}-${v}" "${pkgroot}${libdir}/sparcv9/${soname}"
    fi
    [[ -h "${pkgroot}${libdir}/sparcv9/${soname}" ]]
  done
else
  echo "Wrong architecture '$arch'."
  exit 1
fi
