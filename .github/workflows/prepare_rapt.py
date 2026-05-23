"""Prepare RAPT project assets for Android build."""
import os, shutil, json

REPO = os.environ['GITHUB_WORKSPACE']
RENPY = os.path.join(REPO, 'renpy-sdk')
RAPT = os.path.join(RENPY, 'rapt')
ASSETS = os.path.join(RAPT, 'project', 'app', 'src', 'main', 'assets')
GAME = os.path.join(REPO, 'game')

# Clean and recreate
if os.path.exists(ASSETS):
    shutil.rmtree(ASSETS)

os.makedirs(ASSETS)

# 1. x-android.json
android_config = {
    "expansion": False, "google_play_key": None, "google_play_salt": None,
    "heap_size": "3", "icon_name": "可堡灵之校", "include_pil": False,
    "include_sqlite": False, "layout": None, "name": "可堡灵之校",
    "numeric_version": 1, "orientation": "sensorLandscape",
    "package": "com.kebiaoling.school",
    "permissions": ["VIBRATE", "INTERNET"],
    "source": False, "store": "none", "update_always": True,
    "update_icons": True, "update_keystores": True, "version": "0.2-alpha"
}
with open(os.path.join(ASSETS, 'x-android.json'), 'w') as f:
    json.dump(android_config, f, ensure_ascii=False)

# 2. Copy game files with x- prefix
def copy_with_prefix(src, dst, prefix='x-'):
    """Copy files/dirs from src to dst with prefix added to names."""
    if not os.path.exists(src):
        return
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, prefix + item)
        if os.path.isdir(s):
            shutil.copytree(s, d)
        else:
            shutil.copy2(s, d)

# Script files (compiled .rpyc)
for f in ['script.rpyc', 'options.rpyc', 'screens.rpyc', 'gui.rpyc']:
    src = os.path.join(GAME, f)
    if os.path.exists(src):
        shutil.copy2(src, os.path.join(ASSETS, 'x-' + f))

# Subdirectories
for subdir in ['images', 'audio', 'gui', 'libs']:
    copy_with_prefix(os.path.join(GAME, subdir), ASSETS)

# Font
ttf_src = os.path.join(GAME, 'SourceHanSansLite.ttf')
if os.path.exists(ttf_src):
    shutil.copy2(ttf_src, os.path.join(ASSETS, 'x-SourceHanSansLite.ttf'))

# TL
tl_src = os.path.join(GAME, 'tl', 'None', 'common.rpym')
if os.path.exists(tl_src):
    os.makedirs(os.path.join(ASSETS, 'x-tl', 'x-None'), exist_ok=True)
    shutil.copy2(tl_src, os.path.join(ASSETS, 'x-tl', 'x-None', 'x-common.rpym'))

# Version
with open(os.path.join(ASSETS, 'x-script_version.txt'), 'w') as f:
    f.write('0.2-alpha')

# 3. Copy Ren'Py engine common files with x- prefix
common_src = os.path.join(RENPY, 'renpy', 'common')
if os.path.exists(common_src):
    copy_with_prefix(common_src, os.path.join(ASSETS, 'x-renpy'), prefix='x-')

# 4. Presplash assets
presplash = os.path.join(GAME, 'images', 'gameover.png')
if os.path.exists(presplash):
    shutil.copy2(presplash, os.path.join(ASSETS, 'android-presplash.jpg'))

download_img = os.path.join(GAME, 'images', 'gate_day.png')
if os.path.exists(download_img):
    shutil.copy2(download_img, os.path.join(ASSETS, 'android-downloading.jpg'))

# 5. Private mp3 (silence or from game)
mp3_src = os.path.join(GAME, 'audio', 'suhuan1.mp3')
if os.path.exists(mp3_src):
    shutil.copy2(mp3_src, os.path.join(ASSETS, 'private.mp3'))

# 6. x-saves
os.makedirs(os.path.join(ASSETS, 'x-saves'), exist_ok=True)

# 7. dexopt
os.makedirs(os.path.join(ASSETS, 'dexopt'), exist_ok=True)

# Count files
total = sum(len(files) for _, _, files in os.walk(ASSETS))
print(f"Assets prepared: {total} files")
