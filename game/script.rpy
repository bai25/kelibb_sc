# ============================================================
# 可堡灵之校 v2 - 重构版脚本 (w1d1 ~ w1d2)
# ============================================================

# ---- 全局变量 ----
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

# ---- 场景（复用旧资源 + 新增占位）----
image classroom_day = "jiaoshi_1.jpg"
image classroom_after = "jiaoshi_2.jpg"
image classroom_eve = "jiaoshi_3.jpg"
image classroom_night = "jiaoshi_4.jpg"
image dorm_day = "dorm_day.webp"
image dorm_dusk = "dorm_dusk.webp"
image dorm_night = "dorm_night.webp"
image dorm_moon = "dorm_moon.webp"
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

# ---- 新增场景 ----
image playground = "playground.webp"
image office_hall = "office_hall.webp"
image office_principal = "office_principal.webp"
image school_gate_closeup = "school_gate_closeup.webp"
image broadcast_room = "broadcast_room.webp"
image security_room = "security_room.webp"

# ---- 立绘（吕文强使用原林晓立绘）----
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
        if stamina <= 0:
            renpy.jump("game_over_exhausted")

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

# ============================================================
# 游戏开始
# ============================================================
label start_v2:
    scene black
    with dissolve

    "本游戏纯属虚构"
    "如有雷同，纯属巧合"

    menu:
        "选择难度："
        "简单（允许存档读档）":
            $ difficulty = "easy"
        "困难（吞噬人格后有负面效果，允许存档读档）":
            $ difficulty = "normal"
        "噩梦（不能存档读档，吞噬人格后有负面效果）":
            $ difficulty = "nightmare"

    if difficulty == "nightmare":
        "你选择了噩梦难度。"
        "无法存档，无法读档。"
        "每一个选择都关乎生死。"
    elif difficulty == "normal":
        "你选择了困难模式。"
        "被吞噬的人格会带来负面效果。"
        "谨慎选择你的每一步。"
    else:
        "简单模式。尽情体验故事吧。"

    scene black
    with dissolve

    "故事开始……"

    jump w1d1_morning

# ============================================================
# w1d1 · 异常的前兆
# ============================================================
label w1d1_morning:
    $ w = 1
    $ d = 1

    scene dorm_day
    with fade
    show screen game_hud_v2

    "清晨的阳光透过窗帘的缝隙照进宿舍。"
    "吕文强睁开眼，看了一眼天花板。"

    "又是普通的一天。"
    "普通到让人觉得——"
    "好像哪里不太对。"

    scene classroom_day
    with fade
    "教室里，你翻开课本。"

    show lv normal at center
    with dissolve

    "……嗯？"

    "课本的某一页折了个角。"
    "你确定自己从来没有折过书页的习惯。"

    "你拿起水杯。"
    "杯子的位置也不对——你习惯放在右上角，现在它在左边。"
    $ has_noticed = True

    "可能是室友动过吧。"
    "你压下心里的那点异样，开始自习。"

    scene canteen_day
    with fade
    "午饭时间，食堂里人声嘈杂。"

    "你端着餐盘找了个角落坐下。"
    "对面的同学在讨论什么——"

    "同学A："哎听说了吗？这次春游校长要选六个学生代表。""
    "同学B："六个？这么多？以前最多两个。""
    "同学A："不知道，反正跟我们没关系，那是好学生的事。""

    "你夹了一块肉放进嘴里。"
    "六名学生代表……"

    scene classroom_after
    with fade
    "下午一点。"

    head "同学们，安静一下。"
    head "我要宣布一个好消息——"
    head "学校决定在下周组织春游！"

    show lv happy
    "教室里爆发出欢呼声。"
    "你也跟着鼓起掌来。"
    "春游……确实很久没有过了。"

    
    with dissolve

    "但你的脑海中还在回响着午饭时听到的那句话——"
    "六名学生代表。"
    "总觉得……不太对劲。"

    scene dorm_dusk
    with fade
    "傍晚，宿舍。"
    "室友们都在兴奋地讨论春游要去哪里。"
    "你靠在床头，翻着那本被折过角的课本。"

    "也许是你多心了。"
    "也许一切都很正常。"

    show lv normal at center
    "你合上书，闭上眼。"
    "明天……再说吧。"

    scene dorm_night
    with fade
    "夜深了。"
    "宿舍里只剩下均匀的呼吸声。"

    $ renpy.pause(2.0)

    "你翻了个身。"
    "窗外的月光很亮。"
    "有什么东西在窗台上一闪而过。"

    "……错觉吧。"

    scene black
    with fade

    $ d = 2
    $ stamina = min(stamina_max, stamina + 10)

    "—— w1d1 结束 ——"

    jump w1d2_morning

