import sqlite3
import xml.etree.ElementTree as ET


class ProductFeed:
    def __init__(self, db_path):
        self.conn = None
        try:
            self.conn = sqlite3.connect(db_path)
        except Exception as e:
            print(e)

    def filter_products(self, query):
        """
        Fetches all products from the database and returns them in a list of dictionaries
        """
        self.conn.row_factory = sqlite3.Row
        result = self.conn.execute(query).fetchall()
        result_list = [dict(row) for row in result]
        return result_list

    def create_xml_file(self, products):
        """
        Creates an XML file with the given product data
        """
        root = ET.Element("rss", version="2.0", attrib={'xmlns:g': 'http://base.google.com/ns/1.0'})
        channel = ET.SubElement(root, "channel")
        for product in products:
            item = ET.SubElement(channel, "item")

            pid = ET.SubElement(item, "g:id")
            pid.text = product["product_id"]

            title = ET.SubElement(item, "g:title")
            title.text = product["title"]

            description = ET.SubElement(item, "g:description")
            description.text = product["description"]

            link = ET.SubElement(item, "link")
            link.text = product["link"]

            image_link = ET.SubElement(item, "g:image_link")
            image_link.text = "https://butopea.com/" + product["image"]

            additional_images = product["additional_images"].split("###")
            for image_url in additional_images:
                additional_image_link = ET.SubElement(item, "g:additional_image_link")
                additional_image_link.text = "https://butopea.com/" + image_url

            availability = ET.SubElement(item, "g:availability")
            if int(product["quantity"]) > 0:
                availability.text = "in_stock"
            else:
                availability.text = "out_of_stock"

            price = ET.SubElement(item, "g:price")
            price.text = str(round(float(product["price"]), 2)) + " " + "HUF"

            brand = ET.SubElement(item, "g:brand")
            brand.text = product["brand"]

            condition = ET.SubElement(item, "g:condition")
            condition.text = "new"
        tree = ET.ElementTree(root)
        tree.write("feed.xml", xml_declaration=True, encoding='utf-8')
        return {"status": "feed.xml saved in the same directory"}


def main():
    feed = ProductFeed("data.sqlite")

    """
    SQL query to filter the data from the tables according to the need.
    """
    sql_query = """
                WITH cte AS (
                  SELECT  
                        product_id,
                        image,
                        sort_order
                  FROM product_image
                  ORDER BY product_id, sort_order
                )
                SELECT 
                     product.product_id,
                     product_description.name AS title, 
                     product_description.description, 
                     "https://butopea.com/p/" || product.product_id AS link,
                     product.image,
                     GROUP_CONCAT(cte.image, "###") AS additional_images,
                     product.quantity,
                     product.price,
                     manufacturer.name AS brand
                FROM product
                JOIN manufacturer ON product.manufacturer_id = manufacturer.manufacturer_id
                JOIN product_description ON product.product_id = product_description.product_id
                JOIN cte ON product.product_id = cte.product_id

                WHERE
                    product.status = "1"
                GROUP BY 
                    product.product_id;
        """

    products = feed.filter_products(sql_query)
    print(feed.create_xml_file(products))


if __name__ == '__main__':
    main()
