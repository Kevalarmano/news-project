# News Project

## Setup Instructions

### Clone
git clone <your-repo-link>
cd news-project

### Install dependencies
pip install -r requirements.txt

### Run server
python manage.py runserver

---

## Docker
docker build -t news-project .
docker run -p 8000:8000 news-project

---

## Documentation
Open:
docs/build/html/index.html

---

## Notes
- Run all commands from root folder
- Do NOT enter nested folders