# ============================================================
# w1d2 · 学生代表
# ============================================================
label w1d2_morning:
    scene dorm_day
    with fade
    show screen game_hud_v2

    "第二天。"

    "室友们起得格外早。"
    "有人在哼歌，有人在翻行李箱找衣服。"
    "春游的气氛让整个宿舍都活了过来。"

    "但你心里那根弦始终绷着。"
    "你也起了床，洗漱，去教室。"

    scene classroom_day
    with fade

    "早自习的铃声刚响不久。"

    head "吕文强，跟我出来一下。"

    show lv normal
    "你愣了一下。"
    "班主任的表情看不出喜怒。"

    "你跟着她走出教室。"

    scene corridor_day
    with fade

    head "恭喜你，你被选为本次春游的学生代表之一。"

    show lv fright
    "你张了张嘴。"

    menu:
        "你的反应："
        "「为什么是我？」":
            lv "……为什么是我？"
            head "你的综合表现不错，老师们一致推荐的。"
        "「代表要做什么？」":
            lv "学生代表……具体要做什么？"
            head "一些组织和协调工作。别担心，不复杂。"
        "沉默":
            "你点了点头，没有说话。"
            "班主任似乎对你的平静有些意外。"

    head "其他五位代表已经在等着了。"
    head "你现在去校长办公室集合。"
    head "校长要在大集合之前见你们。"

    show lv normal
    "校长办公室……"
    "你从没去过那个地方。"

    "——【分支选择】——"

    scene corridor_day
    with fade

    "你走在通往行政楼的走廊上。"
    "脚步在空旷的走廊里回响。"

    scene office_hall
    with fade
    "行政楼比教学楼安静得多。"
    "墙上挂着的名人名言在日光灯下显得有些苍白。"

    "校长办公室的门虚掩着。"

    "你推门进去。"

    scene office_principal
    with fade

    "办公室里已经站了五个人。"
    "看到你进来，他们各自投来目光。"

    show zwh normal at left
    zwh "吕文强？你就是第六个？"
    "说话的是一个瘦高的男生——后来你才知道他叫张闻晦。"

    show yjc normal at right
    yjc "人都齐了。校长呢？"
    "严笳谌推了推眼镜，环顾四周。"

    show xhh normal:
        xalign 0.3 yalign 1.0
    xhh "是不是在里间？我去看看？"
    "徐鸿昊已经迈开步子。"

    show wjy normal:
        xalign 0.7 yalign 1.0
    wjy "别乱动。万一校长在开会——"
    "吴机岩靠在墙边，双手插兜。"

    show ld normal:
        xalign 0.5 yalign 1.0
    ld "……"
    "角落里一个高个子男生一言不发。后来你才知道他叫劳达，大家都叫他老大。"

    "五分钟过去了。"
    "十分钟过去了。"

    yjc "校长还没来。"

    zwh "会不会……忘了？"

    "一种不安的气氛在房间里蔓延。"
    "你心里的那根弦，又绷紧了一分。"

    menu:
        "你决定："
        "出去看看情况":
            jump w1d2_look_outside
        "检查校长办公桌":
            jump w1d2_check_desk
        "让大家继续等":
            jump w1d2_keep_waiting

# ============================================================
# w1d2 · 检查办公桌
# ============================================================
label w1d2_check_desk:
    show lv normal
    "你走到校长办公桌前。"
    "桌上摊着一本打开的文件夹。"
    "里面是……一份名单。"
    "六个名字被红笔圈了起来——"
    "包括你的。"
    ""
    "你来不及细看，走廊传来脚步声。"
    "你连忙退回原位。"
    jump w1d2_look_outside

# ============================================================
# w1d2 · 继续等
# ============================================================
label w1d2_keep_waiting:
    show lv normal
    "你又等了五分钟。"
    "校长依然没有出现。"
    ""
    zwh "一直等下去也不是办法……"
    "你决定出去看看。"
    jump w1d2_look_outside

# ============================================================
# w1d2 · 出去看看
# ============================================================
label w1d2_look_outside:
    show lv normal
    "你推开办公室的门，走到走廊上。"

    scene corridor_day
    with fade

    "行政楼依然安静。"
    "你走到窗边——"

    scene playground
    with fade

    "操场上空空荡荡。"

    "没有学生。"
    "没有老师。"
    "一个人都没有。"

    "你愣住了。"

    "集合时间早就过了。"
    "全校上千人——怎么可能一个人都没有？"

    show lv fright
    "你的心跳开始加速。"

    menu:
        "你决定："
        "尝试离开校园":
            jump w1d2_try_leave
        "去教室办公室拿手机":
            jump w1d2_get_phone
        "回办公室告诉大家":
            jump w1d2_back_to_office

# ============================================================
# w1d2 · 尝试离开校园
# ============================================================
label w1d2_try_leave:
    scene corridor_day
    with fade
    "你快步走向校门。"

    scene gate_day
    with fade
    "校门近在咫尺。"
    "你几乎能看到外面的马路——"

    show blackman_default at center
    with vpunch

    blackman "站住。"

    "两个穿黑色西装的男人拦住了你。"
    "他们的脸上没有任何表情。"

    blackman "学生不允许离开校园。"

    show lv angry
    "你盯着他们。"

    menu:
        "强硬离开":
            $ stamina_use(15)
            "你试图冲过去。"
            "黑衣人动作极快——一只手按上你的肩膀。"
            "你挣扎了一下，但力量悬殊太大。"
            "后脑勺传来一阵钝痛。"
            scene black
            with dissolve
            "视野模糊。"
            "你倒了下去。"
            "失去意识前，你听到——"
            mask "第一份……收下了。"
            $ char_alive["lv"] = False
            jump w2_character_select
        "后退":
            show lv normal
            "你后退了一步。"
            "黑衣人没有追上来。"
            "但校门……出不去了。"
            jump w1d2_back_to_office

