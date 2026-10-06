# Weekora

**Make room for a weekend.**

A learning starter for a marketplace where independent organisers post weekend trips and travellers discover them. Weekora is a working project name; domain and trademark availability have not been checked.

## Start here

Open this folder in your editor or Claude Code. In a terminal inside this folder:

```sh
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python app.py
```

Visit http://127.0.0.1:5001. Stop the server with Ctrl+C. On subsequent runs, activate the environment and run `python app.py` again. The development server is for local learning.

## What you have

This matches the scope and structure of your supplied expense-tracker starter: Python, Flask, Jinja templates, plain CSS and JavaScript, with a SQLite setup file left for you to implement.

- A travel landing page with an illustrative trip card.
- Sign-in and registration screens, including a traveller/organiser choice.
- Friendly placeholder pages for browsing, viewing, adding, editing and removing trips, plus profile and logout.
- No account storage, database implementation, real listings, search, bookings or payments yet. Form submissions explain that nothing is saved.

```text
weekora/
  app.py
  requirements.txt
  database/
    __init__.py
    db.py
  templates/
    base.html
    landing.html
    login.html
    register.html
    coming_soon.html
  static/
    css/style.css
    js/main.js
```

## Translate the course project into your project

These are suggested adaptations, not claims about the exact contents or order of the videos.

| When the expense tracker builds… | Build this in Weekora… |
| --- | --- |
| Database tables | Users and trips, linked by organiser ID |
| Registration and login | Traveller and organiser accounts |
| Profile | Traveller profile or organiser business details |
| Add expense | Organiser creates a trip |
| Expense list | Browse published weekend trips |
| Edit expense | Organiser edits their own trip |
| Delete expense | Organiser removes their own trip with confirmation |
| Category/date filters | Destination, departure city, date and price filters |
| Spending summary | Organiser summary: trips posted and enquiries received |

## Use the playlist to learn the tools

Based on the video titles you provided:

- Setup and slash commands: open this folder and ask Claude Code to explain the files.
- Code changes and image context: refine the homepage using your own travel design references.
- Context management: keep one feature per task and summarise completed work.
- CLAUDE.md: write your own project instructions during that lesson. It is intentionally not prewritten here.
- Specs and plan mode: specify trip creation and plan its implementation before coding.
- Custom commands and skills: practise repeatable tasks such as reviewing a trip form.
- Subagents: try separate database, interface and review tasks when the course introduces them.
- MCP, hooks and plugins: add them when you reach those lessons and have a concrete use for them.

A first prompt to use:

> I am following the CampusX Claude Code playlist but building Weekora, a weekend-trip marketplace. Explain this starter and compare it with an expense-tracker app. Do not implement the remaining features yet. Help me complete one lesson at a time.

## Later product direction

First make the local create/list/edit/delete flow work. Then add itinerary details and traveller enquiries. Before inviting real organisers, add ownership checks, server-side validation, CSRF protection, secure authentication and listing moderation. Bookings, capacity, cancellation policies and payments are later milestones.

Design references: https://wondrr.in/ and https://pickyourtrail.com/. No branding, customer reviews or real organiser listings have been copied. All displayed trip details are illustrative.
