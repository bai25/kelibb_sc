# ============================================================
# 可堡灵之校 v2 - w1d3 · 空无一人的校园（探索生存）
# 包含扩充：操场·广播室·保安室·随机事件·时间系统
# ============================================================

label w1d3_empty_school:

    play music "suhuan1.mp3" fadein 2.0 loop

    scene dorm_day
    with fade
    show screen game_hud_v2

    "第三天。"

    $ d = 3
    $ stamina = min(stamina_max, stamina + 10)
    $ keys_inv = []
    $ docs_found = []
    $ wxj_alert = 0
    $ w1d3_phase = 0
    $ w1d3_rand_event_cd = 0
    # 重置地点进度
    $ classroom_search_done = False
    $ classroom_upstairs_done = False
    $ canteen_kitchen_done = False
    $ canteen_cooler_done = False
    $ admin_floor1_done = False
    $ admin_floor2_done = False
    $ wxj_met_admin = False
    $ playground_done = False
    $ broadcast_room_done = False
    $ security_room_done = False

    # ---- 清晨起床（丰富版）----
    scene dorm_day
    with fade

    "第三天的阳光……有些不一样。"
    "不刺眼。偏白。"
    "像隔了一层薄薄的雾。"

    show lv normal at center
    with dissolve

    lv "……嗯。"

    "吕文强睁开眼。"
    "眨了眨干涩的眼睛。"

    "宿舍里安静得过分。"
    "不是那种「室友还在睡」的安静——"
    "而是连呼吸声、翻身声、梦呓声都消失了的那种安静。"

    "他坐起来。"
    "上铺的被子叠得整整齐齐——像是没人睡过。"
    "对面的床铺空着。床单上没有一丝褶皱。"

    lv "……喂？"

    "没有人回答。"

    "他下床。赤脚踩在地板上。"
    "地板冰凉——比平时凉得多。"

    "他走到窗边。"
    "拉开窗帘——"

    scene playground
    with dissolve

    "操场上什么都没有。"
    "草坪在惨白的天光下泛着一种病恹恹的绿。"
    "篮球架孤零零地立着。篮板上的油漆剥落了一大块。"

    "风从窗缝里钻进来。"
    "带着一股奇怪的焦味——像是什么东西在远处被烧过。"

    show lv fright
    "吕文强打了个寒颤。"

    lv "……这不对。"

    "他套上衣服。快步走出宿舍。"

    # ---- 走出宿舍楼（校园整体氛围）----
    scene playground
    with fade

    "宿舍楼的大门虚掩着。"
    "吕文强推开门——"

    "外面的空气比室内冷得多。"
    "而且干燥得不像春天。像是进入了深秋。"

    "他站在宿舍楼门口。"
    "目光扫过整个校园——"

    "教学楼。灰白色的瓷砖墙面。窗户反射着灰蒙蒙的天空。"
    "食堂。卷帘门拉下一半。门口的地面上躺着一个翻倒的垃圾桶——垃圾散了一地，"
    "但已经干了，像是一天前就倒在那里的。"
    "行政楼。窗户拉着窗帘。看不到里面。"

    "校门。铁栅栏紧闭。"
    "门卫室空无一人。窗户上的玻璃裂了一道缝。"

    "整个世界像被按了暂停键。"

    lv "有人吗——？"

    "他的声音在空旷的校园里回荡。"
    "没有人回答。"
    "连回声都显得孤单。"

    "风穿过他的衣领。"
    "远处有什么东西发出轻微的金属碰撞声——"
    "一声。两声。"
    "然后停了。"

    "你需要弄清楚发生了什么。"
    "但首先——你需要装备自己。"

    jump w1d3_explore

# ============================================================
# w1d3 · 探索主循环（丰富版）
# 新增：操场·广播室·保安室·随机事件·时间推进
# ============================================================
label w1d3_explore:

    $ hide_cooldown = max(0, hide_cooldown - 1)
    $ w1d3_rand_event_cd = max(0, w1d3_rand_event_cd - 1)

    # 精力耗尽 → 强制休息
    if stamina <= 0:
        "你的双腿像灌了铅一样沉重……视线开始模糊……"
        jump w1d3_forced_rest

    # 吴玄吉警戒度满 → 追捕
    if wxj_alert >= 100:
        "你听到远处传来急促的脚步声——有人在快速靠近。"
        jump w1d3_wxj_chase

    scene black
    with dissolve

    # 根据时间阶段给出不同的氛围描述
    if w1d3_phase == 0:
        "清晨的校园笼罩在一层薄雾中。你的呼吸在空气中形成白雾。"
        "露水打湿了你的鞋面。四周安静得像一座坟墓。"
    elif w1d3_phase == 1:
        "太阳升高了一些，但阳光没有带来任何暖意。"
        "光线穿过雾气，在地面上投下模糊的影子。"
    elif w1d3_phase == 2:
        "午后。阳光最盛的时候——但在空旷的校园里，这一切只让影子显得更黑更长。"
        "你注意到奇怪的一点——地面上有影子，但没有声音。"
        "好像整个世界都是一幅画。"
    else:
        "天色开始暗下来了。建筑物在黄昏的光线下变成了剪影。"
        "如果你不快点决定，夜晚就要来了。"

    # 随机事件（冷却间隔时触发）
    if w1d3_rand_event_cd <= 0:
        $ w1d3_rand_event_cd = 3
        call w1d3_random_event from _call_w1d3_random_event
        if _return == "leave":
            jump w1d3_time_advance

    # ---- 地点状态汇总 ----
    $ classroom_all_done = classroom_search_done and classroom_upstairs_done
    $ canteen_all_done = canteen_kitchen_done and canteen_cooler_done
    $ admin_locked = "admin_key" not in keys_inv
    $ admin_all_done = admin_floor1_done and admin_floor2_done
    $ admin_accessible_not_done = not admin_locked and not admin_all_done
    $ new_locations_done = playground_done and broadcast_room_done and security_room_done
    $ all_locations_done = classroom_all_done and canteen_all_done and (admin_all_done or admin_locked) and new_locations_done

    if all_locations_done:
        "你把能去的地方都走了一遍。再待下去也不会有什么新发现了。"
        jump w1d3_dorm_rest

    menu:
        "去哪儿？"
        "教学楼" if not classroom_all_done:
            jump w1d3_classroom
        "行政楼" if admin_accessible_not_done:
            jump w1d3_admin
        "行政楼（锁着）" if admin_locked:
            "行政楼大门紧锁。你需要找到钥匙。"
            jump w1d3_explore
        "食堂" if not canteen_all_done:
            jump w1d3_canteen
        "操场" if not playground_done:
            jump w1d3_playground
        "广播室" if not broadcast_room_done:
            jump w1d3_broadcast_room
        "保安室" if not security_room_done:
            jump w1d3_security_room
        "查看背包":
            jump w1d3_inventory
        "回宿舍休息（推进到下一天）":
            jump w1d3_dorm_rest

