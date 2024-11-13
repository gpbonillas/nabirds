from PIL import Image
import psycopg2
import io
import matplotlib.pyplot as plt

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
cur.execute("SELECT image_id, path_image, image_file, ROW_NUMBER () OVER (ORDER BY image_id) as i FROM image_files LIMIT 10")
if cur.rowcount == 0:
    print("No images in the database")
    exit()

plt.figure(figsize=(20, 10))

for image_id, path_image, image_file, i in cur.fetchall():
    # plot all images in one plot figure with 2 rows and 5 columns
    plt.subplot(2, 5, i)
    # read the image file from the database
    image = Image.open(io.BytesIO(image_file))
    plt.imshow(image)
    plt.title(f"image: {i}")
    plt.axis('off')

plt.show()