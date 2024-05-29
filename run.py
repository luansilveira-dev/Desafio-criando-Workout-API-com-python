import os


def run_api():
    return os.system("uvicorn workout_api.main:app --reload")


def open_serve_local():
    return os.system("start msedge http://127.0.0.1:8000")


def criar_migracao():
    return os.system("PYTHONPATH=$(pwd) alembic revision --autogenerate -m 'init_db'")


def rodar_migracao():
    return os.system("PYTHONPATH=$(pwd) alembic upgrade head")


if __name__ == "__main__":
    run_api()
