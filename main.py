import streamlit as st
import os
import sqlite3
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

from dotenv import load_dotenv
load_dotenv()

def get_sql_gurey(text):
    prompt = ChatPromptTemplate.from_template("""
                    You are an expert in converting English questions to SQL query!
                    The SQL database has the name STUDENTS and has the following columns - NAME, COURSE, 
                    SECTION and MARKS. For example, 
                    Example 1 - How many entries of records are present?, 
                        the SQL command will be something like this SELECT COUNT(*) FROM STUDENTS;
                    Example 2 - Tell me all the STUDENTS studying in Data Science COURSE?, 
                        the SQL command will be something like this SELECT * FROM STUDENTS 
                        where COURSE="Data Science"; 
                    also the sql code should not have ``` in beginning or end and sql word in output.
                    Now convert the following question in English to a valid SQL Query: {text}. 
                    No preamble, only valid SQL please
                    """)

    model = "llama-3.1-8b-instant"
    llm = ChatGroq(
        model = model,
        groq_api_key = os.getenv("GROQ_API_KEY"),
    )

    chain = prompt | llm | StrOutputParser()
    response = chain.invoke(input={"text":text})
    return response

def table_data(sql_query):
    database = "STUDENTS.db"
    with sqlite3.connect(database) as conn:
        return conn.execute(sql_query).fetchall()

def main():
    header = st.header("Text to SQL, Data Analyst Role by AI-Agent")

    if header:
        text = st.text_input("Data You want to get:")
        submit = st.button("Submit")
        if submit:
            sql_query = get_sql_gurey(text)
            retrieved_table_rows = table_data(sql_query)
            st.subheader(f"Retrieving results from the database for the query: [{sql_query}]")
            for row in retrieved_table_rows:
                st.header(row)
            
if __name__ == '__main__':
    main()