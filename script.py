import os
import csv
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()


from products.models import Products


def load_data_from_csv(file_name):
    if not os.path.exists(file_name):
        print(f"file : {file_name} does not exist...!!!")
        return
    try:
        with open(file_name,'r') as csvfile:
            reader = csv.DictReader(csvfile)
            products = []

            for row in reader:
                product_name = row.get('product_name')
                brand = row.get('brand')
                price = row.get('price')

                if not product_name or not brand or not price:
                    print(f"Skipping row with missing data : {row}")
                    continue

                products.append(Products(
                    product_name = product_name,
                    brand = brand,
                    price = price
                ))
            
            Products.objects.bulk_create(products)
            print(f"Successfully uploaded {len(products)} products")

    except Exception as e :
        print(f"An error occured: {e}")


if __name__ == "__main__":
    csv_file_path = "MOCK_DATA.csv"
    load_data_from_csv(csv_file_path)