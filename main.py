# Start connection with database PostgreSql
from config.settings import connection_db
DB = connection_db()

# Start application with Gunicorn
from adapters.interfaces.api.views import app

# Create user admin for exemplo
from application.user import UserSerializer
UserSerializer(username="admin", password="admin123").save()