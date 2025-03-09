# Email Slicer Project

## Overview
This project is a Django-based web application that extracts and displays different parts of an email address. Users can enter an email, and the system will return the username and domain separately.

## Features
- Accepts user input via a web interface.
- Parses email addresses to extract the username and domain.
- Displays results in a structured format.
- Utilizes Django's built-in templating and static file management.

## Technologies Used
- **Backend:** Django
- **Frontend:** HTML, CSS
- **Database:** SQLite

## Installation

### Prerequisites
Ensure you have Python installed. You can check by running:
```bash
python --version
```

### Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/deephabiswashi/email-slicer-django.git
   cd email-slicer
   ```
2. Create and activate a virtual environment:
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows use: env\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Apply migrations:
   ```bash
   python manage.py migrate
   ```
5. Run the development server:
   ```bash
   python manage.py runserver
   ```
6. Open your browser and visit `http://127.0.0.1:8000/`.

## Project Structure
```
email_slicer_project/
│── slicer/
│   ├── migrations/
│   ├── static/slicer/css/style.css
│   ├── templates/slicer/index.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
│── staticfiles/
│── db.sqlite3
│── manage.py
│── requirements.txt
```

## Contributing
Feel free to fork this repository and submit pull requests. Any improvements or feature suggestions are welcome!

## License
This project is licensed under the MIT License.
