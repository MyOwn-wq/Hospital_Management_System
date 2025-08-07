# 🏥 Hospital Management System

A comprehensive web-based system for managing patient records, doctor schedules, appointments, billing, and medical records.

## 🎯 Features

### Core Modules
- **User Authentication**: Multi-role login system (Admin, Doctors, Receptionists, Patients)
- **Patient Management**: Complete patient records, medical history, and reports
- **Doctor Management**: Doctor profiles, specialties, and availability management
- **Appointment Booking**: Schedule and manage patient-doctor appointments
- **Billing & Invoices**: Generate bills for services (OPD, tests, medicines)
- **Medical Records**: Upload and manage prescriptions, diagnosis, lab reports
- **Dashboard & Reports**: Role-based dashboards with analytics
- **Notifications**: Appointment reminders and system notifications

### User Roles
- **Admin**: Full system access, user management, reports
- **Doctor**: Patient management, appointment scheduling, medical records
- **Receptionist**: Patient registration, appointment booking, billing
- **Patient**: View appointments, bills, medical records

## 🛠️ Tech Stack

### Backend
- **Framework**: Django 4.2
- **Database**: PostgreSQL
- **Authentication**: Django REST Framework + JWT
- **API**: Django REST Framework
- **Task Queue**: Celery (for notifications)

### Frontend
- **Framework**: React 18
- **UI Library**: Material-UI (MUI)
- **State Management**: Redux Toolkit
- **Routing**: React Router
- **Charts**: Chart.js

### DevOps
- **Containerization**: Docker
- **Deployment**: Docker Compose
- **Environment**: Development/Production configs

## 📁 Project Structure

```
hospital-management/
├── backend/
│   ├── manage.py
│   ├── hospital/          # Django project settings
│   ├── api/              # Django apps
│   │   ├── authentication/
│   │   ├── patients/
│   │   ├── doctors/
│   │   ├── appointments/
│   │   ├── billing/
│   │   └── medical_records/
│   ├── requirements.txt
│   └── Dockerfile
├── frontend/
│   ├── public/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── store/
│   │   ├── services/
│   │   └── utils/
│   ├── package.json
│   └── Dockerfile
├── docker-compose.yml
├── .env.example
└── README.md
```

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Node.js 16+
- Docker & Docker Compose
- PostgreSQL

### Development Setup

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd hospital-management
   ```

2. **Environment Setup**
   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

3. **Using Docker (Recommended)**
   ```bash
   docker-compose up --build
   ```

4. **Manual Setup**

   **Backend:**
   ```bash
   cd backend
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   python manage.py migrate
   python manage.py createsuperuser
   python manage.py runserver
   ```

   **Frontend:**
   ```bash
   cd frontend
   npm install
   npm start
   ```

## 🌐 Access Points

- **Frontend**: http://localhost:3000
- **Backend API**: http://localhost:8000
- **Admin Panel**: http://localhost:8000/admin

## 📊 Database Schema

### Core Entities
- **User**: Base user model with role-based permissions
- **Patient**: Patient information and medical history
- **Doctor**: Doctor profiles and specializations
- **Appointment**: Patient-doctor appointments
- **Billing**: Financial transactions and invoices
- **MedicalRecord**: Prescriptions, reports, and documents

## 🔐 Authentication

The system uses JWT-based authentication with role-based access control:

- **Admin**: Full system access
- **Doctor**: Patient and appointment management
- **Receptionist**: Patient registration and scheduling
- **Patient**: Personal records and appointments

## 📱 API Endpoints

### Authentication
- `POST /api/auth/login/` - User login
- `POST /api/auth/register/` - User registration
- `POST /api/auth/logout/` - User logout

### Patients
- `GET /api/patients/` - List patients
- `POST /api/patients/` - Create patient
- `GET /api/patients/{id}/` - Get patient details
- `PUT /api/patients/{id}/` - Update patient

### Appointments
- `GET /api/appointments/` - List appointments
- `POST /api/appointments/` - Create appointment
- `PUT /api/appointments/{id}/` - Update appointment

### Billing
- `GET /api/billing/` - List bills
- `POST /api/billing/` - Create bill
- `GET /api/billing/{id}/invoice/` - Download invoice

## 🧪 Testing

```bash
# Backend tests
cd backend
python manage.py test

# Frontend tests
cd frontend
npm test
```

## 📦 Deployment

### Production Deployment
```bash
docker-compose -f docker-compose.prod.yml up --build
```

### Environment Variables
- `SECRET_KEY`: Django secret key
- `DEBUG`: Debug mode (False for production)
- `DATABASE_URL`: PostgreSQL connection string
- `ALLOWED_HOSTS`: Allowed host domains
- `CORS_ALLOWED_ORIGINS`: Frontend domain

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License.

## 📞 Support

For support and questions, please open an issue in the repository.

---

**Built with ❤️ for better healthcare management**
