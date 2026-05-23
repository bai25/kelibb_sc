"""Build Ren'Py Android APK using RAPT."""
import sys, os
sys.path.insert(0, 'buildlib')
os.chdir(os.path.dirname(os.path.abspath(__file__)))

import rapt.interface as interface
import rapt.configure as configure
import rapt.build as build

iface = interface.Interface()
os.environ['RENPY_PROJECT'] = os.path.abspath('../projects/goblin')
os.environ['RENPY_BUILD'] = os.path.abspath('build')
print('Configuring...')
configure.configure(iface)
print('Building APK...')
build.build(iface, '--release')
print('BUILD SUCCESS')
