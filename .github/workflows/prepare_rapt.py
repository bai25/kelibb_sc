"""Prepare RAPT project assets for Android build."""
import os, shutil, json, sys

REPO = os.environ.get('GITHUB_WORKSPACE', os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
RENPY = os.path.join(REPO, 'renpy-sdk')

print(f"REPO: {REPO}")
print(f"RENPY SDK: {RENPY}")
print(f"RENPY exists: {os.path.exists(RENPY)}")
print(f"RENPY/renpy exists: {os.path.exists(os.path.join(RENPY, 'renpy'))}")
print(f"RENPY/renpy/common exists: {os.path.exists(os.path.join(RENPY, 'renpy', 'common'))}")

if os.path.exists(os.path.join(RENPY, 'renpy', 'common')):
    common_files = os.listdir(os.path.join(RENPY, 'renpy', 'common'))
    print(f"Common files: {len(common_files)} ({common_files[0] if common_files else 'empty'})")

RAPT = os.path.join(RENPY, 'rapt')

# Ensure project directory exists (copy from prototype if needed)
PROJECT = os.path.join(RAPT, 'project')

# Look for gradle build files in multiple locations
proto_candidates = [
    os.path.join(RAPT, 'prototype'),
    os.path.join(RAPT, 'rapt', 'prototype'),
    os.path.join(REPO, 'android'),
]

project_setup = False
for proto in proto_candidates:
    if os.path.exists(os.path.join(proto, 'gradlew')):
        print(f"Found gradle project at: {proto}")
        # Copy all files from prototype to project
        for item in os.listdir(proto):
            s = os.path.join(proto, item)
            d = os.path.join(PROJECT, item)
            if os.path.isdir(s):
                shutil.copytree(s, d, dirs_exist_ok=True)
            else:
                os.makedirs(os.path.dirname(d), exist_ok=True)
                shutil.copy2(s, d)
        project_setup = True
        break

if project_setup:
    # RAPT Sdk 已存在 renpy-sdk/rapt/Sdk，project/../Sdk 指向同一路径，无需 symlink
    
    # Copy missing generated files from repo's android/ (Jinja2 templates not rendered in CI)
    generated_files = [
        'app/src/main/AndroidManifest.xml',
        'app/src/main/res/values/strings.xml',
        'renpyandroid/src/main/res/values/strings.xml',
        'renpyandroid/src/main/java/org/renpy/android/Constants.java',
    ]
    repo_android = os.path.join(REPO, 'android')
    for rel_path in generated_files:
        src = os.path.join(repo_android, rel_path)
        dst = os.path.join(PROJECT, rel_path)
        if os.path.exists(src) and not os.path.exists(dst):
            os.makedirs(os.path.dirname(dst), exist_ok=True)
            shutil.copy2(src, dst)
            print(f"  📄 Copied missing: {rel_path}")
    
    print(f"Project gradlew exists: {os.path.exists(os.path.join(PROJECT, 'gradlew'))}")
else:
    print("⚠️  No gradle prototype found anywhere!")

ASSETS = os.path.join(PROJECT, 'app', 'src', 'main', 'assets')
GAME = os.path.join(REPO, 'game')

print(f"GAME exists: {os.path.exists(GAME)}")
print(f"RAPT exists: {os.path.exists(RAPT)}")

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
print("✅ x-android.json")

# 2. Copy game files with x- prefix
# Ren'Py expects: game/<dir>/<file> → assets/x-<dir>/<file>
def copy_subdir(src, dst):
    """Copy a subdir (e.g. game/images/) to assets/x-images/."""
    if not os.path.exists(src):
        print(f"  ⚠️  src not found: {src}")
        return
    name = os.path.basename(src)  # 'images'
    dest = os.path.join(dst, 'x-' + name)  # 'assets/x-images'
    shutil.copytree(src, dest)
    print(f"  📂 x-{name}/ ({sum(len(files) for _, _, files in os.walk(src))} files)")

for f in ['script.rpyc', 'options.rpyc', 'screens.rpyc', 'gui.rpyc']:
    src = os.path.join(GAME, f)
    if os.path.exists(src):
        shutil.copy2(src, os.path.join(ASSETS, 'x-' + f))
    else:
        print(f"  ⚠️  Missing: {f}")

for subdir in ['images', 'audio', 'gui', 'libs']:
    copy_subdir(os.path.join(GAME, subdir), ASSETS)

ttf_src = os.path.join(GAME, 'SourceHanSansLite.ttf')
if os.path.exists(ttf_src):
    shutil.copy2(ttf_src, os.path.join(ASSETS, 'x-SourceHanSansLite.ttf'))

tl_src = os.path.join(GAME, 'tl', 'None', 'common.rpym')
if os.path.exists(tl_src):
    os.makedirs(os.path.join(ASSETS, 'x-tl', 'x-None'), exist_ok=True)
    shutil.copy2(tl_src, os.path.join(ASSETS, 'x-tl', 'x-None', 'x-common.rpym'))

with open(os.path.join(ASSETS, 'x-script_version.txt'), 'w') as f:
    f.write('0.2-alpha')

print("✅ Game files copied")

# 3. Copy Ren'Py engine common files
common_src = os.path.join(RENPY, 'renpy', 'common')
if os.path.exists(common_src):
    renpy_assets = os.path.join(ASSETS, 'x-renpy')
    os.makedirs(renpy_assets, exist_ok=True)
    
    # Walk through all files in common
    for root, dirs, files in os.walk(common_src):
        rel = os.path.relpath(root, common_src)
        if rel == '.':
            dst_dir = renpy_assets
        else:
            dst_dir = os.path.join(renpy_assets, 'x-' + rel)
        
        for f in files:
            src_file = os.path.join(root, f)
            dst_file = os.path.join(dst_dir, 'x-' + f)
            os.makedirs(os.path.dirname(dst_file), exist_ok=True)
            shutil.copy2(src_file, dst_file)
    
    print(f"✅ Engine files: {sum(len(files) for _, _, files in os.walk(renpy_assets))}")
else:
    print(f"⚠️  No renpy/common at {common_src}")

# 4. Presplash
for name, img in [('android-presplash.jpg', 'gameover.png'), ('android-downloading.jpg', 'gate_day.png')]:
    src = os.path.join(GAME, 'images', img)
    if os.path.exists(src):
        shutil.copy2(src, os.path.join(ASSETS, name))

mp3_src = os.path.join(GAME, 'audio', 'suhuan1.mp3')
if os.path.exists(mp3_src):
    shutil.copy2(mp3_src, os.path.join(ASSETS, 'private.mp3'))

# 5. Empty directories
os.makedirs(os.path.join(ASSETS, 'x-saves'), exist_ok=True)
os.makedirs(os.path.join(ASSETS, 'dexopt'), exist_ok=True)

total = sum(len(files) for _, _, files in os.walk(ASSETS))
print(f"\n📊 Assets prepared: {total} files")
