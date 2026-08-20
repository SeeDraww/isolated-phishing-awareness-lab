from pathlib import Path
import csv
import matplotlib.pyplot as plt

DATA = Path(__file__).resolve().parents[1] / "data"
CHARTS = Path(__file__).resolve().parents[1] / "charts"
CHARTS.mkdir(exist_ok=True)

files = {
    "Scenario A - Template": DATA / "scenario_a.csv",
    "Scenario B - Benefits": DATA / "scenario_b.csv",
    "Scenario C - Acknowledgment": DATA / "scenario_c.csv",
}

rows_by_scenario = {}
for name, path in files.items():
    with path.open(newline="", encoding="utf-8-sig") as f:
        rows_by_scenario[name] = list(csv.DictReader(f))


def value(row, *names):
    lowered = {str(k).strip().lower(): (v or "") for k, v in row.items()}
    for name in names:
        if name.lower() in lowered:
            return lowered[name.lower()].strip().lower()
    return ""

summary = []
for name, rows in rows_by_scenario.items():
    sent = len(rows)
    opened = sum(value(r, "status") in {"opened", "clicked", "submitted data", "submitted"} for r in rows)
    clicked = sum(value(r, "status") in {"clicked", "submitted data", "submitted"} for r in rows)
    submitted = sum(value(r, "status") in {"submitted data", "submitted"} for r in rows)
    summary.append((name, sent, opened, clicked, submitted))

report = Path(__file__).resolve().parents[1] / "data" / "summary.csv"
with report.open("w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["scenario", "emails_sent", "opens", "clicks", "submissions", "open_rate", "click_rate", "submission_rate"])
    for name, sent, opened, clicked, submitted in summary:
        denom = sent or 1
        writer.writerow([name, sent, opened, clicked, submitted, round(opened/denom*100, 1), round(clicked/denom*100, 1), round(submitted/denom*100, 1)])

labels = [x[0] for x in summary]
open_rates = [x[2] / (x[1] or 1) * 100 for x in summary]
click_rates = [x[3] / (x[1] or 1) * 100 for x in summary]
submission_rates = [x[4] / (x[1] or 1) * 100 for x in summary]

x = range(len(labels))
width = 0.25
plt.figure(figsize=(10, 5.5))
plt.bar([i - width for i in x], open_rates, width, label="Open rate")
plt.bar(x, click_rates, width, label="Click rate")
plt.bar([i + width for i in x], submission_rates, width, label="Submission rate")
plt.xticks(list(x), labels, rotation=15, ha="right")
plt.ylabel("Rate (%)")
plt.title("Local Phishing Awareness Simulation Results")
plt.ylim(0, 100)
plt.grid(axis="y", alpha=0.25)
plt.legend()
plt.tight_layout()
plt.savefig(CHARTS / "campaign_comparison.png", dpi=180)

print("Analysis complete")
print(report)
print(CHARTS / "campaign_comparison.png")
