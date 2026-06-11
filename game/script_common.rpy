# ============================================================
# 可堡灵之校 v2 - 通用定义
# 变量 · 角色 · 场景 · 立绘 · 函数 · HUD
# ============================================================

# ---- 音频资源 ----
# BGM: suhuan1.mp3（校园日常/探索）
# SE: classbell.mp3（上课铃） footstep_02.mp3（脚步声）
#     footstep_out_01.mp3 kb_01.mp3 knock_door.mp3 bang_table.mp3

# ---- 存档限制（难度相关）----
init python:
    import renpy.store as store
    
    def can_save_load():
        """检查当前难度是否允许存档/读档"""
        if hasattr(store, 'difficulty') and store.difficulty == "nightmare":
            return False
        return True
    
    def get_save_sensitive():
        """用于按钮 sensitive 属性"""
        return can_save_load()
    
    def apply_save_restrictions():
        """根据当前难度应用存档限制"""
        if hasattr(store, 'difficulty') and store.difficulty == "nightmare":
            config.has_autosave = False
            config.has_quicksave = False
            renpy.block_rollback()
        else:
            config.has_autosave = True
            config.has_quicksave = True
    
    # 加载游戏后重新应用限制
    config.after_load_callbacks.append(apply_save_restrictions)

# ============================================================
# 全局变量
# ============================================================
default w = 1
default d = 1
default stamina = 50
default stamina_max = 50
default keli_coins = 10
default current_char = "lv"  # lv=吕文强, zwh=张闻晦, xhh=徐鸿昊, yjc=严笳谌, wjy=吴机岩, ld=劳达
default char_alive = {
    "lv": True,
    "zwh": True,
    "xhh": True,
    "yjc": True,
    "wjy": True,
    "ld": True
}
default difficulty = "normal"  # easy / normal / nightmare
default mask_progress = 0      # 面具吞噬进度 0~100
default has_phone = False
default has_noticed = False

# ---- w1d3 探索变量 ----
default keys_inv = []
default docs_found = []
default wxj_alert = 0         # 吴玄吉警戒度 0~100
default hide_cooldown = 0     # 躲藏冷却

# w1d3 原地点进度
default classroom_search_done = False
default classroom_upstairs_done = False
default canteen_kitchen_done = False
default canteen_cooler_done = False
default admin_floor1_done = False
default admin_floor2_done = False
default wxj_met_admin = False

# w1d3 新增地点进度（来自 enrich 扩充）
default playground_done = False
default broadcast_room_done = False
default security_room_done = False

# w1d3 时间阶段（0=清晨, 1=上午, 2=午后, 3=黄昏）
default w1d3_phase = 0

# 随机事件冷却
default w1d3_rand_event_cd = 0

# ---- 角色定义 ----
define lv = Character("吕文强", who_color="#66BB6A")
define zwh = Character("张闻晦", who_color="#42A5F5")
define xhh = Character("徐鸿昊", who_color="#FFA726")
define yjc = Character("严笳谌", who_color="#AB47BC")
define wjy = Character("吴机岩", who_color="#EF5350")
define ld = Character("劳达", who_color="#8D6E63")
define head = Character("班主任", who_color="#78909C")
define unknown = Character("???", who_color="#AAAAAA")
define mask = Character("面具", who_color="#000000")
define kelibao = Character("可丽堡", who_color="#CC3333")
define blackman = Character("黑衣人", who_color="#37474F")
define wxj = Character("吴玄吉", who_color="#993300")

# ---- 扩充角色（背景同学）----
define classmate_a = Character("同学A", who_color="#99BB99")
define classmate_b = Character("同学B", who_color="#99BB99")
define classmate_c = Character("同学C", who_color="#99BB99")
define roommate_1 = Character("室友甲", who_color="#99BB99")
define roommate_2 = Character("室友乙", who_color="#99BB99")

