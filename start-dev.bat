@echo off
echo 🏥 Starting Hospital Management System (Development Mode)
echo ==================================================

REM Check if Docker is running
docker info >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Docker is not running. Please start Docker first.
    pause
    exit /b 1
)

REM Stop any existing containers
echo 🛑 Stopping existing containers...
docker-compose -f docker-compose.dev.yml down

REM Build and start services
echo 🔨 Building and starting services...
docker-compose -f docker-compose.dev.yml up --build -d

REM Wait for services to be ready
echo ⏳ Waiting for services to be ready...
timeout /t 10 /nobreak >nul

REM Show service status
echo 📊 Service Status:
docker-compose -f docker-compose.dev.yml ps

echo.
echo ✅ Services are starting up!
echo.
echo 🌐 Access Points:
echo    Frontend: http://localhost:3001
echo    Backend API: http://localhost:8000
echo    Admin Panel: http://localhost:8000/admin
echo    API Documentation: http://localhost:8000
echo.
echo 📝 To view logs: docker-compose -f docker-compose.dev.yml logs -f
echo 🛑 To stop: docker-compose -f docker-compose.dev.yml down
pause