# ============================================================
# w1d3 · 随机探索事件
# ============================================================
label w1d3_random_event:
    $ rand_ev = renpy.random.randint(1, 6)

    if rand_ev == 1:
        "一阵风吹过。你听到远处传来了什么声音——"
        "像是广播的嗡鸣声。很短。一瞬就消失了。"
        "你转头看向广播室的方向。什么都没有。"
        return False

    elif rand_ev == 2:
        "你注意到地面上有一道拖曳的痕迹。"
        "像是有什么东西被拖着走过——从教学楼的方向，一直延伸到操场。"
        "痕迹已经干了，但看得出是新的——不超过一天。"
        $ has_noticed = True
        return False

    elif rand_ev == 3:
        "一只乌鸦从头顶飞过。"
        "它落在不远处的旗杆上，歪着头看着你。"
        "你与它对视了五秒。"
        "它飞走了。"
        return False

    elif rand_ev == 4:
        "你感觉口袋里的手机震了一下。"
        "你伸手去摸——但口袋是空的。你根本没带手机。"
        "幻震。很有名的一种幽灵震动综合症。"
        "但在此时此刻，它让你出了一身冷汗。"
        return False

    elif rand_ev == 5:
        "你经过一扇关着的门时——"
        "门突然发出「咔」的一声。"
        "像是门锁弹开了。"
        "你停下来。"
        "门没有再动。"
        "周围依然安静。"
        "你推了推那扇门——锁着。"
        "那你刚才听到的是什么？"
        return False

    elif rand_ev == 6:
        "你突然感到脊背一阵发凉——"
        "一种被注视的感觉。"
        "你猛地回头。"
        "没有人。"
        "但你确信——在那几秒钟里，有什么东西在看着你。"
        $ wxj_alert += 5
        return False

    return False

# ============================================================
# w1d3 · 背包/查看道具
# ============================================================
label w1d3_inventory:
    $ renpy.block_rollback()
    call screen inventory_screen
    jump w1d3_explore

# ============================================================
# w1d3 · 可阅读文件（由背包 UI 按钮跳转）
# ============================================================
label inventory_read_doc_newspaper:
    scene black
    with dissolve
    "一份泛黄的报纸剪报。"
    "日期是十五年前。"
    "标题：《城东中学集体失踪案告破——警方不予立案》"
    "「……调查显示，六名学生在春游前夕同时失踪。"
    "校方称学生已请假返乡，但家长表示从未收到通知……」"
    "下面还有一行小字手写批注："
    "「同样的地方，同样的事。历史在重复。—老陈」"
    jump w1d3_inventory

label inventory_read_doc_contract:
    scene black
    with dissolve
    "一份校长手写的合同。纸张有被烧过的痕迹。"
    "「本人自愿献出六名学生的生命力，以换取[[涂黑]]的力量。"
    "作为交换，学校将获得十年繁荣。」"
    "落款处是校长的签名和指印。"
    "旁边还有另一个签名——字迹潦草，但勉强能认出是「吴」字。"
    jump w1d3_inventory

label inventory_read_doc_student_list:
    scene black
    with dissolve
    "一张打印的学生名单。"
    "上面列着六个名字，旁边标注了编号。"
    "你的名字——吕文强——排在第三位。"
    "第一位：徐鸿昊"
    "第二位：严笳谌"
    "第三位：吕文强"
    "第四位：张闻晦"
    "第五位：吴机岩"
    "第六位：劳达"
    "名单底部有红色的手写字："
    "「顺序已定，不可更改。」"
    jump w1d3_inventory

