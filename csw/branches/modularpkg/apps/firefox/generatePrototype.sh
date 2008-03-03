#!/opt/csw/bin/bash

# restore the original prototype file
cp prototype.back proto

# delete existing prototype
rm CSWfirefox*.prototype

echo "d none /opt/csw/mozilla ? ? ?" > CSWfirefox.prototype
echo "d none /opt/csw/mozilla/firefox ? ? ?" >> CSWfirefox.prototype
echo "d none /opt/csw/mozilla/firefox/lib ? ? ?" >> CSWfirefox.prototype

echo "d none /opt/csw/mozilla ? ? ?" > CSWfirefoxrt.prototype
echo "d none /opt/csw/mozilla/firefox ? ? ?" >> CSWfirefoxrt.prototype
echo "d none /opt/csw/mozilla/firefox/lib ? ? ?" >> CSWfirefoxrt.prototype

echo "d none /opt/csw/mozilla ? ? ?" > CSWfirefoxdevel.prototype
echo "d none /opt/csw/mozilla/firefox ? ? ?" >> CSWfirefoxdevel.prototype
echo "d none /opt/csw/mozilla/firefox/lib ? ? ?" >> CSWfirefoxdevel.prototype
echo "d none /opt/csw/mozilla/firefox/share ? ? ?" >> CSWfirefoxdevel.prototype

# IDL stuff goes to devel
grep -v /opt/csw/mozilla/firefox/share/idl proto > proto.temp
grep /opt/csw/mozilla/firefox/share/idl proto >> CSWfirefoxdevel.prototype
cp proto.temp proto

# Include stuff goes to devel
grep -v /opt/csw/mozilla/firefox/include proto > proto.temp
grep /opt/csw/mozilla/firefox/include proto >> CSWfirefoxdevel.prototype
cp proto.temp proto

# lib/pkgconfig stuff goes to devel
grep -v /opt/csw/mozilla/firefox/lib/pkgconfig proto > proto.temp
grep /opt/csw/mozilla/firefox/lib/pkgconfig proto >> CSWfirefoxdevel.prototype
cp proto.temp proto

# bin stuff goes to main
grep -v /opt/csw/mozilla/firefox/bin proto > proto.temp
grep /opt/csw/mozilla/firefox/bin proto >> CSWfirefox.prototype
cp proto.temp proto

# lib/chrome stuff goes to main
grep -v /opt/csw/mozilla/firefox/lib/chrome proto > proto.temp
grep /opt/csw/mozilla/firefox/lib/chrome proto >> CSWfirefox.prototype
cp proto.temp proto

# lib/components stuff goes to main
grep -v /opt/csw/mozilla/firefox/lib/components proto > proto.temp
grep /opt/csw/mozilla/firefox/lib/components proto >> CSWfirefox.prototype
cp proto.temp proto

# lib/defaults stuff goes to main
grep -v /opt/csw/mozilla/firefox/lib/defaults proto > proto.temp
grep /opt/csw/mozilla/firefox/lib/defaults proto >> CSWfirefox.prototype
cp proto.temp proto

# lib/dictionnaries stuff goes to main
grep -v /opt/csw/mozilla/firefox/lib/dictionnaries proto > proto.temp
grep /opt/csw/mozilla/firefox/lib/dictionanries proto >> CSWfirefox.prototype
cp proto.temp proto

# lib/extensions stuff goes to main
grep -v /opt/csw/mozilla/firefox/lib/extensions proto > proto.temp
grep /opt/csw/mozilla/firefox/lib/extensions proto >> CSWfirefox.prototype
cp proto.temp proto

# lib/greprefs stuff goes to main
grep -v /opt/csw/mozilla/firefox/lib/greprefs proto > proto.temp
grep /opt/csw/mozilla/firefox/lib/greprefs proto >> CSWfirefox.prototype
cp proto.temp proto

# lib/icons stuff goes to main
grep -v /opt/csw/mozilla/firefox/lib/icons proto > proto.temp
grep /opt/csw/mozilla/firefox/lib/icons proto >> CSWfirefox.prototype
cp proto.temp proto

# lib/init.d stuff goes to main
grep -v /opt/csw/mozilla/firefox/lib/init.d proto > proto.temp
grep /opt/csw/mozilla/firefox/lib/init.d proto >> CSWfirefox.prototype
cp proto.temp proto

# lib/plugins stuff goes to main
grep -v /opt/csw/mozilla/firefox/lib/plugins proto > proto.temp
grep /opt/csw/mozilla/firefox/lib/plugins proto >> CSWfirefox.prototype
cp proto.temp proto

# lib/res stuff goes to main
grep -v /opt/csw/mozilla/firefox/lib/res proto > proto.temp
grep /opt/csw/mozilla/firefox/lib/res proto >> CSWfirefox.prototype
cp proto.temp proto

# lib/searchplugins stuff goes to main
grep -v /opt/csw/mozilla/firefox/lib/searchplugins proto > proto.temp
grep /opt/csw/mozilla/firefox/lib/searchplugins proto >> CSWfirefox.prototype
cp proto.temp proto

# share stuff goes to main
grep -v /opt/csw/mozilla/firefox/share proto > proto.temp
grep /opt/csw/mozilla/firefox/share proto >> CSWfirefox.prototype
cp proto.temp proto

# share stuff goes to main
grep -v /opt/csw/share proto > proto.temp
grep /opt/csw/share proto >> CSWfirefox.prototype
cp proto.temp proto

# bin stuff goes to main
grep -v /opt/csw/bin proto > proto.temp
grep /opt/csw/bin proto >> CSWfirefox.prototype
cp proto.temp proto

# lib/cpu stuff goes to rt
grep -v /opt/csw/mozilla/firefox/lib/cpu proto > proto.temp
grep /opt/csw/mozilla/firefox/lib/cpu proto >> CSWfirefoxrt.prototype
cp proto.temp proto

# lib/lib*.so stuff goes to rt
grep -v /opt/csw/mozilla/firefox/lib/lib proto > proto.temp
grep /opt/csw/mozilla/firefox/lib/lib proto >> CSWfirefoxrt.prototype
cp proto.temp proto

echo "i copyright=CSWfirefox.copyright" >> CSWfirefox.prototype
echo "i depend=CSWfirefox.depend" >> CSWfirefox.prototype
echo "i pkginfo=CSWfirefox.pkginfo" >> CSWfirefox.prototype
echo "i postinstall=CSWfirefox.postinstall" >> CSWfirefox.prototype
echo "i postremove=CSWfirefox.postremove" >> CSWfirefox.prototype

echo "i copyright=CSWfirefoxrt.copyright" >> CSWfirefoxrt.prototype
echo "i depend=CSWfirefoxrt.depend" >> CSWfirefoxrt.prototype
echo "i pkginfo=CSWfirefoxrt.pkginfo" >> CSWfirefoxrt.prototype

echo "i copyright=CSWfirefoxdevel.copyright" >> CSWfirefoxdevel.prototype
echo "i depend=CSWfirefoxdevel.depend" >> CSWfirefoxdevel.prototype
echo "i pkginfo=CSWfirefoxdevel.pkginfo" >> CSWfirefoxdevel.prototype
