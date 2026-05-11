#!/bin/bash

# Health Check Script

echo "🔍 Checking Hair AI System health..."

# Check backend
echo "Checking backend..."
curl -s -f http://localhost:8000/health > /dev/null && echo "✓ Backend: OK" || echo "✗ Backend: FAILED"

# Check database
echo "Checking database..."
psql -h localhost -U hairai_user -d hair_ai_db -c "SELECT 1;" > /dev/null 2>&1 && echo "✓ Database: OK" || echo "✗ Database: FAILED"

# Check frontend
echo "Checking frontend..."
curl -s -f http://localhost:3000 > /dev/null && echo "✓ Frontend: OK" || echo "✗ Frontend: FAILED"

echo ""
echo "✅ Health check completed!"
