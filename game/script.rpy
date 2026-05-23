# ============================================================================
# 可堡灵之校 - 主游戏脚本 (一周目完整版)
# ============================================================================

# ---- 全局变量 ----
default day = 1
default week = 1
default stamina = 100
default keli_coins = 10
default kbf_trust = 0
default lx_trust = 0
default has_note = False
default has_food = False
default found_hideout = False

# ---- 角色 ----
define kbl = Character("可堡灵", who_color="#CC3333")
define lx = Character("林晓", who_color="#3388CC")
define me = DynamicCharacter("player_name")
define unk = Character("???", who_color="#AAAAAA")

# ---- 场景 ----
image classroom_day = "jiaoshi_1.jpg"
image classroom_after = "jiaoshi_2.jpg"
image classroom_eve = "jiaoshi_3.jpg"
image classroom_night = "jiaoshi_4.jpg"
image dorm_day = "dorm_day.png"
image dorm_dusk = "dorm_dusk.png"
image dorm_night = "dorm_night.png"
image dorm_moon = "dorm_moon.png"
image corridor_day = "corridor_day.png"
image corridor_dusk = "corridor_dusk.png"
image corridor_night = "corridor_night.png"
image gate_day = "gate_day.png"
image gate_dusk = "gate_dusk.png"
image gate_night = "gate_night.png"
image gate_morning = "gate_morning.png"
image gameover = "gameover.png"
image building_day = "building_day.png"
image building_night = "building_night.png"
image canteen_day = "canteen_day.png"
image canteen_dusk = "canteen_dusk.png"
image canteen_light = "canteen_light.png"

# ---- 角色立绘 ----
image kbl normal = "gbl/gbl_normal.png"
image kbl angry = "gbl/gbl_angry.png"
image kbl happy = "gbl/gbl_happy.png"
image kbl fright = "gbl/gbl_fright.png"
image kbl he = "gbl/gbl_he.png"

image lx normal = "lx/lx_normal.png"
image lx angry = "lx/lx_angry.png"
image lx happy = "lx/lx_happy.png"
image lx fright = "lx/lx_fright.png"

# ---- 工具函数 ----
init python:
    def get_dayName(d):
        days = ["星期一", "星期二", "星期三", "星期四", "星期五", "星期六", "星期日"]
        return days[d - 1] if 1 <= d <= 7 else "无效"

    def day_end_check():
        global stamina
        stamina = min(100, stamina + 15)
        if stamina <= 0:
            renpy.jump("game_over_exhausted")

# ---- HUD（放大字号）----
screen game_hud():
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
            text "[get_dayName(day)]" color "#87CEEB" size 22 outlines [(2, "#00000088", 0, 0)]
            text "精力: [stamina]" color "#66DD66" size 22 outlines [(2, "#00000088", 0, 0)]
            if keli_coins > 0:
                text "可丽币: [keli_coins]" color "#FFD700" size 22 outlines [(2, "#00000088", 0, 0)]

# ============================================================
# 游戏开始
# ============================================================
label start:
    "本游戏纯属虚构"
    "如有雷同，纯属巧合"

    $ player_name = renpy.input("请输入你的名字（最多12字符）：", length=12).strip() or "master"

    scene black
    with dissolve
    "故事开始……"
    jump day1_morning

