# src/paths.py
from pathlib import Path

# Определяем корень проекта
ROOT_DIR = Path(__file__).resolve().parent.parent  # Корень проекта (на уровень выше src)

# Основные директории
SRC_DIR = ROOT_DIR / "src"
LOGS_DIR = SRC_DIR / "logs"
MIGRATIONS_DIR = ROOT_DIR / "migrations"
TESTS_DIR = ROOT_DIR / "tests"

# Пути к файлам
LOG_FILE = LOGS_DIR / "app.log"
CONFIG_FILE = ROOT_DIR / "config.yaml"
DOCKER_COMPOSE_FILE = ROOT_DIR / "docker-compose.yaml"

# Убедитесь, что все нужные директории существуют
LOGS_DIR.mkdir(parents=True, exist_ok=True)
