# Text to SQL - AI-Powered Data Analyst 🤖

An intelligent Streamlit application that converts natural language questions into SQL queries and retrieves data from a student database using AI.

## 🌟 Features

- **Natural Language Processing**: Ask questions in plain English
- **Automatic SQL Generation**: AI converts your questions to valid SQL queries
- **Real-time Results**: Instant data retrieval from SQLite database
- **User-Friendly Interface**: Simple and intuitive Streamlit UI
- **LangChain Integration**: Powered by LangChain and Groq LLM

## 📋 Prerequisites

- Python 3.8 or higher
- Groq API Key

## 🚀 Installation

1. **Clone the repository**
```bash
git clone <your-repository-url>
cd <repository-name>
```

2. **Create a virtual environment** (recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install required packages**
```bash
pip install -r requirements.txt
```

4. **Set up environment variables**

Create a `.env` file in the root directory:
```env
GROQ_API_KEY=your_groq_api_key_here
```

## 📦 Dependencies

Create a `requirements.txt` file with:
```
streamlit
langchain
langchain-groq
langchain-core
python-dotenv
sqlite3
```

## 🗄️ Database Setup

Run the database initialization script first:
```bash
python database_setup.py
```

This will create the `STUDENTS.db` database with sample data.

## 💻 Usage

1. **Start the Streamlit application**
```bash
streamlit run app.py
```

2. **Ask questions in natural language**

Example queries:
- "How many students are there?"
- "Show me all students in section A"
- "Which students scored more than 80 marks?"
- "List all students studying Data Science"

## 📁 Project Structure

```
.
├── app.py                 # Main Streamlit application
├── database_setup.py      # Database initialization script
├── STUDENTS.db           # SQLite database (generated)
├── .env                  # Environment variables (not tracked)
├── requirements.txt      # Python dependencies
└── README.md            # Project documentation
```

## 🎯 Database Schema

**Table: STUDENTS**
| Column  | Type        | Description           |
|---------|-------------|-----------------------|
| NAME    | VARCHAR(25) | Student name          |
| MARKS   | INT         | Marks obtained        |
| COURSE  | VARCHAR(25) | Course name           |
| SECTION | VARCHAR(25) | Section (A, B, or C)  |

## 🔑 Getting Groq API Key

1. Visit [Groq Cloud](https://console.groq.com/)
2. Sign up or log in
3. Navigate to API Keys section
4. Create a new API key
5. Copy and paste it into your `.env` file

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 👨‍💻 Author

**Your Name**
- GitHub: [@yourusername](https://github.com/yourusername)

## 🙏 Acknowledgments

- LangChain for the AI framework
- Groq for the LLM API
- Streamlit for the web framework

## 📧 Contact

For questions or feedback, please reach out at syed277526@gmail.com

---

⭐ If you found this project helpful, please give it a star!
