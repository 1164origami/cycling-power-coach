<p align="center">
  <img src="https://img.shields.io/badge/OpenClaw-Skill-6C5CE7?style=for-the-badge" alt="OpenClaw Skill" />
  <img src="https://img.shields.io/badge/QClaw-Skill-6C5CE7?style=for-the-badge" alt="QClaw Skill" />
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" alt="MIT License" />
</p>

<h1 align="center">⚡ Cycling Power Coach</h1>
<h3 align="center">自行车功率训练教练</h3>
<h3 align="center"><i>Power-Based Cycling Training Guide</i></h3>

<p align="center">
  <i>Joe Friel's "The Power Meter Handbook" + integrated sports science research</i>
  <br/>
  <i>Joe Friel《自行车功率训练完全指南》+ 运动科学前沿研究整合</i>
</p>

---

## 📖 简介 · Introduction

**Cycling Power Coach** 是一个 OpenClaw / QClaw Skill，提供科学、系统化的自行车功率训练指导。融合 Joe Friel 经典方法论与 Coggan/Allen（PMC / MMP）、Stephen Seiler（极化训练）、Dylan Johnson 及同行评审运动科学的前沿研究。

**Cycling Power Coach** is an OpenClaw / QClaw Skill providing scientific, systematic power-based cycling training guidance. Integrates Joe Friel's classic methodology with cutting-edge research from Coggan/Allen (PMC, MMP), Stephen Seiler (polarized training), Dylan Johnson, and peer-reviewed sports science.

> ⚠️ **OpenClaw / QClaw Skill** — 为 AI 助手提供功率训练结构化知识库。触发关键词：功率训练、FTP、TSS、NP、训练区间、周期化、比赛策略等。
>
> ⚠️ **OpenClaw / QClaw Skill** — provides structured power training knowledge for AI assistants. Triggered by: power training, FTP, TSS, NP, training zones, periodization, race strategy, etc.

---

## ✨ 功能 · Features

### 📊 数据分析 · Data Analysis

| Feature · 功能 | Description · 说明 |
|---------------|-------------------|
| NP / TSS / IF / VI | 功率数据核心指标解读<br>Core power metrics interpretation |
| MMP 曲线 · MMP Curve | 均值最大化功率曲线分析<br>Mean Maximal Power curve analysis |
| PMC 图表 · PMC Chart | 性能管理图表（CTL / ATL / TSB）<br>Performance Management Chart (CTL / ATL / TSB) |
| 解耦 Pw:HR · Decoupling | 有氧耐力评估<br>Aerobic endurance assessment |
| 耐久性 · Durability | 功率衰减监测<br>Power decay monitoring under fatigue |
| 踏频衰减 · Cadence Decline | 急性疲劳实时监测<br>Real-time acute fatigue tracking |

### 🎯 训练指导 · Training

| Feature · 功能 | Description · 说明 |
|---------------|-------------------|
| FTP 测定 · FTP Testing | 7 种方法按准确度排序<br>7 methods ranked by accuracy |
| 7 区功率区间 · 7 Power Zones | 基于 FTP 百分比的训练区间<br>FTP percentage-based training zones |
| 周期化训练 · Periodization | 基础期 → 强化期 → 巅峰期<br>Base → Build → Peak |
| 训练六要素 · 6 Abilities | 有氧/力量/速度/肌耐力/无氧/冲刺<br>Endurance/Force/Speed/Muscular/Anaerobic/Sprint |
| 极化训练 · Polarized | 80/20 模型 & Seiler 方法论<br>80/20 model & Seiler methodology |

### 🏆 比赛策略 · Race Strategy

| Feature · 功能 | Description · 说明 |
|---------------|-------------------|
| 公路赛 · Road Race | 火柴管理 & VI 控制<br>Match management & VI control |
| 计时赛 · Time Trial | 完美节奏 VI ≤ 1.05<br>Perfect pacing VI ≤ 1.05 |
| 铁三 · Triathlon | Ironman 精英 vs 年龄组 IF 范围<br>Ironman elite vs age-group IF ranges |
| 长距离 · Century | 4 小时+ 配速策略<br>4h+ pacing strategy |

### 🔬 进阶分析 · Advanced