# ============================================================
# 第一天 · 平凡的世界 → 时空重叠
# ============================================================
label day1_morning:
    scene classroom_day
    with fade
    show screen game_hud
    play music "suhuan1.mp3" loop fadein 1.0

    "星期一的早晨。"
    "空气里混着粉笔灰的味道。"
    "你坐在教室里，正准备趴一会儿。"

    show lx normal at right
    with moveinright
    lx "[player_name]，可堡灵又在后面闹了。"
    lx "他说没写生物作业，要借我的抄。"

    menu:
        "怎么回应？"
        "别理他":
            $ lx_trust += 1
            lx "唉……你说得对。"
        "我去看看":
            $ kbf_trust += 1
            "你站起身往后排走去。"

    scene classroom_day
    show kbl normal:
        xalign 0.5 yalign 1.0
    kbl "哦？[player_name]？咋了？"

    menu:
        "你说："
        "「老实写作业」":
            $ kbf_trust -= 1
            show kbl angry
            kbl "啧，装啥呢。"
            $ stamina -= 5
        "「没事，你继续」":
            $ kbf_trust += 1
            show kbl happy
            kbl "嘿嘿，还是你懂我。"

    play sound "classbell.mp3"
    hide kbl
    "上课铃响了。"

    $ renpy.pause(2.0)

    play sound "bang_table.mp3"
    "突然一声拍桌响！"
    show classroom_day with hpunch

    unk "可堡灵！！！上课睡觉？！"
    show kbl normal
    kbl "老师我没睡……"
    unk "站起来！"

    hide kbl
    "可堡灵慢慢站起来。"
    "他的动作……不太对劲。"
    "像换了一个人。"
    $ stamina -= 3

    scene canteen_day
    with fade
    "午饭时，林晓坐在你对面。"

    show lx happy at left
    lx "上午生物课那段你看到了吧？"

    menu:
        "挺正常的":
            $ lx_trust += 1
        "确实有点怪":
            $ kbf_trust += 1

    hide lx
    "下午平平无奇。可堡灵逃课了。"

    scene dorm_day
    with fade
    stop music fadeout 2.0
    "放学回宿舍，身体像灌了铅一样沉。"
    "你爬上床，意识模糊……"

    scene black
    with dissolve
    play sound "kb_01.mp3"

    show white:
        alpha 0
        linear 0.5 alpha 0.8
        linear 1.5 alpha 0

    $ renpy.pause(2.5)

    play music "suhuan1.mp3" loop fadein 2.0

    scene dorm_moon
    with dissolve
    "你醒来。凌晨3:44。"
    "手机——无信号。"
    "一切都不一样了。"

    scene corridor_night
    with fade
    play sound "footstep_02.mp3"
    "走廊空无一人，安静得可怕。"

    scene building_night
    with fade
    play sound "kb_01.mp3"
    "广播突然响起——"

    kbl "各位同学，晚上好。"
    kbl "欢迎来到新的学期。"
    kbl "第一条：晚上十点后，禁止离开宿舍。"
    kbl "第二条：禁止靠近学校大门。"
    kbl "第三条：一切以可丽币结算。"
    kbl "祝各位……活得愉快。"

    play sound "kb_01.mp3"
    "广播切断。你背后一阵发凉。"

    scene gate_night
    with fade
    "校门被半透明的雾气封锁，伸手一碰——"
    play sound "bang_table.mp3"
    "刺痛！真的出不去……"

    scene black
    with fade
    stop music fadeout 2.0

    $ day = 2
    $ day_end_check()

    "第一天 · 结束"

    jump day2_dorm

# ============================================================
# 第二天 · 宿舍探索
# ============================================================
label day2_dorm:
    scene dorm_day
    with fade
    show screen game_hud
    play music "suhuan1.mp3" loop

    "第二天清晨。"
    "你从宿舍床上醒来。"
    "昨晚的一切……不是梦。"

    "宿舍门缝下塞着一张纸条。"

    $ renpy.pause(1.0)
    "你捡起来一看——"

    show white:
        alpha 0
        linear 0.3 alpha 0.5
        linear 0.5 alpha 0

    unk "\「宿舍楼三楼储物间是安全的。\」"
    unk "\「别让可堡灵发现你知道太多。\」"
    unk "\——某人"

    $ has_note = True

    "没有署名。字迹很潦草，像是匆忙写的。"
    "三楼储物间……要去看看吗？"

    menu:
        "去三楼储物间":
            $ found_hideout = True
            "你推开储物间的门——里面堆满了旧桌椅和灰尘。"
            "但在角落里，你发现了一个铁盒。"
            $ keli_coins += 5
            "里面装着5枚可丽币和一张旧学生证。"
            $ has_note = True
            "照片上的人你不认识，但名字有些眼熟……"

        "先搜搜宿舍":
            "你在宿舍翻了翻，找到半包压缩饼干。"
            $ has_food = True
            $ stamina += 5
            "虽然不顶饱，但总比没有好。"

    play sound "footstep_out_01.mp3"
    "走廊里传来脚步声。"
    "你屏住呼吸——脚步声渐远。"

    scene corridor_day
    with fade
    "你小心翼翼地走出宿舍。"
    "走廊的墙上贴着一张新的告示："

    show white:
        alpha 0
        linear 0.3 alpha 0.5
        linear 0.5 alpha 0

    kbl "今日食堂开放时间：12:00-13:00"
    kbl "凭可丽币购买食物"
    kbl "——可堡灵学生会"

    "连食堂都被控制了……"

    scene canteen_day
    with fade
    "你来到食堂，发现菜单上的价格高得离谱。"
    "一份米饭就要3可丽币。"
    "你口袋里只有[keli_coins]枚。"

    menu:
        "买一份吗？"
        "买（-3可丽币）" if keli_coins >= 3:
            $ keli_coins -= 3
            $ stamina += 20
            "你买了一份饭。虽然味道一般，但总算填了肚子。"
        "不买":
            $ stamina -= 10
            "你忍着饿离开了食堂。"

    scene corridor_day
    with fade
    "下午你在教学楼里转了一圈。"
    "大部分教室都锁着门。"
    "偶尔能看到一两个模糊的人影一闪而过——"
    "但他们看到你就跑开了。"

    scene dorm_dusk
    with fade
    "傍晚回到宿舍，你瘫在床上。"
    "这个学校的每一天……都在消耗你的精力。"

    $ day = 3
    $ day_end_check()

    "第二天 · 结束"
    jump day3_search

