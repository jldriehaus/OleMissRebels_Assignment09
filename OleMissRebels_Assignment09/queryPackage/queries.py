# File Name : OleMissRebels_Assignment09
# Student Name: Jack Driehaus and Drew Wolfe
# email:  driehajl@mail.uc.edu
# Assignment Number: Assignment 09
# Due Date:   04/03/2024
# Course #/Section:   IS4010-002
# Semester/Year:   spring 2025
# Brief Description of the assignment:  Work in a team to aacess the SQL server, extract data, and produce some interesting results

# Brief Description of what this module does: Makes the queries for the database
# Citations: 

# Anything else that's relevant:

from databaseConnection.databaseConnector import get_connection
import random

def fetch_products():
    conn = get_connection()
    cursor = conn.cursor()
    query = "SELECT ProductID, [UPC-A], Description, ManufacturerID, BrandID FROM dbo.tProduct"
    cursor.execute(query)
    products = cursor.fetchall()
    conn.close()
    return products


def get_random_product():
    products = fetch_products()
    selected_product = random.choice(products)
    return {
        "ProductID": selected_product[0],
        "Description": selected_product[2],
        "ManufacturerID": selected_product[3],
        "BrandID": selected_product[4]
    }


def get_manufacturer(manufacturer_id):
    conn = get_connection()
    cursor = conn.cursor()
    query = f"SELECT Manufacturer FROM tManufacturer WHERE ManufacturerID = {manufacturer_id}"
    cursor.execute(query)
    manufacturer = cursor.fetchone()
    conn.close()
    return manufacturer[0] if manufacturer else "Unknown Manufacturer"


def get_brand(brand_id):
    conn = get_connection()
    cursor = conn.cursor()
    query = f"SELECT Brand FROM tBrand WHERE BrandID = {brand_id}"
    cursor.execute(query)
    brand = cursor.fetchone()
    conn.close()
    return brand[0] if brand else "Unknown Brand"


def get_items_sold(product_id):
    conn = get_connection()  
    cursor = conn.cursor()
    query = """
    SELECT TOP (100) PERCENT SUM(dbo.tTransactionDetail.QtyOfProduct) AS NumberOfItemsSold
    FROM dbo.tTransactionDetail
    INNER JOIN dbo.tTransaction ON dbo.tTransactionDetail.TransactionID = dbo.tTransaction.TransactionID
    WHERE dbo.tTransaction.TransactionTypeID = 1
    AND dbo.tTransactionDetail.ProductID = ?;
    """
    cursor.execute(query, (product_id,))
    result = cursor.fetchone()  
    number_of_items_sold = result[0] if result[0] is not None else 0
    conn.close()  
    return number_of_items_sold
