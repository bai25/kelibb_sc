# 🏫 可堡灵之校 — Kebao Ling's School

> **校园悬疑·生存·文字AVG** | Ren'Py 8.3.2 | 开发中

---

## 📖 故事简介

一所普通的寄宿中学。六个被选中的学生代表。一个戴着白色面具的神秘校长。

春游的前一天，六名学生代表被召集到校长办公室。校长却迟迟没有出现——当主角走出办公室时，发现全校师生凭空消失了。

校门被封锁，通讯中断，一个自称「面具」的声音通过广播宣布了一切事物的新规则。

六人各怀异能——唯独主角，只是一个普通人。

---

## 🎮 游戏机制

- **难度选择**：简单 / 困难 / 噩梦
- **精力系统**：上限 50，行动消耗，可通过道具提升
- **可丽币**：校内货币，向商人「可丽堡」购买物资
- **角色切换**：主角阵亡后可切换至其他五名学生代表之一
- **多周目**：不同角色视角解锁不同剧情

### 六名学生代表

| 角色 | 能力 |
|------|------|
| **吕文强** | 无（普通人） |
| **张闻晦** | 可进入狭小空间 |
| **徐鸿昊** | 行动精力消耗 -2 |
| **严笳谌** | 能看懂特殊文字 |
| **吴机岩** | 可关闭监控 / 恢复供电 |
| **劳达** | 被发现的概率 -30% |

---

## 🎨 素材

- 画风：日系视觉小说风格（Ghibli 系暖色调）
- 所有立绘为透明 PNG，可直接在 Ren'Py 中使用
- 场景：中式校园（教室、宿舍、走廊、操场、校门等）

---

## 🛠️ 技术栈

- **引擎**：Ren'Py 8.3.2
- **图片生成**：通义万相 (DashScope)
- **构建平台**：Android / PC / Web

---

## 📂 项目结构

```
goblin-game/
├── game/
│   ├── script.rpy        # 主游戏脚本
│   ├── options.rpy       # 游戏配置
│   ├── screens.rpy       # 界面定义
│   ├── gui.rpy           # GUI 配置
│   ├── images/           # 图片素材
│   ├── audio/            # 音效文件
│   └── gui/              # UI 元素
├── .github/workflows/    # GitHub Actions CI
└── android.json          # Android 构建配置
```

---

## 🚀 运行方式

### PC 端
```bash
# 下载 Ren'Py SDK 8.3.2
# 将 goblin-game 放入 projects/ 目录
./renpy.sh projects/goblin-game
```

### Android
```bash
# 使用 Ren'Py Launcher → Build Android
# 或使用 GitHub Actions (见 .github/workflows/)
```

---

## 📝 当前版本

- **v0.2-alpha** — 一周目前两天剧情已完成
- 包含完整素材（立绘、场景、CG、音效）
- APK 下载：[GitHub Releases](https://github.com/bai25/kelibb_sc/releases)

---

## 📜 协议

MIT License
