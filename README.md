# Isolated Phishing Awareness Simulation Lab

This project documents a strictly local cybersecurity awareness exercise built with Kali Linux, Docker Compose, GoPhish, MailHog, and Python.

## Safety scope

The lab uses only reserved `.test` addresses and a local MailHog SMTP server. No real emails, credentials, passwords, company domains, employees, malware, attachments, or external phishing infrastructure were used. Password capture remained disabled, and the only submitted value was a fixed non-sensitive training acknowledgment.

## Components

- GoPhish: local simulation and event tracking
- MailHog: fake SMTP server and local inbox
- Python/matplotlib: metrics and chart generation
- Docker Compose: isolated repeatable deployment

## Start the lab

```bash
docker compose up -d