# ============================================================
# 第三天 · 校园探索
# ============================================================
label day3_search:
    scene corridor_day
    with fade
    show screen game_hud

    "第三天。"
    "你决定更仔细地探索校园。"

    if found_hideout:
        "你再次去了三楼储物间。"
        "里面似乎被人翻过——但铁盒还在原位。"
        "你打开铁盒，发现里面多了一张纸条："
        show white:
            alpha 0
            linear 0.3 alpha 0.5
            linear 0.5 alpha 0
        unk "\「第五天晚上，钟楼见。\」"
        "钟楼……学校的旧钟楼早就废弃了。"
        $ has_note = True
    else:
        "你找到了三楼储物间。"
        "里面有个铁盒，装着一些旧物和一张纸条。"
        unk "\「第五天晚上，钟楼见。\」"
        $ found_hideout = True
        $ has_note = True

    scene canteen_light
    with fade
    "午餐时间，林晓居然出现在食堂。"

    show lx normal at right
    with moveinright
    lx "[player_name]！你还活着！"
    lx "我以为……大家都……"

    menu:
        "你还好吗？":
            $ lx_trust += 1
            lx "我躲在后山器材室两天了。"
        "你知道怎么回事吗？":
            lx "我知道的不比你多。"
            lx "但我觉得……可堡灵已经不是人了。"

    lx "我得走了。他们有巡逻队。"
    lx "保重，[player_name]。"
    hide lx
    with moveoutright

    "林晓匆匆离开。"

    scene corridor_dusk
    with fade
    "你走在回宿舍的路上。"
    "突然——"

    play sound "footstep_02.mp3"
    "急促的脚步声从拐角传来！"
    show kbl he at center
    with vpunch

    kbl "哟，[player_name]。"
    kbl "这两天过得怎么样？"

    "可堡灵的眼睛在昏暗的走廊里发着微弱的红光。"

    menu:
        "「挺好的」":
            $ kbf_trust += 1
            kbl "是吗？那就好。"
            kbl "我还怕你不习惯呢。"
        "「你到底是什么东西」":
            $ kbf_trust -= 2
            show kbl angry
            kbl "啧，说话注意点。"
            kbl "这里我说了算。"
            $ stamina -= 10

    hide kbl
    "可堡灵转身离开了。"
    "你松了口气。"

    scene dorm_night
    with fade
    $ day = 4
    $ day_end_check()
    "第三天 · 结束"
    jump day4_night

# ============================================================
# 第四天 · 夜晚异响
# ============================================================
label day4_night:
    scene dorm_dusk
    with fade
    show screen game_hud

    "第四天。"
    "你发现校园里的人越来越少了。"
    "早上还能看到几个零散的身影，到下午就几乎没人了。"

    scene corridor_dusk
    with fade
    "你在走廊里遇到一个低年级学生。"
    "他低着头快步走着。"

    menu:
        "叫住他":
            "他惊恐地看了你一眼，转身就跑。"
            "你只来得及看到他胳膊上的淤青。"
        "算了":
            "你让他过去了。"

    scene dorm_night
    with fade
    play sound "knock_door.mp3"
    "深夜，你被敲门声惊醒。"

    $ renpy.pause(2.0)
    "又是三声。"

    play sound "knock_door.mp3"
    $ renpy.pause(2.0)

    menu:
        "开门":
            "门外的走廊空无一人。"
            "但地上放着一个纸包。"
            "里面是一瓶水和一张纸条："
            unk "\「坚持下去。\」"
            $ stamina += 10
        "不开门":
            "你屏住呼吸，一动不动。"
            "几分钟后，脚步声远去了。"

    scene dorm_moon
    with dissolve
    "你再也睡不着了。"
    "这个学校……到底发生了什么？"

    $ day = 5
    $ day_end_check()
    "第四天 · 结束"
    jump day5_clocktower

