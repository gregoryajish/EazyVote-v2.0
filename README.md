# EazyVote v2.0 (Vimalagiri Customization)

> **A secure, multi-post desktop election management system built for Vimalagiri Public School, Kothamangalam — Academic Session 2026–2027**

---

## Overview

**EazyVote** is a secure, fast, and visually polished voting application designed for conducting internal student council elections within educational institutions. It runs entirely on-site using local hardware, connecting to a local MySQL database to record and retrieve votes in real time. 

Version 2.0 is custom-tailored for **Vimalagiri Public School** and supports a highly scaled-up election structure. It includes a brand-new multi-page ballot system, external theme configuration, and robust kiosk lockdown controls to ensure a smooth, tamper-proof voting experience.

---

## What's New in v2.0 (Changes from Previous Version)

Compared to the previous version (deployed for St. George Public School), v2.0 brings the following upgrades:

*   🏛️ **School & Session Migration** — Migrated branding and logic for **Vimalagiri Public School, Kothamangalam** for the **2026–27 academic session**.
*   🗄️ **Database Rebranding** — Upgraded the MySQL schema to use database `vimalagiri2026` (instead of `george`).
*   📈 **Massive Candidate & Post Scale-Up** — Expanded from **2 posts** to **8 posts** (Head Boy, Head Girl, Sports Boy, Sports Girl, Arts Boy, Arts Girl, Discipline Boy, and Discipline Girl) and from **6 candidates** to **16 candidates** (2 candidates per post).
*   🗳️ **Multi-Page Ballot Navigation** — Split the ballot into **4 pages** (2 posts per page) to handle the increased number of posts. A dynamic "Next" button guides voters through screens, finishing with a "Finish" button on the final page.
*   ⚙️ **External Configuration System** — Introduced `start_screen_config.json` to configure the school name, academic year, logo/button paths, color themes, and Terms/About text without touching the source code.
*   🛠️ **In-App Branding Editor** — Right-clicking the splash screen launches a secure admin form to modify branding details and swap image assets on the fly.
*   🔒 **Kiosk Lockdown & Access Control** — 
    *   Locks the voter interface in fullscreen kiosk mode (`-fullscreen True`) and overrides close events.
    *   The "Quit" button is disabled by default on completion; administrators can press `u` or `U` to silently unlock it.
    *   To safely terminate the app, administrators can use the shortcut `<Control-Shift-Q>` (or `<Control-Shift-q>`) and enter the secure PIN (`9744`).
*   🔌 **Connection Resilience** — Automatically checks and pings the database connection before query execution, reconnecting on the fly if needed.
*   📂 **Project Reorganization** — Renamed the main ballot app to `vimalagiri.py` (with spec `vimalagiri.spec`), cleaned up redundant legacy background files (removed `table.jpg`), and added Photoshop project config files (`.psxprj`).

---

## Features

- 🗳️ **Interactive Multi-Page Ballot** — A sleek, distraction-free photo ballot. Voters select one candidate per post across 4 pages.
- 📊 **Real-Time Results Viewer** — An admin dashboard that pulls live Tallies from the MySQL database and presents them in a structured table.
- 🔒 **One-Vote-Per-Post Enforcement** — Clickable photo-buttons are immediately disabled after a vote is cast to prevent double voting.
- 🗄️ **Local MySQL Storage** — All votes are persisted in real time in a local database with automatic connection-loss recovery.
- 📋 **CSV Results Export** — Generates a timestamped `results.csv` automatically whenever results are requested.
- 🎨 **Fully Customizable Themes** — Customize backgrounds, accents, logos, and terms via the configuration menu.
- ⚙️ **Quick Reset & Setup** — Scripts to initialize tables (`sqltable.py`) or reset vote tallies to zero (`reset.py`) in one click.

---

## Project Structure

```
Vimalagiri 2026-27/
│
├── vimalagiri.py           # Main voting kiosk application (Vimalagiri UI)
├── result.py               # Results viewer & CSV generator (Admin utility)
├── sqltable.py             # Database initializer (Creates tables & seeds candidates)
├── reset.py                # Database reset utility (Clears votes, keeps candidates)
│
├── Candidates/             # Candidate profile pictures
│   ├── candidate1.jpg      # Lious Basil Joshy
│   ├── candidate2.jpg      # Daniel Saji
│   ├── candidate3.jpg      # Meera P V
│   ├── ...                 
│   ├── candidate16.jpg     # Dilsha Nasrin
│   └── cover.jpg           # Fallback/default image
│
├── Photoshop Config Files/ # Design source projects (.psxprj)
│   ├── resstrtscrn.psxprj  
│   ├── startscreen.psxprj  
│   └── table.psxprj        
│
├── Fonts/                  # Custom application fonts
├── Legal/                  # Product documentation and license agreements
├── Deployement/            # Built executable installers & resources
├── build/                  # PyInstaller build artifacts
├── dist/                   # Compiled standalone executables (.exe)
│
├── start_screen_config.json# Dynamic splash screen configuration
├── continuebtn.jpg         # "Continue" button image asset
├── finishbtn.jpg           # "Finish" button image asset
├── nextbtn.jpg             # "Next" button image asset
├── quitbtn.jpg             # "Quit" button image asset
├── generbtn.jpg            # "Generate Results" button image asset
├── startscreen.jpg         # Voting app splash screen background
├── resstrtscrn.jpg         # Results viewer splash screen background
├── logo.ico                # Application launcher icon
├── vimalagirilogo.png      # High-res Vimalagiri School Logo
├── vimalagirilogo.jpeg     # Fallback Vimalagiri School Logo
├── results.csv             # Auto-generated CSV reports
└── data.dat                # App data file
```

