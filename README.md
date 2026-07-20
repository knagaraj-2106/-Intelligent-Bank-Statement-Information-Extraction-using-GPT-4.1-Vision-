# 🏦 Intelligent Bank Statement Information Extraction using GPT-4.1 Vision

## 📌 Project Overview

This project is an AI-powered Bank Statement Information Extraction System developed using **OpenAI GPT-4.1 Vision**, **Python**, **LangChain**, **Streamlit**, and **MySQL**.

The application extracts structured information from scanned and digital bank statements and stores the extracted data into a MySQL database for downstream reporting and analytics.

Since a complete bank statement contains a large amount of information that exceeds the context window limitations of GPT-4.1 Vision, the extraction process has been divided into **two independent modules**.

---

# 🎯 Client Requirement

The client receives bank statements in PDF format from multiple banks.

The manual process of identifying customer details and transaction history was:

- Time-consuming
- Error-prone
- Difficult to scale
- Required manual data entry into databases

The client required an AI solution capable of:

- Uploading bank statement PDFs
- Automatically extracting customer information
- Automatically extracting transaction details
- Storing extracted information into MySQL
- Eliminating manual data entry
- Improving processing speed and accuracy

---

# 💡 Proposed AI Solution

To solve the above problem, an AI-powered document extraction system was developed using GPT-4.1 Vision.

The complete extraction pipeline was divided into two modules.

---

# 📂 Project Architecture

```
                        Bank Statement PDF
                               │
                               ▼
                     Upload via Streamlit UI
                               │
                               ▼
                    GPT-4.1 Vision (OpenAI)
                               │
          ┌────────────────────┴────────────────────┐
          │                                         │
          ▼                                         ▼
 Module-1 Extraction                      Module-2 Extraction
(Customer Information)                  (Transaction Details)
          │                                         │
          └────────────────────┬────────────────────┘
                               │
                               ▼
                     Structured JSON Output
                               │
                               ▼
                        MySQL Database
                               │
                               ▼
                    Excel / Reporting Output
```

---

# 📁 Project Folder Structure

```
Intelligent-Bank-Statement-Information-Extraction-using-GPT-4.1-Vision/
│
├── AI Extracted Output/
│   ├── AI Extracted Data From Bank Statements.xlsx
│   └── excel/
│
├── Module 1 – Bank Statement Information Extraction/
│   │
│   ├── database/
│   │
│   ├── extraction/
│   │
│   ├── llm/
│   │
│   ├── app.py
│   └── config.py
│
├── Module 2 – Transaction Information Extraction/
│   │
│   ├── app.py
│   ├── main.py
│   └── pdf_reader.py
│
├── uploads/
│
└── README.md
```

---

# 🔹 Module 1

## Objective

Extract customer-related information from the uploaded bank statement.

### Extracted Fields

- Bank Name
- Bank Branch
- IFSC Code
- MICR Number
- Bank ID
- Account Number
- Account Address
- Account Opening Date
- Account Type
- CIF Number
- Nominee Availability
- Mobile Number
- Email Address
- Statement Date
- Statement From Date
- Statement To Date
- Customer ID

---

# 🔹 Module 2

## Objective

Extract all transaction-level information from the bank statement.

### Extracted Fields

- Statement ID
- Transaction Date
- Description
- Transaction Number
- Cheque Number
- Debit Amount
- Credit Amount
- Balance Amount

---

# 🗄 Database

The extracted information is stored into a MySQL database after every successful LLM response.

This enables:

- Data persistence
- Reporting
- Analytics
- Future integrations

---

# ⚙ Technology Stack

| Technology | Purpose |
|------------|----------|
| Python | Backend Development |
| GPT-4.1 Vision | Document Understanding & Information Extraction |
| OpenAI API | Large Language Model |
| LangChain | LLM Orchestration |
| Streamlit | User Interface |
| MySQL | Database |
| Prompt Engineering | Structured Data Extraction |
| VS Code | Development IDE |

---

# 🚀 Project Workflow

```
Upload PDF

      │

      ▼

Read PDF

      │

      ▼

Send PDF to GPT-4.1 Vision

      │

      ▼

Extract Required Fields

      │

      ▼

Validate Output

      │

      ▼

Store into MySQL

      │

      ▼

Generate Structured Output
```

---

# 📊 Output

The application produces:

- Structured customer information
- Structured transaction information
- MySQL database records
- Excel output for reporting

---

# ▶ How to Run

### Clone Repository

```bash
git clone <repository-url>
```

---

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

### Configure OpenAI API Key

Create a `.env` file.

```
OPENAI_API_KEY=your_api_key
```

---

### Run Streamlit

Module 1

```bash
streamlit run app.py
```

Module 2

```bash
streamlit run app.py
```

---

# ✅ Features

- AI-powered bank statement extraction
- GPT-4.1 Vision integration
- Streamlit-based user interface
- Structured JSON extraction
- MySQL database integration
- Excel output generation
- Modular extraction approach
- Prompt engineering for structured output

---

# 📈 Business Benefits

- Eliminates manual data entry
- Faster document processing
- Structured data storage
- Reduced human errors
- Scalable extraction workflow
- Simplifies reporting and auditing

---

# 📌 Future Enhancements

- Support for multiple bank formats
- OCR integration for scanned documents
- Batch document processing
- REST API integration
- Dashboard for analytics
- Automated validation rules

---

# 👨‍💻 Developed By

**Nagaraj Kamale**

Generative AI Engineer

**Tech Stack**

Python • OpenAI GPT-4.1 Vision • LangChain • Prompt Engineering • Streamlit • MySQL
````
