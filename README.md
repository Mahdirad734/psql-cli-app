# psql-cli-app

**psql-cli-app** is a Python-based command-line interface (CLI) tool designed for generating, inserting, and querying **large-scale, realistic sample data** in a **PostgreSQL** database.  
The application uses **batch processing** to efficiently handle bulk inserts and is well-suited for development, testing, and performance benchmarking.

---

## Features

- Generate large volumes of realistic fake user data
- High-performance batch inserts using configurable batch size
- Simple and intuitive CLI commands:
  - `generate` – create and insert data into PostgreSQL
  - `list` – display a list of stored users
  - `find` – retrieve a user by email
- Automatic database connection management
- Automatic table and index creation (no manual migrations required)
- Safe logging and graceful error handling
- Designed for scalability and large datasets

---

## Requirements

- Python 3.8 or higher
- PostgreSQL (local or remote)
- pip (or any Python dependency manager)

---

## Installation & Setup 

### Clone the repository
```bash
git clone https://github.com/<USERNAME>/psql-cli-app.git
cd psql-cli-app/

2. Create and activate a virtual environment
python -m venv .venv
source .venv/bin/activate     # Linux / macOS
# Windows:
 .venv\Scripts\activate

3. Install dependencies
python -m pip install -r requirements.txt

```
---

## psql-app command

usage: spql-app.py [-h] {generate,list,find} ...

Simple PSQL CLI app

commands:
  generate   Generate fake data
  list       List customers
  find       Find user by emaildd


# example 
```bash
psql-app.py generate --total 5000 --batch 2000

psql-app.py list --limit 50 

psql-app.py find --email mahdi_rad@gmail.com

```



