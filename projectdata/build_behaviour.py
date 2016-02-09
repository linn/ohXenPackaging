# Defines the build behaviour for continuous integration builds.

import sys
import os
import shutil
import glob

try:
    from ci import (OpenHomeBuilder, require_version)
except ImportError:
    print "You need to update ohDevTools."
    sys.exit(1)

require_version(45)


class Builder(OpenHomeBuilder):
    output_dir = "build/packages"

    def setup(self):
        self.nuget_server = self.env.get('NUGET_SERVER')

    def clean(self):
        if os.path.isdir(self.output_dir):
            shutil.rmtree(self.output_dir)

    def build(self):
        os.makedirs(self.output_dir)
        self.pack_nuget('src/ohXen.nuspec', '.')

    def publish(self):
        self.publish_package_curl(os.path.join('build', 'packages', '*.nupkg'), self.nuget_server)
