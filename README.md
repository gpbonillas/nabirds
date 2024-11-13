# The NABirds Dataset

[NABirds](https://dl.allaboutbirds.org/nabirds) is a collection of 48,000 annotated photographs of the 400 species of birds that are commonly observed in North America. More than 100 photographs are available for each species, including separate annotations for males, females and juveniles that comprise 700 visual categories. This dataset is to be used for fine-grained visual categorization experiments.

More than 550 visual categories, organized taxonomically
Photos curated in collaboration with domain experts.

## Versions
v0 - June 2015: initial release


For more information about the dataset, visit the project websites:

  - http://www.vision.caltech.edu/visipedia
  - http://vision.cornell.edu/se3/projects/visipedia/
  - http://dl.allaboutbirds.org/nabirds

If you use the dataset in a publication, please cite the dataset in
the style described on the dataset website (see url above).

Please see the nabirds.py file for example code on using the data. You can 
visualize images and annotations by running:
  python nabirds.py
Make sure you are in the nabirds/ directory

## Directory Information

- `images/`
    The images organized in subdirectories based on species. See 
    **IMAGES AND CLASS LABELS** section below for more info.
- `parts/`
    11 part locations per image. See **PART LOCATIONS** section below 
    for more info.

## IMAGES AND CLASS LABELS:
Images are contained in the directory `images/`, with 555 subdirectories (one for each bird category)

### List of image files (_images.txt_) 
The list of image file names is contained in the file images.txt, with each line corresponding to one image:

> `<image_id> <image_name>`

### Train/test split (_train_test_split.txt_)
The suggested train/test split is contained in the file train_test_split.txt, with each line corresponding to one image:

> `<image_id> <is_training_image>`

where `<image_id>` corresponds to the ID in images.txt, and a value of 1 or 0 for `<is_training_image>` denotes that the file is in the training or test set, respectively.

### Image sizes (_sizes.txt_)
The size of each image in pixels:

> `<image_id> <width> <height>`

where `<image_id>` corresponds to the ID in images.txt, and `<width>` and `<height>` correspond to the width and height of the image in pixels.

### Image photographers (_photographers.txt_) 
The photographer for each image:

> `<image_id> <photographer_name>`

where `<image_id>` corresponds to the ID in images.txt, and `<photographer_name>` corresponds to the name of the photographer that took the photo. Please
be considerate and display the photographer's name when displaying their image.

### List of class names (_classes.txt_)
The list of class names (bird species) is contained in the file classes.txt, with each line corresponding to one class:

> `<class_id> <class_name>`

### Image class labels (_image_class_labels.txt_)
The ground truth class labels (bird species labels) for each image are contained in the file image_class_labels.txt, with each line corresponding to one image:

> `<image_id> <class_id>`

where `<image_id>` and `<class_id>` correspond to the IDs in images.txt and classes.txt, respectively.

### Class hierarchy (_hierarchy.txt_)
The ground truth class labels (bird species labels) for each image are contained in the file image_class_labels.txt, with each line corresponding to one image:

> `<child_class_id> <parent_class_id>`

where `<child_class_id>` and `<parent_class_id>` correspond to the IDs in classes.txt.

## BOUNDING BOXES:

Each image contains a single bounding box label.  Bounding box labels are contained in the file _bounding_boxes.txt_, with each line corresponding to one image:

> `<image_id> <x> <y> <width> <height>`

where `<image_id>` corresponds to the ID in images.txt, and `<x>`, `<y>`, `<width>`, and `<height>` are all measured in pixels

## PART LOCATIONS:

### List of part names (_parts/parts.txt_)
The list of all part names is contained in the file `parts/parts.txt`, with each line corresponding to one part:

> `<part_id> <part_name>`


### Part locations (_parts/part_locs.txt_)
The set of all ground truth part locations is contained in the file `parts/part_locs.txt`, with each line corresponding to the annotation of a particular part in a particular image:

> `<image_id> <part_id> <x> <y> <visible>`

where `<image_id>` and `<part_id>` correspond to the IDs in images.txt and parts/parts.txt, respectively. `<x>` and `<y>` denote the pixel location of the center of the part.  `<visible>` is 0 if the part is not visible in the image and 1 otherwise.

## ABOUT IMAGES FILES
> **The `images` folder was ignored in this repository due to its size. You can download the images from the [NABirds](https://dl.allaboutbirds.org/nabirds) website.**

## SOURCE
The dataset is available at [NABirds](https://dl.allaboutbirds.org/nabirds)