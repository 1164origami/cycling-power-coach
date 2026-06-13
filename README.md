# 🚴 cycling-power-coach

自行车功率训练专家 Skill — 基于 Joe Friel《自行车功率训练完全指南》的专业方法论，结合 Coggan/Allen、Seiler 等学者的最新研究。

## 功能

- 📊 **功率数据分析** — 解读 NP/TSS/IF/VI/峰值功率曲线/MMP/PMC
- 🎯 **FTP 与功率区间** — 确定 FTP，设定 7 区功率训练区间
- 📅 **周期化训练计划** — 基础期/强化期/巅峰期完整计划
- 🏆 **专项比赛策略** — 公路赛/计时赛/铁三/Century
- 🔬 **高级分析** — 耐久性(Durability)、踏频衰减、W'管理
- 🧪 **极化训练** — 80/20 模型与 Seiler 方法论

## 安装

将此 Skill 放入 QClaw/OpenClaw 的 skills 目录：

```bash
cp -r cycling-power-coach/ ~/.qclaw/skills/
```

## 使用示例

```
用户: "我的 FTP 是 250W，帮我设定功率区间"
用户: "分析我的比赛功率文件，看看节奏有没有问题"
用户: "离比赛还有 12 周，帮我制定一个训练计划"
用户: "什么是极化训练？和甜区训练有什么区别？"
```

## 参考文件

| 文件 | 内容 |
|------|------|
| `SKILL.md` | 核心框架、速查表、诊断流程 |
| `references/training_plans.md` | 具体训练计划模板 |
| `references/data_analysis.md` | 功率数据分析方法 |
| `references/race_specific.md` | 专项比赛策略 |
| `references/concepts_glossary.md` | 术语表 |
| `references/advanced_data_analysis.md` | Coggan/Allen 深度分析 |
| `references/polarized_training.md` | Seiler 极化训练模型 |
| `references/indoor_training.md` | 室内骑行训练 |
| `references/hiit_and_vo2max.md` | HIIT 与 VO₂max 科学 |
| `references/overtraining_and_recovery.md` | 过度训练与恢复 |
| `references/critical_power_and_w_prime.md` | 临界功率与 W' 模型 |

## 知识来源

- Joe Friel《自行车功率训练完全指南》
- Hunter Allen & Andrew Coggan《Training and Racing with a Power Meter》
- Stephen Seiler 极化训练研究
- Dylan Johnson 科学训练分析
- 多篇同行评审运动科学论文（PMID 标注）

## License

MIT
