# 临界功率与W'模型（Critical Power & W' Model）

基于功率-时长关系和W'平衡模型的最新研究。本文件为 `cycling-power-coach` 的补充参考。

[Created: 2026-05-17, Source: PMC13171990 - Welburn et al. (2026)]

---

## 核心概念

### 临界功率（Critical Power, CP）

CP是功率-时长关系中的功率渐近线，界分**重度强度域（Severe Domain）**和**高强度域**。CP反映最高可持续有氧代谢率。

- 骑行在CP以下：理论上可以无限持续（实际受糖原储备等限制）
- 骑行在CP以上：只能持续有限时间，受W'储备限制

### W'（W-prime）

W'是功率-时长曲线的曲率常数，代表**CP以上可完成的有限功量**（单位：千焦 kJ）。

- 经典理解：W'是固定的"无氧功储备"
- **最新证据**：W'并非固定参数（见下文）

### CP与FTP的关系

| 指标 | 定义 | 典型持续时间 | 关系 |
|------|------|-------------|------|
| **CP** | 功率-时长曲线渐近线 | ~40-60min 可持续 | 理论指标 |
| **FTP** | 60分钟最大平均功率 | 60min | 实用指标 |
| **乳酸阈值功率** | 血乳酸4mmol/L对应功率 | ~45-60min | 生理指标 |

> ⚠️ CP通常略高于FTP（约高3-5%），因为FTP是60分钟实测值而CP是数学外推。实际训练中FTP更实用。

---

## 最新研究：W'不是固定参数

### Welburn et al. (2026, PMC13171990)

**研究设计**：14名骑行者完成3种试验
1. 固定功率至W'消耗70%（90秒耗竭），然后降至CP+20W至力竭
2. 固定功率至W'消耗70%（180秒耗竭），然后降至CP+20W至力竭
3. 固定功率至5分钟力竭（P5），然后降功率继续至力竭，重复2次降功率

**关键发现**：

| 试验 | 实际做功 > CP | 比预测值多 | 实际TTE | 比预测值多 |
|------|-------------|----------|---------|----------|
| 90秒部分耗竭 | WORK90 | +5.4±0.7 kJ | TTE90 | +256±38 s |
| 180秒部分耗竭 | WORK180 | +4.3±1.3 kJ | TTE180 | +240±55 s |
| P5连续降功率 | WORKP5 | +2.7±0.4 kJ | TTEP5 | +109±12 s |

**核心结论**：
1. **W'不是固定参数**——当W'被部分消耗后，在CP以上继续做功的能力超过模型预测
2. 即使W'理论值为0 kJ时，**只要降低功率，仍可在CP以上继续做功**
3. 初始W'消耗速率可能是决定因素：快速消耗（90s）vs 慢速消耗（180s）影响后续表现

### 对训练和比赛的实操意义

**1. 间歇训练配速**：
- 传统CP/W'模型会低估间歇训练中的可持续做功量
- 在间歇组间降低功率时，W'可能部分"恢复"
- 这支持了**短间歇（30s-2min）比长间歇（5min+）更能利用W'"弹性"**的观点

**2. 比赛配速策略**：
- 突破后降功率（如追击后回到集团中）可延长高于CP的做功时间
- 纯匀速策略（TT）可能不是最优——适度的功率波动可利用W'的非固定特性
- 终点冲刺前保留W'的关键不是"省W'"，而是控制W'消耗速率

**3. 功率数据分析**：
- W'平衡模型（Skiba W'bal）可能**低估**间歇训练中的可用W'
- 解读W'bal数据时需考虑：W'消耗速率、恢复区间长度、个体差异
- 建议：W'bal作为**趋势参考**，而非绝对限制

### CP/W'模型的历史演变

| 时期 | 理解 | 代表研究 |
|------|------|---------|
| 1980s | W'是固定无氧功储备 | Moritani et al. (1981) |
| 2000s | W'可能是"疲劳级联"而非固定容器 | Murgatroyd et al. (2011) |
| 2013-2015 | 降功率后可在CP以上继续做功 | Chidnok et al. (2013), Dekerle et al. (2015) |
| **2026** | **W'不是固定参数，部分消耗后可持续做功超过预测** | Welburn et al. (2026) |

---

## 互补研究：mtDNA与VO₂max训练适应

### Sánchez Lorente et al. (2026, PMC13171954)

**研究设计**：
- 横断面：20名高度训练跑者 vs 20名未训练者
- 干预：6周HIIT跑步训练（4min/4min，每周3次）