---

## Candidates List

| Serial No. | Name                 | Class | Post             |
|:----------:|----------------------|:-----:|------------------|
| **1**      | Lious Basil Joshy    | XII A | Head Boy         |
| **2**      | Daniel Saji          | XI A  | Head Boy         |
| **3**      | Meera P V            | XII C | Head Girl        |
| **4**      | Aida Jojo            | XI B  | Head Girl        |
| **5**      | Noha Binil           | XII A | Sports Boy       |
| **6**      | Abhinav Krishna P    | XI A  | Sports Boy       |
| **7**      | Abhinaya Suresh      | XII B | Sports Girl      |
| **8**      | Delna Mariya Jaison  | XI B  | Sports Girl      |
| **9**      | Naveen T.S           | XII A | Arts Boy         |
| **10**     | Chris Ullas          | XI B  | Arts Boy         |
| **11**     | Krishnanandha P.S    | XII B | Arts Girl        |
| **12**     | Aagna Maria Sabu     | XI B  | Arts Girl        |
| **13**     | Adith Anuraj         | XII A | Discipline Boy   |
| **14**     | Geevarghese Basil    | XI A  | Discipline Boy   |
| **15**     | Annmaria Ashly       | XII B | Discipline Girl  |
| **16**     | Dilsha Nasrin        | XI B  | Discipline Girl  |

---

## Tech Stack

| Component      | Technology                                    |
|----------------|-----------------------------------------------|
| Language       | Python 3                                      |
| GUI Framework  | Tkinter (with custom ttk extensions)          |
| Image Handling | Pillow (PIL)                                  |
| Database       | MySQL Server (via `mysql-connector-python`)   |
| Configuration  | JSON (`start_screen_config.json`)             |
| Packaging      | PyInstaller (`.spec` specs + standalone `.exe`)|

---

## Prerequisites

Before running the scripts from source, ensure you have the following installed:

- **Python 3.8+**
- **MySQL Server** (running locally on `localhost`, port `3306`)
- Required Python modules:
  ```bash
  pip install mysql-connector-python Pillow
  ```

> ⚙️ **Default MySQL Credentials:** `user=root`, `password=1234`, `host=localhost`
> If your MySQL password or host differs, adjust it on the connection lines in `vimalagiri.py`, `result.py`, `sqltable.py`, and `reset.py`.

---

## Setup & Usage

### Step 1 — Initialize the Database
Run this **once** on the machine to spin up the schema, set up candidate tables, and reset voter counts:
```bash
python sqltable.py
```

### Step 2 — Run the Voting Kiosk
Start the main voter-facing kiosk terminal:
```bash
python vimalagiri.py
```
- Click **Continue** to proceed (Right-click to modify settings).
- Cast votes across the 4 election pages.
- On the confirmation screen, the **Quit** button is locked. Admin must press `u` or `U` on the keyboard to unlock it, allowing a click to loop back to the splash screen.
- Press `<Control-Shift-Q>` (or `<Control-Shift-q>`) and enter PIN `9744` to exit the application.

### Step 3 — View Results (Admin Only)
Run the results generator to count and tabulate the live poll results:
```bash
python result.py
```
- Click **Generate Results** to pull tallies.
- Results are simultaneously saved to `results.csv`.

### Step 4 — Reset Votes (Optional)
To clear counts for testing or starting a fresh session:
```bash
python reset.py
```
> ⚠️ This resets all candidate votes back to `0` without dropping candidate rows.

---

## Building Executables (PyInstaller)

To recompile the standalone `.exe` files for distribution, run:

```bash
pyinstaller vimalagiri.spec
pyinstaller result.spec
```
The compiled binaries will be outputted to the `dist/` directory.

---

## Window Resolution

The interface is optimized for **1366×768** screen displays. Running on lower/higher resolutions may shift layout alignments.

---

## Legal & License

- © 2026 EazyVote. All rights reserved.
- Developed by **Gregory Ajish** and **Lestlin Robins**.
- Unauthorized replication, modification, or distribution is prohibited.
- See the `Legal/` folder for full terms and agreements.

*Last updated: July 2026 — EazyVote v2.0*
