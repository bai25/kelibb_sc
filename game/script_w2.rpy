# ============================================================
# 可堡灵之校 v2 - w2 · 角色切换
# ============================================================

label w2_character_select:
    scene black
    with fade
    play music "suhuan1.mp3" fadein 2.0 loop

    "吕文强……失去了意识。"
    "但他的故事还没有结束。"
    "或者说——"
    "这里每个人的故事，才刚刚开始。"

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
