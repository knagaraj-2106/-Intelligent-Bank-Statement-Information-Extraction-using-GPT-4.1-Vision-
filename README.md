# 🏦 Intelligent Bank Statement Information Extraction using GPT-4.1 (Vision)

## 📌 Project Overview

The **Intelligent Bank Statement Information Extraction System** is a Generative AI application developed to extract structured information from bank statement PDF documents using **OpenAI GPT-4.1 Vision (VLM)**.

The project is designed to process bank statements uploaded by users and convert the unstructured document into structured JSON data, which is then stored in a **MySQL database** for further analysis and reporting.

Since bank statements contain a large amount of information and the **GPT-4.1 Vision model has a context window limitation**, the extraction process has been divided into **two independent modules**.

This approach improves extraction accuracy while avoiding context length limitations.

---

# Project Objectives

* Extract customer and bank information from bank statements.
* Extract transaction details separately.
* Convert unstructured PDF documents into structured JSON.
* Store extracted information into MySQL database.
* Build a modular document processing pipeline using Generative AI.

---

# Technologies Used

| Technology              | Purpose                                         |
| ----------------------- | ----------------------------------------------- |
| Python                  | Application Development                         |
| OpenAI GPT-4.1 (Vision) | Document Understanding & Information Extraction |
| LangChain               | LLM Integration                                 |
| Prompt Engineering      | Structured JSON Extraction                      |
| Streamlit               | User Interface                                  |
| MySQL                   | Data Storage                                    |
| VS Code                 | Development Environment                         |

---

# System Workflow

```text
                 Upload Bank Statement PDF
                           │
                           ▼
                  Streamlit User Interface
                           │
                           ▼
                  PDF Page Extraction
                           │
                           ▼
             GPT-4.1 Vision (LLM Processing)
                           │
             ┌─────────────┴──────────────┐
             │                            │
             ▼                            ▼
      Part-1 Extraction             Part-2 Extraction
  Basic Statement Details      Transaction Information
             │                            │
             └─────────────┬──────────────┘
                           ▼
                 Structured JSON Output
                           │
                           ▼
                  MySQL Database Storage
```

---

# Project Modules

## Module 1 – Bank Statement Information Extraction

The first module extracts customer and bank-related information available in the statement.

### Extracted Fields

* bank_name
* bank_branch
* ifsc_code
* micr_no
* bank_id
* account_number
* account_address
* account_open_date
* account_type
* cif_no
* nominee_exist
* mobile_no
* email_id
* statement_date
* from_date
* to_date
* customer_id

The extracted information is converted into a structured JSON object and stored in the **Basic Statement Details** table in MySQL.

---

## Module 2 – Transaction Information Extraction

The second module focuses only on transaction-level information.

### Extracted Fields

* statement_id
* transaction_date
* description
* transaction_no
* cheque_no
* debit_amount
* credit_amount
* balance_amount

Each transaction extracted by the LLM is inserted into the **Transaction Details** table in MySQL using the generated **statement_id**.

---

# Why Two Separate Modules?

Bank statements often contain multiple pages with both customer information and transaction history.

Processing the complete document in a single LLM request resulted in exceeding the **GPT-4.1 Vision context window**.

To overcome this limitation, the extraction process was divided into two stages:

### Part-1

Extracts only the bank and customer information.

### Part-2

Extracts only transaction information.

This modular design improves:

* Extraction accuracy
* Prompt clarity
* Maintainability
* Database organization

---

# Database Design

The application stores extracted information into MySQL.

## Table 1

### Basic Statement Details

Stores:

* Bank Information
* Customer Information
* Statement Information

Primary Key:

```
statement_id
```

---

## Table 2

### Transaction Details

Stores every transaction associated with a statement.

Foreign Key:

```
statement_id
```

Relationship:

```
One Statement
      │
      │
      ├──────── Transaction 1
      ├──────── Transaction 2
      ├──────── Transaction 3
      ├──────── Transaction n
```

---

# Features

* Upload bank statement PDF
* GPT-4.1 Vision-based document understanding
* Prompt-engineered JSON extraction
* Two-stage extraction pipeline
* Automatic MySQL insertion
* Structured storage of customer and transaction information
* Streamlit-based user interface

---

# Technical Architecture

```
                   ┌──────────────────────┐
                   │  Streamlit UI        │
                   └──────────┬───────────┘
                              │
                              ▼
                  Upload Bank Statement PDF
                              │
                              ▼
                    PDF Page Processing
                              │
                              ▼
                   GPT-4.1 Vision (LLM)
                              │
              ┌───────────────┴──────────────┐
              │                              │
              ▼                              ▼
      Part-1 Prompt                  Part-2 Prompt
(Bank Details Extraction)     (Transaction Extraction)
              │                              │
              ▼                              ▼
       Structured JSON              Structured JSON
              │                              │
              └───────────────┬──────────────┘
                              ▼
                     MySQL Database
```

---

# Prompt Engineering Strategy

Two independent prompts were designed:

**Prompt 1**

Focused only on extracting:

* Bank Information
* Customer Information
* Statement Information

**Prompt 2**

Focused only on extracting:

* Transaction Details

This separation minimizes unnecessary context sent to the model and improves structured extraction quality.

---

---

# Future Enhancements

* Support for multiple bank statement formats.
* Batch processing of multiple PDFs.
* Validation of extracted fields before database insertion.
* Export extracted data to Excel or CSV.
* Dashboard for viewing extracted statement summaries.

---

## Key Highlights

* **Modular two-stage extraction pipeline** designed to handle GPT-4.1 Vision context window limitations.
* **Prompt engineering** tailored separately for statement metadata and transaction details.
* **Structured JSON outputs** are persisted directly into **MySQL**.
* **Streamlit** provides a simple interface for uploading bank statement PDFs.
* **LangChain** orchestrates interactions with the GPT-4.1 Vision model.

This README accurately reflects the architecture and functionality you described without introducing unsupported features or assumptions beyond your stated implementation.
