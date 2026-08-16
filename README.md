# ID Generator (ProgrammerID)

A Django web app for generating printable ID cards. A user fills in a registration form —
first and last name, photo, gender, date of birth, civil status, blood type, and a personal
motto — and the app stores that record and renders it as an ID card, complete with an
auto-assigned issue date and a validity date five years out.

Despite the repo name, this isn't a UUID/nanoid-style unique-identifier library — it's a
Django CRUD app for producing employee/programmer identification cards.

## Features

- **Registration form** (`/register/`) — collects personal details and a profile photo,
  backed by a Django `ModelForm` (`main/forms.py`) with a custom date picker widget.
- **ID card view** (`/identification/`) — lists all registered records, most recent first,
  rendered as ID cards.
- **Delete** (`/identification/delete/<id>/`) — removes a record.
- **Django admin** — the `UserInfo` model is registered with the Django admin site for
  quick data management.
- **Auto-computed validity** — `date_issued` is set on creation and `validity` defaults to
  five years from issuance, computed with `python-dateutil`.

## Stack

- **Django** (project name `ProgrammerID`) with the `main` app holding models, views,
  forms, and templates
- **SQLite** (`db.sqlite3`) as the default database
- Django's `ImageField` for photo uploads, served from `MEDIA_ROOT` in debug mode

## Data model

`UserInfo` (`main/models.py`) stores: first/last name, photo, gender (M/F), date of birth,
civil status (Single/Married/Live-in/Separated/Widow-er), blood type (A/B/AB/O, +/-),
issue date, validity date, and a free-text motto.

## Setup

```bash
pip install django python-dateutil pillow
python manage.py migrate
python manage.py runserver
```

Then visit `/register/` to add a record and `/identification/` to view generated ID cards.
