# Lawyer-Client Portal MVP Requirements

## System Overview
A basic Django-based platform connecting lawyers and clients with essential features for case management and payments.

## Current App Structure 
├── app
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
├── core
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── db.sqlite3
├── filestruct.txt
└── manage.py

## MVP Features

### 1. Authentication
- Use Django's built-in authentication
- Two user types: Lawyer and Client (using a simple boolean field)
- Basic login/register pages

### 2. Basic Models

#### User (Django's built-in User model + Profile)
- is_lawyer boolean field
- phone_number
- address

#### Case
- client (ForeignKey to User)
- lawyer (ForeignKey to User)
- title
- description
- status (New, Pending Payment, Active, Closed)
- payment_status (Pending, Completed)
- created_at

#### Payment
- case (ForeignKey to Case)
- amount
- is_paid
- payment_date

### 3. Simple Views/Pages

#### Client Pages
1. Registration/Login
2. Submit Case Form
3. My Cases List
4. Simple Payment Form
5. Case Detail View

#### Lawyer Pages
1. Registration/Login
2. Cases List
3. Case Detail View with status update
4. Simple PDF generation for court draft( with use of any LLM api)

### 4. Implementation Steps

1. Setup Models
   - Add models to models.py
   - Create migrations
   - Register in admin.py

2. Create Basic Templates
   - Base template
   - Login/Register forms
   - Case submission form
   - Case list views
   - Case detail views

3. Implement Views
   - Authentication views
   - Case CRUD operations
   - Simple payment form
   - PDF generation using reportlab

4. Add URLs
   - Authentication URLs
   - Case management URLs
   - Payment URLs

### 5. Simplified Flow
1. Client registers/logs in
2. Client submits case details
3. Client makes payment (simple form, no gateway integration)
4. Lawyer sees paid cases
5. Lawyer can generate basic PDF draft
6. Lawyer can update case status

### 6. Tech Stack
- Django (with built-in features)
- SQLite (default database)
- Crispy Forms for forms
- ReportLab for PDF generation
- Bootstrap for basic styling

### 7. Security
- Django's built-in security features
- Basic permission checks
- Login required decorators

This MVP focuses on core functionality without complex features, making it quick to implement while maintaining essential requirements.