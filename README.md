<p align="center">
  <img src="https://img.shields.io/badge/Codex-Skill-0A73B8?style=for-the-badge" alt="Codex Skill" />
  <img src="https://img.shields.io/badge/Agent_Skills-Open_Standard-2A9D8F?style=for-the-badge" alt="Agent Skills" />
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

**Cycling Power Coach** 是一个以 **OpenAI Codex** 为主要使用环境、兼容开放 Agent Skills 规范的自行车功率训练知识型 Skill。基于 Joe Friel 的训练框架，结合 Coggan/Allen 功率数据分析、Seiler 强度分布及运动科学资料，帮助骑行者理解FTP、NP、TSS、IF、CTL/ATL/TSB、耐久性和训练恢复。

**Cycling Power Coach** is a Codex-first, portable Agent Skill for power-based endurance coaching, training analysis, return-to-riding progression and evidence-aware cycling decisions.

> **训练决策原则**：结合功率数据、RPE、疼痛/麻木、睡眠、补水补给和个体目标综合判断。与姿势或接触点疼痛有关的问题，请交叉参考 [bike-fit-guide](https://github.com/1164origami/bike-fit-guide)。不以平台恢复分数单独决定是否可以训练。

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

## 📦 在 Codex 中安装 · Installation

本仓库是标准的 `SKILL.md` + `references/` 知识型 Skill，无需 Python 包或后台进程。**个人级安装目录推荐 `$HOME/.agents/skills/`**。

### Windows PowerShell（推荐）

```powershell
$skillsRoot = Join-Path $HOME ".agents\skills"
New-Item -ItemType Directory -Force -Path $skillsRoot | Out-Null
git clone https://github.com/1164origami/cycling-power-coach.git (Join-Path $skillsRoot "cycling-power-coach")
```

已克隆的用户可使用 `git -C (Join-Path $HOME '.agents\skills\cycling-power-coach') pull --ff-only` 更新。

### macOS / Linux

```bash
mkdir -p "$HOME/.agents/skills"
git clone https://github.com/1164origami/cycling-power-coach.git "$HOME/.agents/skills/cycling-power-coach"
```

如只需在一个工作仓库内使用，也可克隆到该仓库 `.agents/skills/cycling-power-coach/`。

### 调用示例

- 显式调用：`$cycling-power-coach`，或在 Codex 中打开 `/skills` 选择。
- 提示词示例：`使用 $cycling-power-coach 读取我已授权的训练记录，对比最近两次骑行的功率保持、RPE和恢复情况，制定下次轻松骑的方案。`
- Codex 也可能根据 `SKILL.md` 描述自动选择，但并不保证每次关键词匹配都触发。
- Codex 检测安装或更新一般不需特殊操作；若新 Skill 未出现可重启。详见 [Codex Skills 官方文档](https://developers.openai.com/codex/skills)。

### 与高驰、Intervals.icu 数据配合

本仓库只定义**分析流程**，不会自动获得 COROS/高驰或 Intervals.icu 权限。Codex 如已配置相应插件/MCP且得到用户授权，可按 [多源教练协议](references/multisource_coaching.md) 读取训练信息；否则可分析用户明确提供的脱敏记录。默认只读，不自动修改FTP、训练日历或路书。公开仓库不要写入私人运动数据及GPS家庭轨迹。

---
## 🗂️ 文件结构 · Structure

```text
cycling-power-coach/
├── SKILL.md                           # Codex 触发描述与主要工作流
├── README.md                          # 安装与项目说明
├── AGENTS.md                          # Codex 维护本仓库的规范
├── agents/openai.yaml                 # 可选界面元数据
├── references/
│   ├── training_plans.md
│   ├── data_analysis.md
│   ├── race_specific.md
│   ├── concepts_glossary.md
│   ├── advanced_data_analysis.md
│   ├── polarized_training.md
│   ├── indoor_training.md
│   ├── hiit_and_vo2max.md
│   ├── overtraining_and_recovery.md
│   ├── critical_power_and_w_prime.md
│   ├── multisource_coaching.md
│   └── return_to_riding.md
├── tests/validate_skill.py            # 静态校验
└── .github/workflows/skill-validation.yml
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
  <sub>Codex-first · Open Agent Skills</sub>
</p>

## 🧭 近期更新：多源数据训练与安全修订

本仓库提供**训练知识**，不自动取得用户运动账号权限。支持将已获授权的 COROS/高驰、Intervals.icu 记录与本人RPE、症状、睡眠、补给一起评估；跨平台同一次活动不重复计数。详见 [多源教练协议](references/multisource_coaching.md) 与 [复骑/100km分级指南](references/return_to_riding.md)。

此次修订校正 IF = NP/FTP、室内外FTP无固定高低关系、ERG最大努力测试的局限、个体化补水、心率功率解耦的条件，以及 **100公里不等于传统100英里Century**。公开仓库严禁提交私人训练文件、完整GPS轨迹、账号标识或健康记录。
