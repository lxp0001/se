import os
import sqlite3
import sys
from pathlib import Path

import pytest
from fastapi.testclient import TestClient


BACKEND_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(BACKEND_DIR))


@pytest.fixture(scope="session")
def database_path(tmp_path_factory):
    test_database = tmp_path_factory.mktemp("api-tests") / "registrations.db"
    os.environ["DATABASE_PATH"] = str(test_database)
    return test_database


@pytest.fixture(scope="session")
def client(database_path):
    # 在设置 DATABASE_PATH 后才导入 main，确保 API 使用临时测试库。
    from main import app

    with TestClient(app) as test_client:
        yield test_client


@pytest.fixture(autouse=True)
def clear_registrations(client, database_path):
    with sqlite3.connect(database_path) as connection:
        connection.execute("DELETE FROM registrations")
    yield
