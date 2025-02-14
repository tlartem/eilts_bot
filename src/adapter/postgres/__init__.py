# from src.db.db import DatabaseManager
from src.database.models import init_db 
# # Создаем экземпляр DatabaseManager
# db_manager = DatabaseManager()

# # Экспортируем только db_manager
# __all__ = ["db_manager"]
__all__ = ["init_db"]