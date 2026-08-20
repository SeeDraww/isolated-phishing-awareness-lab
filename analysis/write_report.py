from pathlib import Path
import csv

root = Path(__file__).resolve().parents[1]
rows = list(csv.DictReader((root / "data" / "summary.csv").open(encoding="utf-8-sig")))

def n(row, key):
    return row.get(key, "0")

lines = [
    "# Human-Risk Assessment Report",
    "",
    "> This report documents a strictly local, harmless phishing-awareness simulation. No real organization, employee, credential, password, or external recipient was used.",
    "",
    "## 1. Executive Summary",
    "",
    "Three controlled campaigns were conducted using GoPhish and MailHog inside a Docker network. The exercise measured message delivery, opens, clicks, and one fixed non-sensitive acknowledgment submission. Results are indicative of interaction with the test recipient only and must not be generalized to a wider population.",
    "",
    "## 2. Methodology",
    "",
    "GoPhish delivered simulated messages to the local MailHog SMTP server. All recipients used the reserved `.test` domain. The scenarios used harmless awareness wording, no attachments, no external URLs, and no password or credential fields. Events were exported as CSV and analyzed with Python.",
    "",
    "## 3. Results",
    "",
    "| Scenario | Emails sent | Opens | Clicks | Submissions | Open rate | Click rate | Submission rate |",
    "|---|---:|---:|---:|---:|---:|---:|---:|",
]
for r in rows:
    lines.append(f"| {r['scenario']} | {n(r,'emails_sent')} | {n(r,'opens')} | {n(r,'clicks')} | {n(r,'submissions')} | {n(r,'open_rate')}% | {n(r,'click_rate')}% | {n(r,'submission_rate')}% |")

lines += [
    "",
    "![Campaign comparison](../charts/campaign_comparison.png)",
    "",
    "## 4. Risk Interpretation",
    "",
    "The observed events demonstrate that message delivery alone does not establish user awareness. Opens and clicks indicate interaction with simulated content, while the acknowledgment event demonstrates that a user can complete a non-sensitive workflow. Because the sample consisted of a controlled test recipient, the results are a technical demonstration rather than a statistically valid organizational risk score.",
    "",
    "## 5. Recommendations",
    "",
    "Organizations should provide recurring security-awareness training, encourage reporting of suspicious messages, verify unexpected requests through trusted channels, use protective email controls, and measure improvement over time with authorized simulations. Future exercises should use larger approved samples and documented consent or organizational authorization.",
    "",
    "## 6. Safety and Scope Appendix",
    "",
    "- Execution remained inside a local Kali Linux virtual machine and Docker network.",
    "- MailHog intercepted the SMTP traffic; no real email delivery was intended.",
    "- Only `.test` addresses controlled by the student were used.",
    "- No real company domains, branding, employees, credentials, passwords, malware, or attachments were used.",
    "- Password capture remained disabled.",
    "- The only submitted value was a fixed, non-sensitive training acknowledgment.",
    "- Raw results must be reviewed before publication to ensure no private information remains.",
]
(root / "report" / "human_risk_assessment.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
print(root / "report" / "human_risk_assessment.md")
