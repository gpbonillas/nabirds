from os.path import exists
from PIL import Image
import psycopg2
import io
import matplotlib.pyplot as plt
import numpy as np

# connect to the database
conn = psycopg2.connect(
    database="nabirds",
    user="postgres",
    password="password",
    host="localhost",
    port="5432"
)

# Create a cursor
cur = conn.cursor()


# check if table exists
cur.execute("SELECT EXISTS (SELECT 1 FROM information_schema.tables WHERE table_name = 'image_files')")
if cur.fetchone()[0]:
    print("Table '%s' exists" % 'image_files')

# read the images from the database
cur.execute("SELECT image_id, path_image, image_file FROM image_files WHERE image_id = '0009051b-a76c-4a27-ac5d-bf410aea7e0c'")
if cur.rowcount == 0:
    print("No images in the database")
    exit()

for image_id, path_image, image_file in cur.fetchall():

    print("image_id: ", image_id, "path_image: ", path_image, "exist_image: ", exists(path_image))

    if image_id == '0009051b-a76c-4a27-ac5d-bf410aea7e0c':
        # read the image file in binary mode
        image = Image.open(io.BytesIO(image_file))
        print(image.size)
        print(image.mode)
        print(image.format)

        # plot the image
        # plt.close(1)
        fig = plt.figure(1)
        plt.imshow(image)
        plt.title("Image ID: %s " % (image_id))
        plt.axis('off')
        plt.show()