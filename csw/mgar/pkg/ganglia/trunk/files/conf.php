<?php

$conf['gmetad_root'] = "/var/opt/csw/ganglia";
$conf['rrds'] = "${conf['gmetad_root']}/rrds";
$conf['dwoo_compiled_dir'] = "${conf['gmetad_root']}/dwoo";
$conf['dwoo_cache_dir'] = "${conf['gmetad_root']}/dwoo_cache";
$conf['views_dir'] = $conf['gmetad_root'] . '/conf';
$conf['conf_dir'] = $conf['gmetad_root'] . '/conf';

$conf['overlay_events_file'] = $conf['conf_dir'] . "/events.json";
$conf['overlay_events_color_map_file'] = $conf['conf_dir'] . "/event_color.json";

$conf['rrdtool'] = "/opt/csw/bin/rrdtool";
?>