| Feature · 功能 | Description · 说明 |
|---------------|-------------------|
| CP & W' | 临界功率模型 & W' 储备管理<br>Critical Power model & W' balance management |
| HIIT & VO₂max | 高强度间歇训练科学<br>High-intensity interval training science |
| 室内训练 · Indoor | ERG vs 坡度模式、热管理<br>ERG vs slope mode, heat management |
| 过度训练 · Overtraining | 征兆识别 & 恢复科学<br>Symptom identification & recovery science |

---

## 📦 安装 · Installation

### 依赖 · Requirements

本 Skill 为纯知识型（Markdown），无需额外依赖。

This is a knowledge-only Skill (Markdown), no additional dependencies required.

### For OpenClaw / QClaw

```bash
# Option A: Git Clone（推荐 · Recommended）
git clone https://github.com/1164origami/cycling-power-coach.git ~/.qclaw/skills/cycling-power-coach

# Option B: 手动复制 · Manual Copy
cp -r cycling-power-coach/ ~/.qclaw/skills/

# Option C: OpenClaw workspace
cp -r cycling-power-coach/ <your-openclaw-workspace>/skills/
```

当对话涉及功率训练、FTP、训练区间、比赛策略等关键词时，AI 助手会自动加载此技能。

The AI assistant auto-loads this skill when triggered by power training, FTP, training zones, or race strategy keywords.

---

## 🗂️ 文件结构 · Structure

```
cycling-power-coach/
├── SKILL.md                              # 核心技能定义 · Core（速查表 & 诊断流程）
├── README.md                             # 本文件 · This file
├── LICENSE                               # MIT License
├── .gitignore
└── references/                           # 分层知识库 · Layered knowledge base（按需加载）
    ├── training_plans.md                 # 训练计划模板 · Training plan templates
    ├── data_analysis.md                  # 功率数据分析方法 · Power data analysis methods
    ├── race_specific.md                  # 专项比赛策略 · Race-specific strategy
    ├── concepts_glossary.md              # 术语表 · Glossary of terms
    ├── advanced_data_analysis.md         # Coggan/Allen 深度分析 · Deep analytics
    ├── polarized_training.md             # Seiler 极化训练模型 · Polarized training model
    ├── indoor_training.md                # 室内骑行训练 · Indoor cycling training
    ├── hiit_and_vo2max.md                # HIIT & VO₂max 科学 · HIIT & VO₂max science
    ├── overtraining_and_recovery.md       # 过度训练 & 恢复 · Overtraining & recovery
    └── critical_power_and_w_prime.md     # CP & W' 模型 · CP & W' model
```

---

## 🚀 使用示例 · Usage

| 中文 | English |
|------|---------|
| "我的 FTP 是 250W，设定功率区间" | "My FTP is 250W, set my power zones" |
| "分析我的比赛功率数据" | "Analyze my race power data" |
| "离比赛还有 12 周，制定训练计划" | "12 weeks to race, create a training plan" |
| "什么是极化训练？" | "What is polarized training?" |
| "甜区训练和极化训练哪个好？" | "Sweet spot vs polarized — which is better?" |
| "如何提高 FTP？" | "How to increase my FTP?" |
| "过度训练有什么征兆？" | "What are signs of overtraining?" |
| "室内 Zwift 训练怎么安排？" | "How to structure indoor Zwift training?" |

---

## 📚 知识来源 · Knowledge Sources

| Source · 来源 | Content · 内容 |
|--------------|---------------|
| **Joe Friel** | 《自行车功率训练完全指南》— 训练框架 & 周期化<br>*The Power Meter Handbook* — training framework & periodization |
| **Allen & Coggan** | 《Training and Racing with a Power Meter》— PMC / MMP / W'<br>*Training and Racing with a Power Meter* (3rd Ed.) |
| **Stephen Seiler** | 极化训练模型 (80/20 Rule) · Polarized training model |
| **Dylan Johnson** | 甜区 vs 极化对比、Durability 训练<br>Sweet spot vs polarized, durability training |
| **同行评审 · Peer-reviewed** | 多篇 PMID 标注的运动科学论文<br>Multiple PMID-referenced sports science papers |

---

## 📄 许可协议 · License

MIT © [1164origami](https://github.com/1164origami)

---

<p align="center">
  <sub>用功率训练，以信心比赛 · Train with power, race with confidence</sub>
  <br/>
  <sub>Built for OpenClaw & QClaw</sub>
</p>
