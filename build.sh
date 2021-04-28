#!/bin/bash
sudo chmod 775 ./src/DEBIAN/postinst
dpkg-deb --build src graphic-tab-config.deb