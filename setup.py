from setuptools import setup, find_packages

setup(
    name="chiagent",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "fastapi==0.109.0",
        "uvicorn==0.27.0",
        "sqlalchemy==2.0.25",
        "psycopg2-binary==2.9.9",
        "pydantic==2.5.3",
        "python-dotenv==1.0.0",
        "pytest==7.4.4"
    ],
    python_requires=">=3.8"
)