# ---- 场景定义 ----
image classroom_day = "jiaoshi_1.jpg"
image classroom_after = "jiaoshi_2.jpg"
image classroom_eve = "jiaoshi_3.jpg"
image classroom_night = "jiaoshi_4.jpg"
image dorm_day = Transform("dorm_day.png", size=(1280, 720), fit="cover")
image dorm_dusk = Transform("dorm_dusk.png", size=(1280, 720), fit="cover")
image dorm_night = Transform("dorm_night.png", size=(1280, 720), fit="cover")
image dorm_moon = Transform("dorm_moon.png", size=(1280, 720), fit="cover")
image corridor_day = "corridor_day.webp"
image corridor_dusk = "corridor_dusk.webp"
image corridor_night = "corridor_night.webp"
image gate_day = "gate_day.webp"
image gate_dusk = "gate_dusk.webp"
image gate_night = "gate_night.webp"
image gate_morning = "gate_morning.webp"
image gameover = "gameover.webp"
image building_day = "building_day.webp"
image building_night = "building_night.webp"
image canteen_day = "canteen_day.webp"
image canteen_dusk = "canteen_dusk.webp"
image canteen_light = "canteen_light.webp"

# ---- 新增场景（1:1 图片→拉伸填满16:9）----
image playground = Transform("playground.webp", size=(1280, 720), fit="cover")
image office_hall = Transform("office_hall.webp", size=(1280, 720), fit="cover")
image office_principal = Transform("office_principal.webp", size=(1280, 720), fit="cover")
image school_gate_closeup = Transform("school_gate_closeup.webp", size=(1280, 720), fit="cover")
image broadcast_room = Transform("broadcast_room.webp", size=(1280, 720), fit="cover")
image security_room = Transform("security_room.webp", size=(1280, 720), fit="cover")

# ---- 立绘：吕文强（原林晓立绘）----
image lv normal = "lx/lx_normal.webp"
image lv happy = "lx/lx_happy.webp"
image lv angry = "lx/lx_angry.webp"
image lv fright = "lx/lx_fright.webp"

# ---- 新增立绘 ----
image zwh normal = "zwh_normal.webp"
image zwh happy = "zwh_happy.webp"
image zwh angry = "zwh_angry.webp"
image zwh fright = "zwh_fright.webp"
image zwh sneaky = "zwh_sneaky.webp"
image xhh normal = "xhh_normal.webp"
image xhh happy = "xhh_happy.webp"
image xhh angry = "xhh_angry.webp"
image xhh fright = "xhh_fright.webp"
image yjc normal = "yjc_normal.webp"
image yjc happy = "yjc_happy.webp"
image yjc angry = "yjc_angry.webp"
image yjc fright = "yjc_fright.webp"
image wjy normal = "wjy_normal.webp"
image wjy happy = "wjy_happy.webp"
image wjy angry = "wjy_angry.webp"
image wjy fright = "wjy_fright.webp"
image ld normal = "ld_normal.webp"
image ld happy = "ld_happy.webp"
image ld angry = "ld_angry.webp"
image ld fright = "ld_fright.webp"
image mask_principal = "mask_principal.webp"
image kelibao_normal = "gbl/gbl_normal.webp"
image kelibao_happy = "gbl/gbl_happy.webp"
image kelibao_angry = "gbl/gbl_angry.webp"
image blackman_default = "blackman.webp"
image wxj normal = "blackman.webp"
image wxj angry = "blackman.webp"
image wxj happy = "blackman.webp"
image hallway = "corridor_day.webp"

# ---- 精灵缩放（立绘太大 → 缩小到合适尺寸）----
transform sprite_stand:
    zoom 0.85

transform sprite_left:
    xalign 0.25 yalign 1.0 zoom 0.85

transform sprite_center:
    xalign 0.5 yalign 1.0 zoom 0.85

transform sprite_right:
    xalign 0.75 yalign 1.0 zoom 0.85

# ---- 工具函数 ----
init python:
    def get_dayName(d):
        days = ["星期一", "星期二", "星期三", "星期四", "星期五", "星期六", "星期日"]
        return days[d - 1] if 1 <= d <= 7 else "无效"

    def stamina_use(cost):
        global stamina
        if current_char == "xhh":
            cost = max(1, cost - 2)
        stamina -= cost
        # 精力耗尽 → 在探索主循环中处理

# ---- HUD ----
screen game_hud_v2():
    zorder 100
    frame:
        xalign 1.0
        yalign 0.0
        xmargin 15
        ymargin 15
        background Solid("#00000099")
        xpadding 18
        ypadding 12
        vbox:
            spacing 4
            text "第 [d] 天" color "#87CEEB" size 22 outlines [(2, "#00000088", 0, 0)]
            text "精力: [stamina]/[stamina_max]" color "#66DD66" size 22 outlines [(2, "#00000088", 0, 0)]
            if keli_coins > 0:
                text "可丽币: [keli_coins]" color "#FFD700" size 22 outlines [(2, "#00000088", 0, 0)]
