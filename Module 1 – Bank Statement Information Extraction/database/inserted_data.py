from database.db_connection import get_connection
from datetime import datetime


def format_date(date_value):

    if not date_value:
        return None

    possible_formats = [

        "%d %b %Y",      # 30 Jul 2023
        "%d-%m-%Y",      # 30-07-2023
        "%d/%m/%Y",      # 30/07/2023
        "%Y-%m-%d",      # 2023-07-30
        "%d %B %Y"       # 30 July 2023

    ]

    for fmt in possible_formats:

        try:

            converted = datetime.strptime(
                date_value.strip(),
                fmt
            )

            return converted.strftime(
                "%Y-%m-%d"
            )

        except:

            pass

    return None


def save_basic_details(data):

    connection = get_connection()

    cursor = connection.cursor()

    data["account_open_date"] = format_date(
        data.get("account_open_date")
    )

    data["statement_date"] = format_date(
        data.get("statement_date")
    )

    data["from_date"] = format_date(
        data.get("from_date")
    )

    data["to_date"] = format_date(
        data.get("to_date")
    )


    sql = """

    INSERT INTO basic_details(

    bank_name,
    bank_branch,
    ifsc_code,
    micr_no,
    bank_id,
    account_number,
    account_address,
    account_open_date,
    account_type,
    cif_no,
    nominee_exist,
    mobile_no,
    email_id,
    statement_date,
    from_date,
    to_date,
    customer_id

    )

    VALUES(

    %s,%s,%s,%s,%s,%s,%s,%s,%s,
    %s,%s,%s,%s,%s,%s,%s,%s

    )

    """

    values = (

        data.get("bank_name"),
        data.get("bank_branch"),
        data.get("ifsc_code"),
        data.get("micr_no"),
        data.get("bank_id"),
        data.get("account_number"),
        data.get("account_address"),
        data.get("account_open_date"),
        data.get("account_type"),
        data.get("cif_no"),
        data.get("nominee_exist"),
        data.get("mobile_no"),
        data.get("email_id"),
        data.get("statement_date"),
        data.get("from_date"),
        data.get("to_date"),
        data.get("customer_id")

    )

    cursor.execute(
        sql,
        values
    )

    connection.commit()

    inserted_id = cursor.lastrowid

    connection.close()

    return inserted_id