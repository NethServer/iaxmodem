#!/bin/bash

package=$1
version=$2
mock_cfg=nethserver-rpm-x86_64

rpmbuild --define "_sourcedir ." --define "_specdir ." --define "_builddir ./$mock_cfg/" --define "_srcrpmdir ./$mock_cfg/" --define "_rpmdir ./$mock_cfg/" --define "dist .nh" --define "vendor Nethesis" --define "" \
--define "_source_filedigest_algorithm md5" \
--define "_binary_filedigest_algorithm md5" \
--nodeps  -bs ./$package.spec
mock -r $mock_cfg --configdir=../nethserver-devbox/root/usr/share/nethesis/nethserver-devbox/mock --uniqueext=nsrvbuild -D "dist .nh" -D "vendor Nethesis"  --resultdir=./$mock_cfg/ --rebuild ./nethserver-rpm-x86_64/$package-$version.src.rpm