# ============================================================
# w1d2 · 去教室办公室
# ============================================================
label w1d2_get_phone:
    scene corridor_day
    with fade

    "你转身，快步走向教学楼。"
    "教室办公室的门锁着。"

    "你试着拧了拧把手——锁死的。"

    menu:
        "撞开门？":
            $ stamina_use(10)
            "你用肩膀撞了两下——门开了。"
            show lv normal
            lv "(……这算不算犯罪？)"
            "没有时间犹豫了。"
            "你找到讲台上的手机——"
            "屏幕亮起。"
            "无信号。"
            "一格都没有。"
            "手机在这里只是块砖头。"
        "算了，回去":
            jump w1d2_back_to_office

    scene classroom_day
    with fade

    show lv fright
    "你握着手机站在空荡荡的教室里。"
    "没有信号。"
    "校门出不去。"
    "校长消失了。"

    "你突然意识到一个可怕的事实——"
    "你被困住了。"

    jump w1d2_broadcast

# ============================================================
# w1d2 · 回办公室
# ============================================================
label w1d2_back_to_office:
    scene office_principal
    with fade

    "你推门回到校长办公室。"
    "五个人都看着你。"

    menu:
        "你告诉他们："
        "「操场上一个人都没有」":
            zwh "什么意思？"
            lv "操场上……没人。全校都没人。"
            "房间里陷入沉默。"
            $ has_noticed = True
        "「校门被封了」":
            xhh "封了？什么叫封了？"
            lv "有穿黑衣服的人拦着，不让出去。"
            ld "……果然。"
            "劳达开口了。这是他说的第一句话。"
            $ has_noticed = True

    "就在这时——"

    play sound "classbell.mp3"

    "广播突然响了。"

    scene black
    with fade

    jump w1d2_broadcast

# ============================================================
# w1d2 · 广播
# ============================================================
label w1d2_broadcast:
    scene corridor_day
    with fade

    mask "各位同学，上午好。"

    "广播里的声音……不是校长。"

    mask "原定于下周的春游活动，暂时取消。"
    mask "请各位同学回到教室，正常上课。"
    mask "重复——春游取消，正常上课。"

    "广播切断。"

    scene classroom_day
    with fade

    "不到十分钟。"
    "学生们陆陆续续回到了教室。"
    "一切都恢复了正常——"
    "不。"

    show lv fright
    "你看着周围的同学。"
    "他们安静地坐下。"
    "安静地翻开课本。"
    "安静地开始自习。"

    "没有人说话。"
    "没有人讨论春游取消的事。"
    "没有人问为什么。"

    "他们只是……安静地学习。"

    "太安静了。"

    "你感到一股寒意从脚底升起。"

    scene classroom_day
    with fade

    "老师走进来。开始讲课。"
    "一切如常。"
    "如常得让人毛骨悚然。"

    "你坐在座位上，握着笔。"
    "笔尖悬在纸上，迟迟没有落下。"

    show lv normal
    "你的同桌在认真做笔记。"
    "他的字迹工整。"
    "但你看了一眼他的眼睛——"

    "空的。"

    scene black
    with fade

    $ d = 3
    $ stamina = min(stamina_max, stamina + 10)

    "—— w1d2 结束 ——"

    "w1d3 待续……"

    return

# ============================================================
# w2 · 角色选择（主角阵亡后）
# ============================================================
label w2_character_select:
    scene black
    with fade

    "吕文强……失去了意识。"
    "但他的故事还没有结束。"
    "或者说——"
    "这里每个人的故事，才刚刚开始。"

    $ current_char_choices = []
    $ c_list = [("zwh", "张闻晦"), ("xhh", "徐鸿昊"), ("yjc", "严笳谌"), ("wjy", "吴机岩"), ("ld", "劳达")]

    menu:
        "选择下一位角色："
        "张闻晦（可进入小空间）":
            $ current_char = "zwh"
        "徐鸿昊（行动精力-2）":
            $ current_char = "xhh"
        "严笳谌（能看懂特殊文字）":
            $ current_char = "yjc"
        "吴机岩（可关闭监控/恢复供电）":
            $ current_char = "wjy"
        "劳达（被发现的概率-30%%）":
            $ current_char = "ld"

    "你将成为——[current_char]。"
    "故事从另一个视角继续……"

    jump w2_start

label w2_start:
    scene black
    with dissolve
    "—— w2 待续 ——"
    return

# ============================================================
# Game Over
# ============================================================
label game_over_exhausted:
    scene gameover
    with fade
    "你的精力耗尽了……"
    $ renpy.pause(2.0)
    return

# ============================================================
# 启动入口 - 跳转到v2版
# ============================================================
label start:
    jump start_v2