# ============================================================
# 第五天 · 钟楼之约
# ============================================================
label day5_clocktower:
    scene building_day
    with fade
    show screen game_hud

    "第五天。"
    "你记得纸条上的约定——钟楼。"

    scene corridor_day
    with fade
    "旧钟楼在教学楼的最西侧。"
    "铁门虚掩着，像是被人打开不久。"

    scene corridor_dusk
    with fade
    "你沿着旋转楼梯往上走。"
    "每走一步，木阶梯就发出刺耳的吱呀声。"

    scene canteen_dusk
    with fade
    "钟楼的顶层出乎意料地宽敞。"
    "地上铺着一条旧毯子，旁边堆着几本书和一个水壶。"

    "有人住在这里。"

    show white:
        alpha 0
        linear 0.3 alpha 0.5
        linear 0.5 alpha 0

    lx "[player_name]？是你吗？！"
    show lx happy at center
    with dissolve

    "林晓从角落里探出头来。"

    lx "那张纸条是我放的！"
    lx "这里是我发现的秘密据点。"

    menu:
        "你怎么找到这里的？":
            lx "我之前是学生会成员，有所有楼的钥匙。"
            lx "但现在都没用了。可堡灵控制了所有通道。"
        "你在这里安全吗？":
            lx "暂时安全。这里有水和干粮。"
            lx "但撑不了几天了。"

    lx "我觉得……我们要逃出去。"
    lx "校门口那层雾，一定有破解的办法。"

    "林晓翻开一本旧笔记。"
    show lx normal
    lx "我以前在图书馆看过一本关于这个学校历史的书。"
    lx "这个学校……一百年前就出过类似的事。"
    lx "那本书里提到，要解除封锁，需要找到「堡灵之印」。"

    "\「堡灵之印」？"
    lx "我不知道那是什么。但肯定跟可堡灵有关。"

    scene corridor_night
    with fade
    "离开钟楼时天色已暗。"
    "你心里有了目标——找到「堡灵之印」。"

    $ day = 6
    $ day_end_check()
    "第五天 · 结束"
    jump day6_desperate

# ============================================================
# 第六天 · 绝境
# ============================================================
label day6_desperate:
    scene corridor_day
    with fade
    show screen game_hud

    "第六天。"
    "你开始在校园里寻找「堡灵之印」的线索。"
    "图书馆锁着门。行政楼也锁着。"
    "可堡灵的巡逻队明显增多了。"

    scene canteen_day
    with fade
    "你在食堂买饭时，发现告示栏上贴着一张新通知："

    show white:
        alpha 0
        linear 0.3 alpha 0.5
        linear 0.5 alpha 0

    kbl "全校集会——第七天下午五点 · 操场"
    kbl "无故缺席者——后果自负。"

    "不好的预感。"

    scene corridor_dusk
    with fade
    play sound "footstep_02.mp3"

    "回宿舍的路上，你被三个穿黑衣服的学生拦住了。"

    unk "你就是[player_name]？"
    unk "堡灵哥要见你。"

    menu:
        "跟他们走":
            $ stamina -= 10
            "他们把你带到了旧教学楼的一间教室里。"
            scene classroom_night
            with fade
            show kbl angry at center
            kbl "[player_name]，你最近很不老实啊。"
            kbl "到处打听不该打听的事。"
            "他走到你面前，几乎贴着你的脸。"
            kbl "明天的集会，你得来。"
            kbl "不然……你知道后果。"
            hide kbl
            "他们放你走了。"
            "但你心里清楚——明天不会是什么好事。"

        "逃跑":
            "你转身就跑！"
            $ stamina -= 15
            "你拼了命地跑回宿舍，锁上门。"
            "外面传来咒骂声和踢门声。"
            "但他们最终离开了。"
            "你暂时安全了……但可堡灵不会放过你的。"

    scene dorm_night
    with fade

    $ day = 7
    $ day_end_check()
    "第六天 · 结束"
    jump day7_finale

