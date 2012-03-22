<?php

$conf['gmetad_root'] = "/var/opt/csw/ganglia";
$conf['rrds'] = "${conf['gmetad_root']}/rrds";
$conf['dwoo_compiled_dir'] = "${conf['gmetad_root']}/dwoo";
$conf['views_dir'] = $conf['gmetad_root'] . '/conf';
$conf['conf_dir'] = $conf['gmetad_root'] . '/conf';

$conf['rrdtool'] = "/opt/csw/bin/rrdtool";
?>
