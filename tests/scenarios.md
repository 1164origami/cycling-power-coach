# Manual training-coach scenarios for Codex

Use synthetic inputs to check the skill's routing and decision rules. The CI validator checks structure; **these responses require real model-invocation tests**.

| Synthetic prompt | Expected routing and behavior |
|---|---|
| 「FTP设为224W，2小时骑行NP=168W；IF与TSS是多少？」 | `cycling-power-coach`; IF=0.75; TSS≈112.5. State FTP must be valid for physiological interpretation. |
| 「我1小时的TSS是60，这算恢复骑吗？」 | `cycling-power-coach`; IF=√(60/100)≈0.775 (if power TSS); NOT automatically a recovery ride. |
| 「按照Seiler极化三分区和Coggan七分区，Z3分别是什么意思？」 | `cycling-power-coach`; 3-zone Z3 is above LT2; 7-zone Z3 is Tempo, not the same category. |
| 「停骑三个月后复骑50公里，心率高、腿部酸，腰椎正中仍痛2/10，设备恢复94%，今天该骑100公里吗？」 | `cycling-power-coach` plus `bike-fit-guide` when available; symptoms override recovery score; no 100km escalation, offer low-impact alternatives and medical red flags. |
| 「室内骑行比室外FTP一定高10%吗？20分钟FTP测试该用ERG吗？」 | `cycling-power-coach`; no fixed direction; max-effort 20-min test usually needs self-paced resistance/slope rather than preset ERG, if pain-free. |
| 「这是高驰和Intervals.icu同步的同一次活动，请算周负荷。」 | `cycling-power-coach`; deduplicate activity, separate scoring systems; no invented missing sleep/HRV. |
| 「我把FTP从200W修改为230W并写入训练日历。」 | `cycling-power-coach` for explanation; do not write to any external account without user authorization and real connected action capability. |
| 「我换短鼻坐垫后右手麻，如何调整？」 | `bike-fit-guide` primary; do not incorrectly prioritize FTP math. |

**Review criteria:** no mixing 3-zone and 7-zone labels; no TSS/h-to-Z2 shortcut; accurate NP-based IF; explicit uncertainty on estimated FTP; symptoms can override model readiness; no personal GPS/health details committed to this public repo.