**关键发现**：
- 高度训练跑者的白细胞mtDNA拷贝数**显著高于**未训练者（p=0.046，中等-大效应 d=0.652）
- mtDNA拷贝数与VO₂max**正相关**（p=0.013，R²=0.153）
- 6周HIIT后：VO₂max显著提高（p<0.001），mtDNA拷贝数增加321.6±391.6%
- **显著的个体差异**：提示存在"应答者 vs 无应答者"模式

**对骑行训练的意义**：
1. VO₂max训练适应有**分子层面基础**（线粒体生物发生）
2. 6周HIIT足以显著改变mtDNA——这是VO₂max提升的生物学标志
3. 个体差异大（321.6%±391.6%的增幅）说明**同一训练计划对不同人的效果差异巨大**
4. 支持个性化训练的必要性——监控个体对训练的实际反应比遵循固定计划更重要

---

## 三项训练负荷数据（Triathlon TL Reference）

### Wells et al. (2026, PMC13171522)

对95名年龄组三项运动员6个月内的34,731次训练课的数据分析：

| 参数 | 长距离组 | 短距离组 |
|------|---------|---------|
| 周训练时间 | 615 min/wk | 507 min/wk |
| 周距离 | 171 km/wk | 118 km/wk |
| 周TSS | 574 TSS/wk | 452 TSS/wk |

**训练阶段差异**：
- **专项期**最高负荷：556 min/wk, 166 km/wk, 620 TSS/wk
- **休赛期**最低：340 min/wk, 84 km/wk, 364 TSS/wk

**对骑行者的参考价值**：这些客观数据可作为年龄组运动员训练负荷比较的基准。

---

## 参考文献

1. Welburn, A.J. et al. (2026). "The effect of reducing work rate on total work done and time to task failure during severe intensity exercise." PMC13171990.
2. Sánchez Lorente, I.M. et al. (2026). "Adaptation of mtDNA content to endurance training, a cross-sectional study and an endurance training intervention." PMC13171954.
3. Wells, L.A. et al. (2026). "Training load and intensity in triathlon: objective differences between sex, age, race distance preference and training phase across a cohort of 95 age-group triathletes over six months." PMC13171522.
4. Jones, A.M. et al. (2010). "Critical power: implications for determination of VO2max and exercise tolerance." Med Sci Sports Exerc.
5. Skiba, P.F. et al. (2012). "Effect of work and recovery durations on W' reconstitution during intermittent exercise." Med Sci Sports Exerc.
6. Denham, J. et al. (2026). "Physiological and subjective measures of exercise intensity cycling at 55% and 85% of functional threshold power: Findings from a randomised crossover trial." J Sports Sci. doi: 10.1080/02640414.2026.2673477. PMID: 42148565.

---

## 补充：FTP百分比的生理学验证

[Updated: 2026-05-24, Source: Denham et al. (2026, PMID 42148565)]

### 研究设计

- 12名健康男性，随机交叉试验
- 测定VO₂max、FTP（递增负荷测试）
- 两次30分钟骑行：55% FTP vs 85% FTP
- 测量指标：摄氧量、心率、血乳酸、RPE（基线、15min、30min）

### 关键发现

| 指标 | 55% FTP | 85% FTP | 对应强度域 |
|------|---------|---------|-----------|
| 摄氧量变化 | 中等强度（相当于中等训练区） | 高强度 | 55%→中等, 85%→高强度 |
| 心率 | Z2范围 | Z4范围 | 一致 |
| 血乳酸 | <2mmol/L | >4mmol/L | 55%→低于LT, 85%→高于LT |
| RPE | 中等 | 高 | 85%的RPE高于FTP预测 |

### 核心结论

1. **55% FTP ≈ 中等强度训练**——与Z2定义（56-75% FTP）一致
2. **85% FTP ≈ 高强度训练**——但FTP百分比的解读**低估了≥85% FTP时的生理和心理需求**
3. 骑行者应**结合心率和RPE**来界定训练强度，FTP百分比单独使用在≥85% FTP时可能误导
4. 85% FTP的血乳酸和RPE均高于预期——这支持Z3上限（88-93% FTP）为"甜区"的合理性，但也暗示甜区训练的代价比一般认为的更高

### 对功率区间定义的影响

- 传统Z3（76-90% FTP）的**上限**可能需要重新审视——85% FTP已是高强度域
- 建议在≥85% FTP训练时，**用心率和RPE双重验证**实际强度
- 这与cycling-power-coach SKILL.md中"Z4训练回报高但成本极高"的结论一致

> 📌 本文件建议在用户询问"CP"、"临界功率"、"W'"、"W prime"、"功率时长关系"、"间歇配速"、"FTP百分比"、"功率区间验证"时读取。