# ============================================================
# w1d3 · 教学楼（丰富版）
# ============================================================
label w1d3_classroom:
    scene classroom_day
    with fade

    "教学楼的走廊比你记忆中更暗。"
    "日光灯发出微弱的嗡鸣——但有一半的灯管已经灭了。"
    "走廊的尽头笼罩在阴影中。"

    "你每走一步，脚步声就在空荡荡的走廊里回荡。"
    "你尽量放轻脚步——但在这片寂静中，任何声音都显得格外清晰。"

    $ stamina_use(5)

    menu classroom_loop:
        "搜索教室" if not classroom_search_done:
            call w1d3_classroom_search from _call_w1d3_cr_search
            jump classroom_loop
        "上二楼看看" if not classroom_upstairs_done:
            call w1d3_classroom_upstairs from _call_w1d3_cr_upstairs
            jump classroom_loop
        "检查走廊尽头公告栏（新）":
            call w1d3_classroom_bulletin from _call_w1d3_cr_bulletin
            jump classroom_loop
        "离开教学楼":
            "你走出了教学楼。"
            jump w1d3_explore

# --- 教室搜索（扩充版）---
label w1d3_classroom_search:
    $ stamina_use(5)

    "你走进自己的教室。"
    "桌椅排列整齐。黑板上还留着一行板书——"
    "是班主任的字迹。"

    "「距高考还有 XXX 天。」"
    "但那个数字被擦掉了。只剩下白色的印记。"

    "课桌上散落着课本。有人在水杯旁边留了半包饼干。"
    "窗帘在半开的窗户旁轻轻晃动。"

    "这里的一切都像是在说——「主人只是暂时离开，马上就会回来。」"
    "但你知道不是。"
    "已经一天了。没有人回来过。"

    $ found_something = False

    if "locker_key" not in keys_inv:
        "你在讲台的抽屉里发现了一把钥匙。上面贴着一张小标签：「储物柜 03」。"
        $ keys_inv.append("locker_key")
        $ found_something = True

    if "doc_newspaper" not in docs_found:
        "你在一个课桌的夹层里找到了一份旧报纸剪报。边缘泛黄，纸质脆硬。"
        "你小心翼翼地把它展开——"
        $ docs_found.append("doc_newspaper")
        $ found_something = True

    # 新增：半张照片线索
    if "photo_half" not in docs_found:
        "你还在教室后排的地板上捡到了半张照片。"
        "照片上有六个人——但半边被撕掉了，只剩下三个人的半张脸。"
        "背景是学校的大门。看起来是很多年前的毕业照。"
        $ docs_found.append("photo_half")
        "（「半张毕业照」加入你的文档）"
        $ found_something = True

    if not found_something:
        "教室里已经没有更多线索了。"
    else:
        "你搜了一遍教室，找到了几样东西。你把它收好。"
        "但你总觉得……有什么人在看着你翻找。"

    $ classroom_search_done = True
    $ wxj_alert += 10
    return

# --- 二楼（扩充版）---
label w1d3_classroom_upstairs:
    $ stamina_use(5)
    scene classroom_after
    with fade

    "你走上二楼。"

    "这里的采光比一楼好一些，但空气更闷。"
    "窗户都关着。走廊里弥漫着一股奇怪的味道——"
    "像是粉笔灰和消毒水的混合，又带了一点点金属的腥味。"

    "走廊两侧的教室门全部关着。"
    "你试着推了推第一间——锁着。"
    "第二间——也锁着。"
    "第三间——开了。"

    "这是一间空着的教室。桌椅被推到墙边，地面上有杂乱的脚印。"

    if "doc_student_list" not in docs_found:
        "你在教师办公室的碎纸机旁发现了一张残缺的名单。"
        "纸张被撕过——但重要的部分还在。"
        $ docs_found.append("doc_student_list")
    else:
        "二楼没有什么新的发现了。"

    "走廊尽头的门虚掩着。"
    "你走过去，推开门——"

    scene corridor_day
    with fade

    "门后是通往天台的楼梯。"
    "但楼梯口被一把锁链锁住了。"
    "铁链很新。像是不久前才挂上去的。"

    "锁链上挂着一张小卡片——"
    "上面印着一个红色的面具图案。"

    show lv fright
    with dissolve

    "你不记得在哪里见过——但那个红色的面具，让你心里咯噔了一下。"

    "你伸手碰了碰卡片——"
    "就在这时，你听到楼下传来什么声音。"

    "脚步声。"
    "有人在教学楼里。"

    $ wxj_alert += 10
    lv "(……得快点离开这里。)"

    $ classroom_upstairs_done = True
    return

# --- 新增：公告栏 ---
label w1d3_classroom_bulletin:
    scene corridor_day
    with fade

    "走廊的公告栏上贴满了通知。"
    "大部分是常规的——食堂开放时间调整、图书馆周末闭馆公告。"
    "但有一张最新的通知引起了你的注意。"

    "通知日期是前天——也就是第二天。"
    "标题：《关于调整校园出入管理的通知》"

    "「经学校研究决定，即日起关闭校园东门和北门，"
    "全体师生统一经由南门出入。学生在上课期间不得离开校园范围。"
    "若有特殊情况，须持校长签字的请假条方可离校。」"

    "通知的落款不是校务处——"
    "而是一个你从未见过的名字。"
    "「校务管理委员会」"

    show lv normal
    with dissolve

    lv "(校务管理委员会……学校什么时候有这个部门了？)"

    "你拿出手机想拍照——"
    "但手机没电了。"

    "你注意到通知的右下角有一个小小的红色符号——"
    "和你在天楼梯口看到的面具图案一模一样。"

    $ has_noticed = True

    return

