# KidGuard — Digital Device Control System for Parents

> **4COM2006 / 4COM2011 — Team Software Project**  
> University of Hertfordshire | 2026

---

## Project Overview

**KidGuard** is a web-based parental control dashboard that allows parents to monitor, manage, and restrict their children's digital device usage in real time.

Built as a full-stack prototype using **Python**, **Flask**, **SQLite**, and **HTML/CSS**, KidGuard demonstrates a complete end-to-end system covering database design, backend API development, and a clean interactive frontend.

---

## Team

| Member | Role |
|---|---|
| Team Member 1 | Project Lead & Backend Developer |
| Team Member 2 | UI/UX Designer & Frontend Developer |

---

## Features

| Feature | Description |
|---|---|
| **Parent Dashboard** | Real-time overview of children and device screen time usage |
| **Time Limits** | Set daily screen time limits per device |
| **School Mode** | Block entertainment apps during school hours (9AM–3PM) |
| **Device Locking** | Instantly lock/unlock any child's device |
| **Usage Reports** | Aggregated app usage reports with excessive usage alerts |
| **Live Location** | GPS-based location tracking module |
| **Website Blocklist** | Add/remove blocked websites stored in the database |
| **Settings** | Account details and notification preferences |

---

## Tech Stack

| Layer | Technology |
|---|---|
| **Backend** | Python 3.12, Flask 3.0 |
| **Database** | SQLite (via Python's `sqlite3` module) |
| **Frontend** | HTML5, CSS3 (Vanilla), Jinja2 Templates |
| **Icons** | Font Awesome 6.4 |
| **Fonts** | Google Fonts — Inter |
| **Map** | OpenStreetMap Embed |

---

## Database Schema

```
child          → id, name, age, avatar
device         → id, child_id, name, type, screen_time_limit, school_mode, is_locked
activity       → id, device_id, app_name, duration, date
blocked_site   → id, url
```

---

## Prerequisites & Requirements

Before running the application, ensure you have the following installed on your system:
- **Python 3.8+** (We recommend Python 3.12)
- **pip** (Python package installer)

You also need to install the project dependencies listed in `requirements.txt`:
- `Flask==3.0.3`

---

## How to Run

### Option 1 — Windows (Easy)
1. Double-click **`run_kidguard.bat`**
2. Open your browser and go to: `http://localhost:5000`

### Option 2 — Terminal
```bash
# Install dependencies
pip install -r requirements.txt

# Run the server
python app.py
```
Then open `http://localhost:5000` in your browser.

> **Note:** The SQLite database (`kidguard.db`) is automatically created and seeded with mock data on first run.

---

## Project Structure

```
KidGuard/
│
├── app.py                  # Flask backend — all routes and logic
├── schema.sql              # SQLite database schema and seed data
├── requirements.txt        # Python dependencies
├── run_kidguard.bat        # One-click Windows launcher
├── HOW_TO_RUN.txt          # Plain-text setup instructions
│
├── static/
│   └── style.css           # Global CSS styles
│
└── templates/
    ├── layout.html         # Base HTML layout with navigation
    ├── dashboard.html      # Parent Dashboard page
    ├── time_limits.html    # Time Limits & School Mode page
    ├── reports.html        # Usage Reports page
    ├── location.html       # Live GPS Location page
    └── settings.html       # Settings & Website Blocklist page
```

---

## Security Considerations

- All SQL queries use **parameterised statements** to prevent SQL injection
- All child and device data is stored **locally** — no external cloud transmission
- Designed in compliance with **GDPR data minimisation** principles

---

## References

1. Anderson, M. & Jiang, J. (2023). *Teens, Social Media and Technology*. Pew Research Center.
2. Common Sense Media. (2022). *The Common Sense Census: Media Use by Tweens and Teens*.
3. Google. (2024). *Google Family Link*. families.google.com
4. Qustodio. (2024). *Annual Kids & Screens Report*. qustodio.com
5. Radesky, J. et al. (2023). *Defining Digital Wellness in Childhood and Adolescence*. Pediatrics, 151(2).
6. Nielsen Norman Group. (2022). *UX Design Principles for Family and Parental Control Apps*.

---

## Licence

This project was developed as part of a University of Hertfordshire academic submission. All rights reserved.
