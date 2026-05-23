## 此文件包含有可自定义您游戏的设置。

## 基础
define config.name = _("可堡灵之校")
define gui.show_name = True
define config.version = "0.1-alpha"

define gui.about = _p("""
""")

define build.name = "kebiaoling_school"

## 主菜单背景（使用 gameover 画面）
define gui.main_menu_background = "gameover.png"

## 窗口标题
python:
    config.window_title = "可堡灵之校"

## 音效和音乐
define config.has_sound = True
define config.has_music = True
define config.has_voice = True

## 转场
define config.enter_transition = dissolve
define config.exit_transition = dissolve
define config.intra_transition = dissolve
define config.after_load_transition = None
define config.end_game_transition = None

## 窗口管理
define config.window = "auto"
define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)

## 默认设置
default preferences.text_cps = 0
default preferences.afm_time = 15

## 存档目录
define config.save_directory = "kebiaoling-1778953410"

## 图标
define config.window_icon = "gui/window_icon.png"

## 构建配置
init python:
    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)
    build.documentation('*.html')
    build.documentation('*.txt')