# ============================================================
# w1d3 · 食堂（丰富版）
# ============================================================
label w1d3_canteen:
    scene canteen_day
    with fade

    "食堂的门虚掩着。你推门进去——"
    "一股发酸的味道扑面而来。"

    "昨天剩下的饭菜还摆在窗口后面的保温台上。"
    "汤面上浮着一层油脂，已经凝固了。"
    "苍蝇嗡嗡地绕着盘旋——至少说明在这个空荡荡的学校里，"
    "还有别的活物存在。"

    "你穿过用餐区。"
    "椅子歪歪扭扭地放在桌旁——像人们离开时走得并不匆忙。"
    "餐盘回收处的推车上有几只没收拾的碗。筷子散落一地。"

    "后厨的灯还亮着。"
    "透过窗口，你能看到灶台上的锅里还煮着什么东西——已经烧干了。"
    "锅底焦黑一片。"

    $ stamina_use(3)

    menu canteen_loop:
        "搜索后厨" if not canteen_kitchen_done:
            call w1d3_canteen_kitchen from _call_wn_canteen_kitchen
            jump canteen_loop
        "检查冷藏室" if not canteen_cooler_done:
            call w1d3_canteen_cooler from _call_wn_canteen_cooler
            jump canteen_loop
        "在用餐区仔细查看（新）":
            call w1d3_canteen_dining from _call_wn_canteen_dining
            jump canteen_loop
        "离开食堂":
            "你走出了食堂。"
            jump w1d3_explore

# --- 后厨（扩充版）---
label w1d3_canteen_kitchen:
    "你推开后厨的门。"
    "里面的温度比外面高了几度——灶台还没完全冷却。"
    "锅里的水已经蒸发干净，留下一层焦黑的残渣。"

    "储物柜的门半开着。"
    "里面有一些干粮——压缩饼干、方便面、几瓶矿泉水。"
    "大多是食堂员工的备餐。现在没人管了。"

    "你装了一些在身上。"

    $ stamina = min(stamina_max, stamina + 15)

    "虽然只是干粮，但食物带来的充实感让你的身体恢复了一些。"

    "你正准备离开——"
    "余光扫到灶台底下有什么东西。"
    "一张对折的纸条。被油渍浸透了一半。"

    "你展开它。上面歪歪扭扭地写着——"

    "「别吃食堂的肉。」"

    show lv fright
    "你愣住了。"
    "纸条上没有署名。纸张已经发皱——像是在口袋里揣了很久。"

    "你把纸条收好。心里像是压了一块石头。"

    $ canteen_kitchen_done = True
    $ wxj_alert += 5
    return

# --- 冷藏室（扩充版）---
label w1d3_canteen_cooler:
    scene black
    with dissolve

    "你打开冷藏室的门。"
    "一股冰凉的、带腥味的空气扑面而来。"

    "冷藏室里的灯坏了一盏，只剩下另一盏昏黄的灯泡在头顶晃动。"
    "货架上摆着成箱的蔬菜和冻肉。"
    "墙角有一台冰柜——正在嗡嗡地运转。"

    "你注意到墙角有一个被锁上的铁柜。"

    if "locker_key" in keys_inv:
        "你用储物柜钥匙打开了它。"
        "铁柜里放着一份文件——"
        if "doc_contract" not in docs_found:
            "是一份烧了一半的合同。纸张边缘焦黑。"
            "你小心翼翼地把它拿出来。"
            $ docs_found.append("doc_contract")
        else:
            "里面没有别的东西了。"
        $ wxj_alert += 10
    else:
        "储物柜锁着。你需要钥匙才能打开。"
        "但透过柜门的缝隙，你隐约能看到里面有一份文件类的东西。"

    "你正准备离开——"
    "冰柜突然发出一声异响。"
    "像是有什么东西在里面动了一下。"

    "你后退了一步。"
    "冰柜的盖子关着。"
    "你盯着它看了十秒。"
    "没有第二声。"
    "但你心里的那根弦，又绷紧了一分。"

    $ canteen_cooler_done = True
    return

# --- 新增：用餐区检查 ---
label w1d3_canteen_dining:
    scene canteen_day
    with fade

    "用餐区比后厨更让人不安。"
    "不是因为它混乱——恰恰相反，它太整齐了。"
    "像是有人刻意收拾过。"

    "你在餐桌之间走动。"
    "每张桌子上都有餐盘，每个餐盘里都有吃剩的食物。"
    "但有一个细节让你停下了脚步——"

    "所有餐盘里的筷子，都放在同一个方向。"
    "统一指向东边。"

    show lv normal
    with dissolve

    $ has_noticed = True

    return

# ============================================================
# w1d3 · 操场（新地点）
# ============================================================
label w1d3_playground:
    scene playground
    with fade

    "你走向操场。"

    "塑胶跑道的红色在阴沉的天光下显得暗沉。"
    "草坪发黄——不是秋天的黄，而是一种病态的枯黄。"
    "像是地底下缺少了什么养分。"

    "风吹过的时候，旗杆上的绳索发出单调的敲击声——"
    "叮、叮、叮。"

    "偌大的操场上只有你一个人。"

    $ stamina_use(8)

    menu playground_loop:
        "检查旗杆底座":
            call w1d3_playground_flagpole from _call_pl_flagpole
            jump playground_loop
        "查看看台下方":
            call w1d3_playground_stands from _call_pl_stands
            jump playground_loop
        "绕着跑道走一圈":
            call w1d3_playground_lap from _call_pl_lap
            jump playground_loop
        "离开操场":
            "你离开了操场。"
            $ playground_done = True
            jump w1d3_explore

