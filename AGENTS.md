# Codex repository maintenance guide

本仓库是 **Codex-first、兼容开放 Agent Skills** 的纯知识型技能。

- 根目录唯一 `SKILL.md` 必须具有 `name` 和短而明确的 `description`；将详细训练方法、数据字段与限制放在 `references/`，控制自动载入上下文长度。
- 文档默认**先核实指标来源和数据质量**，再分析功率、心率、负荷与RPE；`IF = NP/FTP`，不同平台负荷不等价，Century英里与100公里不同。
- 时间、时区、重复运动、旧FTP与eFTP、设备未同步等问题不得忽略。运动员报告的腰痛、手麻、异常疲劳具有更高安全优先级。
- 若任务涉及姿势/坐垫或疼痛分布，与 `1164origami/bike-fit-guide` 交叉参考；避免把纯训练Skill写成医学诊断器。
- `README.md` 的安装路径与调用方式要使用目前的 Codex Skill 标准；不要引入废弃的工具平台品牌或其专属安装目录。
- COROS/Intervals.icu 连接需要用户独立授权；未经明确确认不写入运动日历、改FTP或上传路书。**不得将个人训练记录、完整GPS或令牌提交到公开仓库。**
- 每次修改运行 `python tests/validate_skill.py`，检查引用、公式和安全规则。
