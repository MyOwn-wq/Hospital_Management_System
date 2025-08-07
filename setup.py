#!/usr/bin/env python3
"""
Setup script for Hospital Management System
This script helps initialize the project and create necessary files.
"""

import os
import subprocess
import sys
from pathlib import Path

def run_command(command, cwd=None):
    """Run a command and return the result"""
    try:
        result = subprocess.run(
            command,
            shell=True,
            cwd=cwd,
            capture_output=True,
            text=True
        )
        return result.returncode == 0, result.stdout, result.stderr
    except Exception as e:
        return False, "", str(e)

def create_env_file():
    """Create .env file from template"""
    env_example = Path("env.example")
    env_file = Path(".env")
    
    if env_example.exists() and not env_file.exists():
        print("Creating .env file from template...")
        with open(env_example, 'r') as f:
            content = f.read()
        
        with open(env_file, 'w') as f:
            f.write(content)
        print("✅ .env file created successfully!")
    else:
        print("ℹ️  .env file already exists or template not found.")

def setup_backend():
    """Setup Django backend"""
    print("\n🔧 Setting up Django backend...")
    
    backend_dir = Path("backend")
    if not backend_dir.exists():
        print("❌ Backend directory not found!")
        return False
    
    # Install Python dependencies
    print("Installing Python dependencies...")
    success, stdout, stderr = run_command("pip install -r requirements.txt", cwd=backend_dir)
    if not success:
        print(f"❌ Failed to install dependencies: {stderr}")
        return False
    print("✅ Dependencies installed successfully!")
    
    # Run migrations
    print("Running database migrations...")
    success, stdout, stderr = run_command("python manage.py migrate", cwd=backend_dir)
    if not success:
        print(f"❌ Failed to run migrations: {stderr}")
        return False
    print("✅ Migrations completed successfully!")
    
    # Create superuser
    print("Creating superuser...")
    print("Please enter the following details for the admin user:")
    success, stdout, stderr = run_command("python manage.py createsuperuser", cwd=backend_dir)
    if not success:
        print(f"⚠️  Failed to create superuser: {stderr}")
        print("You can create one manually later with: python manage.py createsuperuser")
    
    return True

def setup_frontend():
    """Setup React frontend"""
    print("\n🔧 Setting up React frontend...")
    
    frontend_dir = Path("frontend")
    if not frontend_dir.exists():
        print("❌ Frontend directory not found!")
        return False
    
    # Install Node.js dependencies
    print("Installing Node.js dependencies...")
    success, stdout, stderr = run_command("npm install", cwd=frontend_dir)
    if not success:
        print(f"❌ Failed to install dependencies: {stderr}")
        return False
    print("✅ Dependencies installed successfully!")
    
    return True

def check_prerequisites():
    """Check if required software is installed"""
    print("🔍 Checking prerequisites...")
    
    # Check Python
    success, stdout, stderr = run_command("python --version")
    if success:
        print(f"✅ Python: {stdout.strip()}")
    else:
        print("❌ Python not found!")
        return False
    
    # Check Node.js
    success, stdout, stderr = run_command("node --version")
    if success:
        print(f"✅ Node.js: {stdout.strip()}")
    else:
        print("❌ Node.js not found!")
        return False
    
    # Check npm
    success, stdout, stderr = run_command("npm --version")
    if success:
        print(f"✅ npm: {stdout.strip()}")
    else:
        print("❌ npm not found!")
        return False
    
    # Check Docker (optional)
    success, stdout, stderr = run_command("docker --version")
    if success:
        print(f"✅ Docker: {stdout.strip()}")
    else:
        print("⚠️  Docker not found (optional for development)")
    
    return True

def main():
    """Main setup function"""
    print("🏥 Hospital Management System Setup")
    print("=" * 50)
    
    # Check prerequisites
    if not check_prerequisites():
        print("\n❌ Prerequisites not met. Please install required software.")
        sys.exit(1)
    
    # Create .env file
    create_env_file()
    
    # Setup backend
    if not setup_backend():
        print("\n❌ Backend setup failed!")
        sys.exit(1)
    
    # Setup frontend
    if not setup_frontend():
        print("\n❌ Frontend setup failed!")
        sys.exit(1)
    
    print("\n🎉 Setup completed successfully!")
    print("\n📋 Next steps:")
    print("1. Edit .env file with your configuration")
    print("2. Start the backend: cd backend && python manage.py runserver")
    print("3. Start the frontend: cd frontend && npm start")
    print("4. Or use Docker: docker-compose up --build")
    print("\n🌐 Access points:")
    print("- Frontend: http://localhost:3000")
    print("- Backend API: http://localhost:8000")
    print("- Admin Panel: http://localhost:8000/admin")

if __name__ == "__main__":
    main()