# --- 旗杆底座 ---
label w1d3_playground_flagpole:
    $ stamina_use(3)

    "你走到旗杆下。"
    "旗杆的基座是一个水泥台。上面刻着学校的建校年份和一些模糊的校训文字。"
    "水泥台表面布满了裂纹——像是什么重物曾经砸在上面。"

    "你蹲下来仔细查看。"
    "在基座的侧面，你发现了一行刻字——"
    "字迹很小，像是用钥匙尖刻上去的。"

    "「救我。」"
    "下面还有一个日期——"
    "十五年前的今天。"

    show lv fright
    with dissolve

    lv "……十五年前？"

    "你站起身。"
    "回头看了看空荡荡的教学楼。"
    "十五年前……"
    "这个学校十五年前发生过什么？"

    $ has_noticed = True

    return

# --- 看台下方 ---
label w1d3_playground_stands:
    $ stamina_use(5)

    scene black
    with dissolve

    "你走向操场旁边的看台。"
    "看台下方是空的——一个半封闭的储物空间，堆放着体育器材。"
    "门锁着——但锁已经生锈了。你用力一拧，锁就开了。"

    "里面很暗。你眯起眼睛适应光线。"
    "角落里堆着几块旧垫子、一筐落满灰的篮球。"
    "墙上挂着一面破旧的横幅——「第二十三届校运动会」"

    "你在垫子底下翻到了一个书包。"
    "灰蓝色的。拉链上挂着一个褪色的钥匙扣——一个小熊形状的。"
    "书包很旧——像是很多年前被人遗忘在这里的。"

    "你打开它。"
    "里面有几本课本——封面上写着名字，但已经模糊到看不清了。"
    "一个文具盒。半截铅笔。"
    "还有一个信封。"

    "信封没有封口。里面装着一张照片。"
    "照片上是六个学生——穿着老款校服。"
    "他们并排站在校门前。"
    "站在中间的人——手里拿着一枚吊坠。"

    "那枚吊坠的形状——"
    "和你之前在行政楼见过的面具图案，一模一样。"

    show lv normal
    with dissolve

    lv "……这是。"

    "你盯着照片看了很久。"
    "那六个学生。他们的表情——"
    "不像是在拍照。"
    "像是在等待什么。"

    "你把照片收好。"

    if "old_photo" not in docs_found:
        $ docs_found.append("old_photo")
        "（「旧照片——十五年前的六名学生」加入你的文档）"

    return

# --- 绕跑道走一圈 ---
label w1d3_playground_lap:
    $ stamina_use(10)

    "你沿着跑道走了一圈。"
    "四百米的标准跑道。每一步都很均匀。"
    "你的脚步在塑胶地面上发出轻微的摩擦声。"

    "走到主席台前的时候——"
    "你停下了。"

    "主席台上放着一把椅子。"
    "孤零零的——摆在正中央。"
    "像是有谁曾经坐在这里，看着空荡荡的操场。"

    "椅子旁边的地面上——"
    "有一个烟头。"

    "不是很久以前的烟头。"
    "烟嘴上的滤纸还很白。"
    "是今天的——或者昨晚的。"

    show lv normal
    with dissolve

    lv "学校里还有人。"

    "这不是一个疑问句。"
    "你感到脊背发凉。"
    "除了吴玄吉……还有别人。"

    $ wxj_alert += 15

    return

# ============================================================
# w1d3 · 广播室（新地点）
# ============================================================
label w1d3_broadcast_room:
    scene corridor_day
    with fade

    "广播室在教学楼的三楼——楼梯口右边走廊的尽头。"
    "你之前从来没进去过。"
    "门上挂着一块铁牌：「校园广播站 · 非工作人员勿入」"

    "门没有锁。"

    $ stamina_use(5)

    scene broadcast_room
    with fade

    "你推开门。"
    "广播室比你想象的小——大约十平方米。"
    "靠墙摆着一张桌子，上面放着麦克风和调音台。"
    "调音台的电源指示灯还亮着——红色的微光在昏暗的房间里格外显眼。"

    "墙壁上贴满了隔音海绵——有些已经脱落了，露出灰白的墙面。"
    "墙角有一个铁皮柜。柜门半开——里面放着几盘老旧的磁带和CD。"

    "你走到调音台前。"
    "麦克风还开着。"
    "桌上的笔记本翻开到最新一页——"

    "你弯下腰读了几行。"

    "「Day 1：正常播报。没有人注意到。」"
    "「Day 2：取消了春游。他们照做了。」"
    "「Day 3：所有学生回到教室。像什么都没发生过。」"
    "「效果超出预期。面具大人的力量……是真的。」"

    show lv fright
    with dissolve

    "你的血液一瞬间凝固了。"

    lv "这是——"

    "这是广播员的工作日志。"
    "但字迹——你认得。"
    "这是班主任的笔迹。"

    "你继续翻。"

    "「明天会有更多人消失。一切按计划进行。」"
    "「没有人会记得他们。」"

    "你深吸一口气。"
    "这个房间让你喘不过气来。"

    "你合上笔记本。把它拿了起来。"

    if "broadcast_log" not in docs_found:
        $ docs_found.append("broadcast_log")
        "（「广播室工作日志」加入你的文档）"

    "角落里还有一张打印纸——像是操作手册的一部分。"

    menu:
        "仔细查看":
            "你拿起那张纸。"
            "上面写着广播设备的操作流程——"
            "但在最底部，有一行手写的备注："
            "「※ 面具模式：长按红色按钮三秒，切换至预设广播内容」"
            "你看了看调音台——"
            "确实有一个红色按钮。被一个塑料盖罩着。"
            "像是在防止误触。"
            $ has_noticed = True
        "先离开":
            "你没有继续查看。"
            "这个地方让你不安。"
            "你决定先出去再说。"

    "你走出广播室。"
    "心跳还没平复。"
    "班主任——她也参与了这件事。"

    $ broadcast_room_done = True

    jump w1d3_explore

