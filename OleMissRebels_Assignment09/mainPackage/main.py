# File Name : OleMissRebels_Assignment09
# Student Name: Drew Wolfe
# email:  wolfeaw@mail.uc.edu
# Assignment Number: Assignment 09
# Due Date:   04/03/2024
# Course #/Section:   IS4010-002
# Semester/Year:   Spring 2025
# Brief Description of the assignment:  Work in a team to aacess the SQL server, extract data, and produce some interesting results
# Brief Description of what this module does: Instantiates the functions found in queryPackage and writes the sentence 
# Citations: 
# Anything else that's relevant:

from databaseConnection.databaseConnector import *
from queryPackage.queries import get_random_product, get_manufacturer, get_brand, get_items_sold

if __name__ == "__main__":

    def main():
        product = get_random_product()
        manufacturer = get_manufacturer(product["ManufacturerID"])
        brand = get_brand(product["BrandID"])
        items_sold = get_items_sold(product["ProductID"])
        sentence = (
            f"The product '{product['Description']}' is manufactured by {manufacturer} under the {brand} brand, "
            f"and has sold {items_sold} units."
        )

        print(sentence)

    main()