import PyInstaller.__main__
import datetime
import os
import re
from shutil import copy, make_archive


def builder(exeName, orgName='The Orange Toolbox', url=None, version='0.0.1', assets=[]):

    builddate = datetime.datetime.now().strftime('%b %d %Y')
    distDir = './dist/' + exeName + '-v' + str(version)
    exeDir = distDir + '/' + exeName
    iconPath = './icon/icon.ico'

    # Write version info into _constants.py resource file
    with open('src/_constants.py', 'w') as f:
        f.write("ORGNAME = \"{}\"\n".format(orgName))
        f.write("NAME = \"{}\"\n".format(exeName))
        f.write("VERSION = \"{}\"\n".format(version))
        f.write("BUILD_DATE = \"{}\"\n".format(builddate))
        f.write("URL = \"{}\"\n".format(url))

    args = ['src/__main__.py',
            '-p', 'src',
            '-n', exeName,
            '-F',
            '--distpath', exeDir,
            '--icon', iconPath]

    # Build!
    assets = assets or []
    PyInstaller.__main__.run(args + assets)

    # include CompilePal plugin configuration
    def add_file(path):
        if os.path.isfile(path):
            copy(path, exeDir)

    add_file('./plugins/compilepal/meta.json')
    add_file('./plugins/compilepal/parameters.json')

    # include README.md
    if os.path.isfile('./README.md'):
        f = open('./README.md')
        re_omit = r'<!--- start txt omit -->.*<!--- end txt omit -->'
        readmetxt = re.sub(re_omit, '', f.read(), flags=re.S)
        f.close()

        f = open(distDir + '/readme.txt', "w+")
        f.seek(0)
        f.write(readmetxt)
        f.truncate()
        f.close()

    # Zip the package
    try:
        os.remove(distDir + '.zip')
    except OSError:
        pass
    make_archive(distDir, 'zip', distDir)