# ============================================================
# w1d3 · 保安室（新地点）
# ============================================================
label w1d3_security_room:
    scene security_room
    with fade

    "保安室在教学楼一楼西侧——你路过它无数次，但从没进去过。"

    "门开着。"
    "里面一片狼藉。"

    "你跨过门槛。"
    "房间不大——一张桌子、一把椅子、一个文件柜、一台挂在墙上的监控显示器。"
    "监控屏幕全黑——不是关闭了，而是摄像头被切断了。屏幕一片漆黑。"

    "桌面上摊着一本签到簿。"
    "最新的签到记录停留在两天前——"
    "「夜班 · 晚8:00 — 早6:00 · 一切正常」"
    "从那以后就没有记录了。"

    $ stamina_use(5)

    menu security_loop:
        "检查文件柜":
            call w1d3_security_filing from _call_sec_filing
            jump security_loop
        "检查监控设备":
            call w1d3_security_monitor from _call_sec_monitor
            jump security_loop
        "搜查桌面和抽屉":
            call w1d3_security_desk from _call_sec_desk
            jump security_loop
        "离开保安室":
            "你走出了保安室。"
            $ security_room_done = True
            jump w1d3_explore

# --- 文件柜 ---
label w1d3_security_filing:
    "文件柜锁着。"
    "但锁很老旧——你试着用之前找到的储物柜钥匙捅了捅——"

    if "locker_key" in keys_inv:
        "咔哒一声——锁开了！"
        "你拉开柜门。"
        "里面叠放着一排文件——大多是出入记录和值班表。"
        "你快速翻了一遍——"
        "大部分内容都很正常。直到你看到一份被单独抽出来的档案。"

        "封面上写着："
        "「2011年 — 特殊事件记录」"

        "你打开它。"
        "里面只有一页纸。"
        "上面写着一行字——"

        "「春游事件 · 全员失联 · 三日后半数返回 · 无记忆 · 档案封锁」"

        show lv normal
        with dissolve

        lv "……春游事件？"

        "你翻回封面——日期是2011年。"
        "十五年前的春天。"

        "你快速把这份档案收好。"

        if "security_archive" not in docs_found:
            $ docs_found.append("security_archive")
            "（「保安室档案·2011特殊事件记录」加入你的文档）"
    else:
        "锁太结实了。你打不开。"
        "也许你需要找到正确的钥匙。"

    return

# --- 监控设备 ---
label w1d3_security_monitor:
    "你走到监控台前。"
    "显示器的主机还在运转——风扇发出轻微的嗡鸣。"
    "但所有画面都是黑的。"

    "你试着按了几个按钮——"
    "屏幕上出现了几行日志。"

    "「摄像头 #01 教学楼东 · 离线」"
    "「摄像头 #02 教学楼西 · 离线」"
    "「摄像头 #03 行政楼入口 · 离线」"
    "「摄像头 #04 校门主入口 · 离线」"
    "所有摄像头——全部离线。"

    "但日志的最后一行——"
    "「摄像头 #05 食堂后厨 · 信号中断 — 最后画面：23:44」"

    "你看了看时间。"
    "你的手表已经不走了。"
    "但你记得你到食堂的时候，后厨的汤还是温的。"

    "23:44。那是两天前的深夜。"

    "也就是说——"
    "食堂后厨的摄像头，在所有人消失的那天晚上，"
    "拍到了什么。"

    return

# --- 桌面抽屉 ---
label w1d3_security_desk:
    "保安的桌面上没什么特别的——一个空茶杯、一盒薄荷糖、半包烟。"
    "你拉开抽屉。"
    "里面有一串钥匙、一张地图和一本翻旧了的杂志。"

    "你拿起那串钥匙——大部分都用不上。但有一把看起来像是开文件柜的。"

    "你展开地图——"
    "是学校的手绘平面图。标注得相当详细。"
    "教学楼、行政楼、食堂、宿舍——每个房间都有编号。"
    "但你注意到——地图上标注了一个没有编号的入口。"

    "就在食堂后厨的冷藏室旁边。"
    "用红笔圈了出来，旁边写着四个字——"

    "「通往底下」"

    show lv normal
    with dissolve

    lv "……底下？"

    "你盯着那个红圈。"
    "学校里还有地下空间？"

    "你从没听说过。"
    "但地图不会撒谎。"

    if "school_map" not in docs_found:
        $ docs_found.append("school_map")
        "（「学校平面图」加入你的文档）"

    $ has_noticed = True

    return

