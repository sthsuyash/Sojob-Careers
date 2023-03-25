from sqlalchemy import create_engine, text
from dotenv import load_dotenv

load_dotenv()
import os

db_connection_string = f"mysql+pymysql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}/{os.getenv('DB_NAME')}?charset=utf8mb4"

engine = create_engine(
    db_connection_string,
    connect_args={
        "ssl": {
            "ssl_ca": "/etc/ssl/cert.pem"
        }
    })


def load_jobs_from_db():
    with engine.connect() as con:
        result = con.execute(text("SELECT * FROM jobs"))
        # for each_job in result:
        #     print(f"\n\nJob id: {each_job[0]}")
        #     print(f"Name: {each_job[1]}\nLocation: {each_job[2]}\nSalary: {each_job[4]}.{each_job[3]}\nDescription: {each_job[5]}\nRequirements: {each_job[6]}")

        jobs = []
        for row in result.all():
            jobs.append(dict(zip(result.keys(), row)))
        return jobs

        # first_result = result.fetchone()
        # if first_result:
        #     first_result_dict = dict(zip(result.keys(), first_result))

        # print(first_result_dict['title'])


def load_job_from_db(id):
    with engine.connect() as con:
        result = con.execute(text(f"SELECT * FROM jobs WHERE id = {id}"))
        job = result.fetchone()
        if job:
            job = dict(zip(result.keys(), job))
        return job
