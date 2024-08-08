from langchain_community.agent_toolkits.sql.base import create_sql_agent
from langchain_community.utilities.sql_database import SQLDatabase
from urllib.parse import quote
import os

user = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")
database = os.getenv("DB_DATABASE")
host = os.getenv("DB_HOST")
port = os.getenv("DB_PORT")
db_type = os.getenv("DB_DB_TYPE")

connection_str = f"{db_type}://{user}:{quote(password)}@{host}:{port}/{database}"

db_conn = SQLDatabase.from_uri(connection_str)

def get_sql_agent(llm):
    sql_agent = create_sql_agent(
        llm=llm,
        db=db_conn,
        verbose=True,
        top_k=100,
        agent_executor_kwargs={"handle_parsing_error": True}
    )
    return sql_agent