# ============================================================
# w1d3 · 行政楼入口（氛围扩展）
# ============================================================
label w1d3_admin:
    scene building_day
    with fade

    "你站在行政楼前。"
    "这栋楼比你印象中矮了一截——或者是因为周围的空旷让它显得如此。"
    "墙面上的瓷砖有一些脱落的痕迹。墙角的排水管锈迹斑斑。"
    "大门紧闭着——门把手是新换的，和周围的老旧格格不入。"

    "你推开门——"
    "一股冷气从门缝里涌出来。"
    "像是空调开了一整夜。但现在是春天。没有人会开空调。"

    "你走进大厅。"

    scene office_hall
    with fade

    "大厅里的灯亮着。"
    "日光灯发出惨白的光——照亮了地面上凌乱的脚印。"
    "脚印很多——有大有小，有新有旧。"
    "不像是一个人留下的。"

    "你低头看了看——"
    "这些脚印全都通向走廊深处。"

    "你顺着脚印的方向看过去——"
    "走廊尽头，校长办公室的门虚掩着。"

    $ stamina_use(5)

    menu admin_loop:
        "搜索一楼办公室" if not admin_floor1_done:
            $ found_key = False
            if "admin_key" not in keys_inv:
                "你在保安室的抽屉里找到了行政楼的备用钥匙。"
                $ keys_inv.append("admin_key")
                $ found_key = True
            if not found_key:
                "一楼已经没有什么有用的东西了。"
            $ admin_floor1_done = True
            $ wxj_alert += 15
            jump admin_loop
        "上二楼" if not admin_floor2_done:
            scene office_hall
            with fade
            "你走上二楼。"
            "走廊尽头是校长办公室。"
            "门锁着。"
            "但门缝下透出一丝光亮。"
            "里面有人。"
            $ wxj_alert += 20
            menu:
                "敲门":
                    jump w1d3_knock_door
                "撤退——被发现就完了":
                    jump admin_loop
        "离开行政楼":
            "你走出了行政楼。"
            jump w1d3_explore

# ============================================================
# w1d3 · 敲门（吴玄吉会面）
# ============================================================
label w1d3_knock_door:
    "你深吸一口气——敲了敲门。"

    "门内的动静停了。"
    "脚步声。"
    "门开了一条缝。"

    show wxj normal at center
    with dissolve

    "一张肥胖的脸从门缝里探出来。"
    "长发遮住了半边脸。"

    "你们对视了一秒——"
    "双方都认出了对方。"

    wxj "……是你啊。"

    show lv normal
    lv "吴玄吉……你怎么在这？"

    wxj "这话该我问你吧，吕文强。"
    wxj "你来行政楼干什么？"

    show lv fright
    menu:
        "问他知不知道发生了什么":
            lv "学校里的人呢？你知道怎么回事吗？"
            wxj "我怎么知道。我一觉醒来就这样了。"
            wxj "到处走了走——一个人都没有。"
            wxj "食堂没人，教学楼没人。连保安室都没人。"
            "他说话的时候一直在笑。但你看得出来——他在紧张。"
            $ wxj_alert += 15
            $ admin_floor2_done = True
            jump w1d3_explore
        "质问他——你在校长室干什么":
            lv "你才是，你来校长室干什么？"
            "他没有立刻回答。"
            "你注意到他手里攥着一张纸——粉色封面的。"
            "你认得那种纸。保送推荐表。"
            wxj "……你看到了？"
            "空气有些微妙。"
            lv "……你跟校长说了什么？"
            wxj "呵。"
            "他关上了门。"
            "你听到里面传来上锁的声音。"
            $ wxj_alert += 25
            $ admin_floor2_done = True
            jump w1d3_explore
        "撤退":
            "你后退了一步。"
            "你说了声打扰了，转身离开。"
            "你感觉他的目光一直钉在你背上。"
            jump admin_loop

# ============================================================
# w1d3 · 吴玄吉追逐
# ============================================================
label w1d3_wxj_chase:
    stop music

    "脚步声越来越近。"

    show wxj normal at center
    with vpunch

    wxj "吕文强——"

    "他找到你了。"

    menu:
        "跑！":
            $ stamina_use(20)
            "你转身就跑。"
            jump w1d3_running
        "躲进附近的教室":
            if hide_cooldown <= 0:
                jump w1d3_hide
            else:
                "你刚躲过一次，现在没有合适的藏身处了。只能跑。"
                jump w1d3_running

# ============================================================
# w1d3 · 奔跑
# ============================================================
label w1d3_running:
    play sound "footstep_02.mp3"
    "你拼命跑。"
    "楼梯在脚下飞速后退。"
    "你推开门——冲进走廊——"

    $ wxj_alert = max(0, wxj_alert - 30)

    "脚步声从你面前经过——渐渐远去。"

    "你安全了。"

    play music "suhuan1.mp3" fadein 2.0 loop

    $ stamina_use(5)

    jump w1d3_explore

