from os.path import exists
import psycopg2

# connect to the database
conn = psycopg2.connect(
    database="nabirds",
    user="postgres",
    password="password",
    host="localhost",
    port="5432"
)

# set a commit counter
commit_counter = 0

# set commit max constant value
COMMIT_MAX = 1000

# Create a cursor
cur = conn.cursor()

# check if table exists
cur.execute("SELECT EXISTS (SELECT 1 FROM information_schema.tables WHERE table_name = 'image_files')")
if cur.fetchone()[0]:
    print("Table '%s' exists" % 'image_files')

# read the text file with the image paths
with open('../images.txt', 'r') as f:
    for linea in f:
        image_id = linea.strip().split(' ')[0]
        # get the path of the image
        path_image = linea.strip().split(' ')[1]
        # concatenate the path of the image
        path_image = f"images/{path_image}"

        # read the image file in binary mode
        with open(path_image, 'rb') as imagen_file:
            binary_image = imagen_file.read()

        # print the image_id, path_image and the binary image
        print("image_id: ", image_id, "path_image: ", path_image, "exist_image: ", exists(path_image))

        cur.execute("SELECT EXISTS (SELECT 1 FROM image_files WHERE image_id = %s)", (image_id,))
        if cur.fetchone()[0]:
            print("Image '%s' already exists" % image_id)
            continue
        else:
            print("Image '%s' does not exist" % image_id)
            # insert the image file into the database
            cur.execute(
                "INSERT INTO image_files (image_id, path_image, image_file) VALUES (%s, %s, %s)",
                (image_id, path_image, binary_image)
            )

            # check if the image was inserted successfully
            cur.execute("SELECT EXISTS (SELECT 1 FROM image_files WHERE image_id = %s)", (image_id,))
            if cur.fetchone()[0]:
                print("Image '%s' was inserted successfully" % image_id)
                commit_counter += 1
            else:
                print("Image '%s' was not inserted" % image_id)

        # commit the changes every 1000 images
        if commit_counter == COMMIT_MAX:
            conn.commit()
            commit_counter = 0

# commit the changes and close the cursor and the connection
conn.commit()
cur.close()
conn.close()