#!/bin/bash

# Database Setup Script

set -e

echo "🗄️  Setting up PostgreSQL database..."

# Load environment variables
if [ -f .env ]; then
    export $(cat .env | grep -v '^#' | xargs)
fi

# Database credentials
DB_USER=${DB_USER:-hairai_user}
DB_PASSWORD=${DB_PASSWORD:-hairai_password}
DB_NAME=${DB_NAME:-hair_ai_db}
DB_HOST=${DB_HOST:-localhost}
DB_PORT=${DB_PORT:-5432}

echo "Creating database..."

# Create database
PGPASSWORD=${DB_PASSWORD} psql -h ${DB_HOST} -U postgres -c "CREATE DATABASE ${DB_NAME};" || true

# Create user
PGPASSWORD=${DB_PASSWORD} psql -h ${DB_HOST} -U postgres -c "CREATE USER ${DB_USER} WITH PASSWORD '${DB_PASSWORD}';" || true

# Grant privileges
PGPASSWORD=${DB_PASSWORD} psql -h ${DB_HOST} -U postgres -c "GRANT ALL PRIVILEGES ON DATABASE ${DB_NAME} TO ${DB_USER};"

echo "✅ Database setup completed!"
echo ""
echo "Database Details:"
echo "Host: ${DB_HOST}"
echo "Port: ${DB_PORT}"
echo "Database: ${DB_NAME}"
echo "User: ${DB_USER}"