# ============================================================
# w1d3 · 躲藏
# ============================================================
label w1d3_hide:
    scene black
    with dissolve

    "你闪进旁边的教室，关上门，蹲在讲台后面。"

    "脚步声越来越近——"
    "然后经过了你的门口。"

    "没有停下。"

    "你松了一口气。"

    $ wxj_alert = max(0, wxj_alert - 40)
    $ hide_cooldown = 3

    play music "suhuan1.mp3" fadein 2.0 loop

    jump w1d3_explore

# ============================================================
# w1d3 · 被抓
# ============================================================
label w1d3_caught:
    scene black
    with fade

    "你没能逃掉。"

    show wxj normal at center
    with dissolve

    wxj "别跑了。"
    wxj "我带你去见校长。"

    menu:
        "拼了！":
            $ stamina_use(25)
            "你猛地撞向吴玄吉。"
            "他踉跄了两步——"
            "你趁机挣脱，拼命往前跑。"
            $ wxj_alert = max(0, wxj_alert - 50)
            "这次你跑得很远，直到完全听不到他的声音才停下。"
            play music "suhuan1.mp3" fadein 2.0 loop
            jump w1d3_explore
        "……放弃抵抗":
            "你垂下肩膀。"
            "吴玄吉带着你走向行政楼深处……"

            scene office_principal
            with fade

            "你被推进了一间黑暗的办公室。"
            "门在你身后关上。锁死了。"

            scene black
            with fade

            "不知过了多久。"
            "门开了——"
            "阳光从门缝里照进来。"

            "是第二天早上了。"

            $ stamina = stamina_max
            $ wxj_alert = 0

            jump w1d4_preview

# ============================================================
# w1d3 · 时间推进（多次探索后触发）
# ============================================================
label w1d3_time_advance:
    if w1d3_phase < 3:
        $ w1d3_phase += 1
        if w1d3_phase == 1:
            "时间悄悄流逝。阳光移到了头顶——已经上午了。"
        elif w1d3_phase == 2:
            "太阳开始偏西。已经是下午了。你还没有找到所有答案。"
        elif w1d3_phase == 3:
            "天色渐晚。黄昏的橘色光线将校园染上了一层不真实的颜色。"
            "你最好抓紧时间——天一黑，校园里会变得更危险。"
    else:
        "夜幕即将降临。你该回宿舍了。"

    jump w1d3_explore

# ============================================================
# w1d3 · 宿舍休息（丰富版·反思）
# ============================================================
label w1d3_dorm_rest:

    # 如果在被吴玄吉追捕时休息 → 死亡
    if wxj_alert >= 100:
        scene dorm_day
        with fade
        "你冲进宿舍，锁上门。"
        "靠在门板上大口喘气——"
        "砰！砰！砰！"
        "门板剧烈震动。"
        show wxj normal
        wxj "开门。"
        wxj "我知道你在里面。"
        "你捂住嘴，不敢出声。"
        show wxj angry
        "砰！！"
        "门被撞开了——"
        scene black
        with vpunch
        "你没能逃掉。"
        jump w1d3_wxj_caught_death

    scene dorm_dusk
    with fade

    "你回到了宿舍。"

    "推开门的那一刻——"
    "你有一种错觉：室友们随时会推门进来，问你今天怎么样。"
    "但没有人来。"
    "房间里的东西和你离开时一模一样。"

    "你坐在床边。"
    "脱下鞋——脚底板已经有些发麻了。"
    "你找了很久。走了很多地方。"

    "——你找到了什么？"

    "你闭上眼睛，整理今天的收获。"

    if len(docs_found) > 0:
        "你翻看了今天找到的东西："
        $ doc_names = {
            "doc_newspaper": "一份旧报纸剪报",
            "doc_contract": "一份烧了一半的合同",
            "doc_student_list": "一张残缺的学生名单",
            "photo_half": "半张毕业照",
            "old_photo": "一张十五年前的六人照片",
            "broadcast_log": "广播站的工作日志",
            "security_archive": "保安室·2011特殊事件档案",
            "school_map": "学校平面图"
        }
        python:
            docs_list = [doc_names.get(d, d) for d in docs_found]
            if docs_list:
                for doc in docs_list:
                    renpy.say(None, "• " + doc)
        "这些线索在你脑子里打转。"
        "你还没有完全理解它们之间的联系——"
        "但你有一个直觉：所有答案，都指向一个地方。"
    else:
        "你翻了翻口袋——什么也没有找到。"
        lv "……今天白忙了。"

    "你倒在床上。"
    "天花板的裂缝在昏暗中看起来像一张地图。"
    "你闭上眼。"

    "疲惫像潮水一样涌来。"
    "意识渐渐模糊……"

    jump w1d4_transition

# ============================================================
# w1d3 · 精力耗尽（强制推进）
# ============================================================
label w1d3_forced_rest:
    scene black
    with fade

    "你的腿像灌了铅一样沉重。"
    "视线开始模糊……"
    "你已经没有力气了。"

    "你跌跌撞撞地走回宿舍。"
    "连衣服都没脱就倒在了床上。"
    "意识在一片黑暗中沉了下去……"

    jump w1d4_transition

# ============================================================
# w1d3 · 过渡到 w1d4
# ============================================================
label w1d4_transition:
    scene black
    with fade

    "当阳光再次照在你脸上的时候——"
    "已经是新的一天了。"

    $ stamina = stamina_max
    $ wxj_alert = max(0, wxj_alert - 30)

    "你活过了第三天。"

    jump w1d4_preview