# ============================================================
# 第七天 · 一周目终章
# ============================================================
label day7_finale:
    scene dorm_day
    with fade
    show screen game_hud

    "第七天。"
    "最后一天了。"
    "集会下午五点开始。"

    scene corridor_day
    with fade

    "你还有几个小时做准备。"

    if found_hideout:
        "你去钟楼找了林晓。"
        show lx normal at right
        lx "你来了。"
        lx "我查到了「堡灵之印」是什么了。"
        lx "那是可堡灵的力量核心。"
        lx "只要毁了它，封锁就会解除。"
        lx "那东西……就在他身上。"
        "所以你需要在集会上接近他。"

    scene gate_day
    with fade
    "下午五点，操场。"
    "全校不到三十个人稀稀拉拉地站着。"
    "讲台上——可堡灵穿着笔挺的黑色制服。"

    show kbl he at center
    kbl "各位，这一周过得还愉快吧？"
    kbl "从今天起，这里将实行新的制度。"
    kbl "愿意效忠我的，可以留下。"
    kbl "不愿意的——"
    "他笑了笑。"
    kbl "校门在那，你们可以走。"

    "人群骚动起来。几个人试探性地走向校门——"
    "他们穿过了雾气！"

    "真的可以走了？！"

    "但可堡灵接下来的话让你僵住了。"
    kbl "不过嘛……离开的人，会忘记在这里的一切。"
    kbl "包括你们在外面的人生。"
    kbl "出去就是一个全新的人。"
    kbl "什么都不记得。"

    "人群沉默了。"

    menu:
        "你的选择："
        "走向校门（离开，失去一切记忆）":
            jump ending_leave
        "冲向可堡灵（夺走堡灵之印）":
            jump ending_fight
        "先观察情况":
            jump ending_watch

# ============================================================
# 结局 · 离开
# ============================================================
label ending_leave:
    scene gate_morning
    with fade
    "你走向校门。"
    "雾气在你面前分开。"

    scene black
    with fade

    "你走出了学校。"
    "身后的铁门缓缓关上。"

    $ renpy.pause(2.0)

    unk "……"
    unk "你站在一条陌生的街道上。"
    unk "你不记得自己从哪里来。"
    unk "也不记得自己是谁。"

    $ renpy.pause(3.0)

    "——一周目 · 结局：遗忘——"
    return

# ============================================================
# 结局 · 抗争
# ============================================================
label ending_fight:
    play sound "bang_table.mp3"
    scene gate_day with hpunch

    "你冲向讲台！"
    "可堡灵措手不及——"

    show kbl angry:
        xalign 0.5 yalign 1.0
    kbl "你疯了？！"
    "你抓住了他胸口的吊坠——那就是「堡灵之印」。"
    "用力一扯——"

    show white:
        alpha 0
        linear 0.2 alpha 1.0
        linear 1.0 alpha 0

    play sound "kb_01.mp3"

    "一道刺目的白光炸开。"

    scene black
    with dissolve

    "当你再次睁开眼睛时——"
    "你躺在宿舍床上。"
    "手机有信号了。"
    "阳光照进窗户。"

    "学校广播里传来日常的通知。"
    "一切都恢复了正常……"

    $ renpy.pause(2.0)

    "但你知道。"
    "有什么东西不一样了。"

    $ renpy.pause(2.0)

    "——一周目 · 结局：苏醒——"
    return

# ============================================================
# 结局 · 观察
# ============================================================
label ending_watch:
    "你站在人群中，一动不动。"
    "有人离开了，有人留下了。"
    "可堡灵的目光扫过你们。"
    kbl "很好。留下的，你们做出了正确的选择。"
    kbl "明天开始，你们会明白的。"

    scene black
    with fade

    "你留在了学校。"
    "不是因为害怕。"
    "而是因为你还没有放弃。"

    $ renpy.pause(3.0)

    "——一周目 · 结局：潜伏——"
    "\（二周目待续\）"
    return

# ============================================================
# Game Over
# ============================================================
label game_over_exhausted:
    scene gameover
    with fade
    play music "suhuan1.mp3"
    "你的精力已经耗尽……"
    $ renpy.pause(2.0)
    "—— GAME OVER ——"
    return
