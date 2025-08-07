# 🏥 Hospital Management System - Project Documentation

## 📋 Table of Contents

1. [Project Overview](#project-overview)
2. [Architecture](#architecture)
3. [Database Schema](#database-schema)
4. [API Documentation](#api-documentation)
5. [Frontend Components](#frontend-components)
6. [Development Guide](#development-guide)
7. [Deployment Guide](#deployment-guide)
8. [Testing Guide](#testing-guide)

## 🎯 Project Overview

The Hospital Management System is a comprehensive web-based solution designed to streamline healthcare operations. It provides role-based access control for different user types and manages all aspects of hospital operations.

### Key Features

- **Multi-role Authentication**: Admin, Doctor, Receptionist, Patient
- **Patient Management**: Complete patient records and medical history
- **Doctor Management**: Doctor profiles, specializations, and availability
- **Appointment Scheduling**: Patient-doctor appointment booking system
- **Billing & Invoices**: Financial management and invoice generation
- **Medical Records**: Prescriptions, lab reports, and medical documents
- **Dashboard & Analytics**: Role-based dashboards with statistics
- **Notifications**: Email/SMS reminders for appointments

### User Roles & Permissions

| Role | Permissions |
|------|-------------|
| **Admin** | Full system access, user management, reports |
| **Doctor** | Patient management, appointments, medical records |
| **Receptionist** | Patient registration, appointment booking, billing |
| **Patient** | View appointments, bills, medical records |

## 🏗️ Architecture

### Technology Stack

#### Backend
- **Framework**: Django 4.2
- **Database**: PostgreSQL
- **Authentication**: JWT (JSON Web Tokens)
- **API**: Django REST Framework
- **Task Queue**: Celery + Redis
- **File Storage**: Local/Cloud storage

#### Frontend
- **Framework**: React 18
- **UI Library**: Material-UI (MUI)
- **State Management**: Redux Toolkit
- **Routing**: React Router v6
- **HTTP Client**: Axios
- **Charts**: Chart.js

#### DevOps
- **Containerization**: Docker
- **Orchestration**: Docker Compose
- **Deployment**: Heroku/AWS/Vercel

### System Architecture

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   React App     │    │   Django API    │    │   PostgreSQL    │
│   (Frontend)    │◄──►│   (Backend)     │◄──►│   (Database)    │
└─────────────────┘    └─────────────────┘    └─────────────────┘
         │                       │                       │
         │                       │                       │
         ▼                       ▼                       ▼
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Material-UI   │    │   Celery Tasks  │    │   Redis Cache   │
│   Components    │    │   (Background)  │    │   (Caching)     │
└─────────────────┘    └─────────────────┘    └─────────────────┘
```

## 🗄️ Database Schema

### Core Entities

#### User Model
```python
class User(AbstractUser):
    role = models.CharField(choices=ROLE_CHOICES)
    phone_number = models.CharField()
    address = models.TextField()
    date_of_birth = models.DateField()
    profile_picture = models.ImageField()
```

#### Patient Model
```python
class Patient(models.Model):
    user = models.OneToOneField(User)
    patient_id = models.CharField(unique=True)
    gender = models.CharField(choices=GENDER_CHOICES)
    blood_group = models.CharField(choices=BLOOD_GROUP_CHOICES)
    emergency_contact = models.CharField()
    allergies = models.TextField()
    medical_conditions = models.TextField()
```

#### Doctor Model
```python
class Doctor(models.Model):
    user = models.OneToOneField(User)
    doctor_id = models.CharField(unique=True)
    specialization = models.ForeignKey(Specialization)
    license_number = models.CharField(unique=True)
    experience_years = models.PositiveIntegerField()
    consultation_fee = models.DecimalField()
```

#### Appointment Model
```python
class Appointment(models.Model):
    patient = models.ForeignKey(Patient)
    doctor = models.ForeignKey(Doctor)
    appointment_type = models.CharField(choices=APPOINTMENT_TYPE_CHOICES)
    scheduled_date = models.DateField()
    scheduled_time = models.TimeField()
    status = models.CharField(choices=STATUS_CHOICES)
```

#### Invoice Model
```python
class Invoice(models.Model):
    patient = models.ForeignKey(Patient)
    appointment = models.ForeignKey(Appointment)
    invoice_date = models.DateField()
    subtotal = models.DecimalField()
    tax_amount = models.DecimalField()
    total_amount = models.DecimalField()
    status = models.CharField(choices=STATUS_CHOICES)
```

### Entity Relationships

```
User (1) ──── (1) Patient
User (1) ──── (1) Doctor
Patient (1) ──── (N) Appointment
Doctor (1) ──── (N) Appointment
Patient (1) ──── (N) Invoice
Appointment (1) ──── (1) Invoice
Patient (1) ──── (N) MedicalHistory
Doctor (1) ──── (N) MedicalHistory
```

## 📡 API Documentation

### Authentication Endpoints

#### POST /api/auth/login/
**Description**: User login
**Request Body**:
```json
{
  "username": "string",
  "password": "string"
}
```
**Response**:
```json
{
  "message": "Login successful",
  "user": {
    "id": 1,
    "username": "john_doe",
    "email": "john@example.com",
    "role": "patient"
  },
  "tokens": {
    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...",
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9..."
  }
}
```

#### POST /api/auth/register/
**Description**: User registration
**Request Body**:
```json
{
  "username": "string",
  "email": "string",
  "password": "string",
  "password_confirm": "string",
  "first_name": "string",
  "last_name": "string",
  "role": "patient"
}
```

#### GET /api/auth/user-info/
**Description**: Get current user information
**Headers**: `Authorization: Bearer <token>`

### Patient Endpoints

#### GET /api/patients/
**Description**: List all patients
**Query Parameters**:
- `search`: Search by name
- `page`: Page number
- `page_size`: Items per page

#### POST /api/patients/
**Description**: Create new patient
**Request Body**:
```json
{
  "user": {
    "username": "patient_username",
    "email": "patient@example.com",
    "first_name": "John",
    "last_name": "Doe"
  },
  "gender": "M",
  "blood_group": "A+",
  "emergency_contact": "+1234567890"
}
```

#### GET /api/patients/{id}/
**Description**: Get patient details

#### PUT /api/patients/{id}/
**Description**: Update patient information

### Appointment Endpoints

#### GET /api/appointments/
**Description**: List appointments
**Query Parameters**:
- `patient_id`: Filter by patient
- `doctor_id`: Filter by doctor
- `status`: Filter by status
- `date`: Filter by date

#### POST /api/appointments/
**Description**: Create appointment
**Request Body**:
```json
{
  "patient": 1,
  "doctor": 2,
  "appointment_type": "consultation",
  "scheduled_date": "2024-01-15",
  "scheduled_time": "09:00:00",
  "symptoms": "Fever and headache"
}
```

### Billing Endpoints

#### GET /api/billing/invoices/
**Description**: List invoices

#### POST /api/billing/invoices/
**Description**: Create invoice

#### GET /api/billing/invoices/{id}/download/
**Description**: Download invoice PDF

## 🎨 Frontend Components

### Component Structure

```
src/
├── components/
│   ├── Layout/
│   │   ├── Layout.js
│   │   └── Sidebar.js
│   ├── Auth/
│   │   └── PrivateRoute.js
│   ├── Common/
│   │   ├── LoadingSpinner.js
│   │   ├── ErrorBoundary.js
│   │   └── DataTable.js
│   └── Forms/
│       ├── PatientForm.js
│       ├── AppointmentForm.js
│       └── BillingForm.js
├── pages/
│   ├── Auth/
│   │   ├── Login.js
│   │   └── Register.js
│   ├── Dashboard/
│   │   └── Dashboard.js
│   ├── Patients/
│   │   └── Patients.js
│   ├── Doctors/
│   │   └── Doctors.js
│   ├── Appointments/
│   │   └── Appointments.js
│   ├── Billing/
│   │   └── Billing.js
│   └── MedicalRecords/
│       └── MedicalRecords.js
├── store/
│   ├── index.js
│   └── slices/
│       ├── authSlice.js
│       ├── patientSlice.js
│       ├── doctorSlice.js
│       ├── appointmentSlice.js
│       ├── billingSlice.js
│       └── medicalRecordSlice.js
└── services/
    ├── api.js
    ├── authService.js
    ├── patientService.js
    └── appointmentService.js
```

### Key Components

#### Layout Component
- Responsive sidebar navigation
- Role-based menu items
- User profile dropdown
- Notification system

#### Dashboard Component
- Statistics cards
- Recent appointments
- Quick actions
- Charts and analytics

#### Authentication Components
- Login form with validation
- Registration form
- Password reset functionality
- JWT token management

## 🛠️ Development Guide

### Prerequisites

1. **Python 3.8+**
2. **Node.js 16+**
3. **PostgreSQL 12+**
4. **Redis** (for Celery)
5. **Docker** (optional)

### Local Development Setup

#### 1. Clone Repository
```bash
git clone <repository-url>
cd hospital-management
```

#### 2. Backend Setup
```bash
cd backend

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp env.example .env
# Edit .env with your configuration

# Run migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Start development server
python manage.py runserver
```

#### 3. Frontend Setup
```bash
cd frontend

# Install dependencies
npm install

# Start development server
npm start
```

#### 4. Database Setup
```bash
# Install PostgreSQL
# Create database
createdb hospital_db

# Update .env with database credentials
```

### Development Workflow

#### 1. Feature Development
```bash
# Create feature branch
git checkout -b feature/patient-management

# Make changes
# Test locally

# Commit changes
git add .
git commit -m "Add patient management feature"

# Push to remote
git push origin feature/patient-management
```

#### 2. Code Quality
```bash
# Backend linting
cd backend
flake8 .
black .

# Frontend linting
cd frontend
npm run lint
npm run format
```

#### 3. Testing
```bash
# Backend tests
cd backend
python manage.py test

# Frontend tests
cd frontend
npm test
```

### Environment Variables

#### Backend (.env)
```env
# Django Settings
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# Database
DB_NAME=hospital_db
DB_USER=postgres
DB_PASSWORD=password
DB_HOST=localhost
DB_PORT=5432

# JWT Settings
JWT_SECRET_KEY=your-jwt-secret-key-here

# Email Settings
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password

# Redis Settings
REDIS_URL=redis://localhost:6379/0
```

#### Frontend (.env)
```env
REACT_APP_API_URL=http://localhost:8000/api
REACT_APP_BASE_URL=http://localhost:3000
```

## 🚀 Deployment Guide

### Docker Deployment

#### 1. Build and Run
```bash
# Build all services
docker-compose up --build

# Run in background
docker-compose up -d
```

#### 2. Production Deployment
```bash
# Use production compose file
docker-compose -f docker-compose.prod.yml up --build
```

### Manual Deployment

#### 1. Backend Deployment
```bash
# Install dependencies
pip install -r requirements.txt

# Collect static files
python manage.py collectstatic

# Run migrations
python manage.py migrate

# Start with Gunicorn
gunicorn hospital.wsgi:application --bind 0.0.0.0:8000
```

#### 2. Frontend Deployment
```bash
# Build for production
npm run build

# Serve with nginx or similar
```

### Cloud Deployment

#### Heroku
```bash
# Create Heroku app
heroku create hospital-management-app

# Add PostgreSQL addon
heroku addons:create heroku-postgresql:hobby-dev

# Deploy
git push heroku main

# Run migrations
heroku run python manage.py migrate
```

#### AWS
- Use Elastic Beanstalk for Django
- Use S3 for static files
- Use RDS for PostgreSQL
- Use ElastiCache for Redis

## 🧪 Testing Guide

### Backend Testing

#### Unit Tests
```bash
# Run all tests
python manage.py test

# Run specific app tests
python manage.py test api.patients

# Run with coverage
coverage run --source='.' manage.py test
coverage report
```

#### API Tests
```bash
# Test API endpoints
python manage.py test api.tests.test_views
```

### Frontend Testing

#### Unit Tests
```bash
# Run all tests
npm test

# Run with coverage
npm test -- --coverage

# Run specific test
npm test -- --testNamePattern="Login"
```

#### Integration Tests
```bash
# Run E2E tests
npm run test:e2e
```

### Test Structure

```
tests/
├── backend/
│   ├── test_models.py
│   ├── test_views.py
│   ├── test_serializers.py
│   └── test_api.py
└── frontend/
    ├── components/
    │   └── __tests__/
    ├── pages/
    │   └── __tests__/
    └── services/
        └── __tests__/
```

## 📊 Performance Optimization

### Backend Optimization

1. **Database Optimization**
   - Use database indexes
   - Optimize queries
   - Use select_related/prefetch_related

2. **Caching**
   - Redis caching
   - Database query caching
   - API response caching

3. **Async Tasks**
   - Use Celery for background tasks
   - Email notifications
   - Report generation

### Frontend Optimization

1. **Code Splitting**
   - Lazy loading components
   - Route-based splitting

2. **Bundle Optimization**
   - Tree shaking
   - Minification
   - Gzip compression

3. **Performance Monitoring**
   - React DevTools
   - Lighthouse audits
   - Bundle analyzer

## 🔒 Security Considerations

### Authentication & Authorization
- JWT token expiration
- Role-based access control
- Password hashing
- Session management

### Data Protection
- Input validation
- SQL injection prevention
- XSS protection
- CSRF protection

### API Security
- Rate limiting
- Request validation
- Error handling
- Logging and monitoring

## 📈 Monitoring & Logging

### Backend Monitoring
```python
# Django logging configuration
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': 'debug.log',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'INFO',
            'propagate': True,
        },
    },
}
```

### Frontend Monitoring
```javascript
// Error boundary for React
class ErrorBoundary extends React.Component {
  componentDidCatch(error, errorInfo) {
    // Log error to monitoring service
    console.error('Error:', error, errorInfo);
  }
}
```

## 🤝 Contributing

### Development Guidelines

1. **Code Style**
   - Follow PEP 8 for Python
   - Use ESLint for JavaScript
   - Write meaningful commit messages

2. **Testing**
   - Write unit tests for new features
   - Maintain test coverage > 80%
   - Test edge cases

3. **Documentation**
   - Update README.md
   - Document API changes
   - Add inline comments

### Pull Request Process

1. Fork the repository
2. Create feature branch
3. Make changes and test
4. Submit pull request
5. Code review
6. Merge to main

## 📞 Support

### Getting Help

1. **Documentation**: Check this documentation first
2. **Issues**: Create GitHub issue for bugs
3. **Discussions**: Use GitHub discussions for questions
4. **Email**: Contact maintainers for urgent issues

### Common Issues

#### Backend Issues
- Database connection errors
- Migration conflicts
- Environment variable issues

#### Frontend Issues
- Build errors
- API integration problems
- State management issues

#### Deployment Issues
- Docker container problems
- Environment configuration
- Database setup

---

**Last Updated**: January 2024
**Version**: 1.0.0
**Maintainers**: Hospital Management System Team
