import os

from PIL import Image

c = 0

labels_folder = "labels"
labels = os.listdir(labels_folder)

with open("annotations.txt", "w") as fw:
    for label in labels:

        doors_formatted_str = ""
        label_no_extension = os.path.splitext(os.path.basename(label))[0]
        image_filename = f"{label_no_extension}.jpg"
        image_path = os.path.join("images", image_filename)

        if os.path.exists(image_path) is False:
            image_filename = f"{label_no_extension}.png"
            image_path = os.path.join("images", image_filename)

        if os.path.exists(image_path) is False:
            image_filename = f"{label_no_extension}.JPG"
            image_path = os.path.join("images", image_filename)

        if os.path.exists(image_path) is False:
            image_filename = f"{label_no_extension}.jpeg"
            image_path = os.path.join("images", image_filename)

        if os.path.exists(image_path) is False:

            continue
            # raise BaseException(f"NOT FOUND PNG OR JPG MATCH TO {label}")

        im = Image.open(image_path)
        width, height = im.size
        with open(os.path.join(labels_folder, label), "r") as fr:
            c+=1
            print(c)
            doors = []
            for line in fr:
                idx = int(line[0])
                # if not door delete:
                if idx != 0:
                    try:
                        os.remove(image_path)
                        os.remove(os.path.join(labels_folder, label))
                    except Exception as e:
                        print(e)
                else:
                    str_yolo_door = line[2:]
                    list_yolo_door = str_yolo_door.strip('\n').split(" ")
                    x_center = float(list_yolo_door[0])
                    y_center = float(list_yolo_door[1])
                    x_width = float(list_yolo_door[2])
                    y_height = float(list_yolo_door[3])

                    x_min = int(width * (x_center - x_width / 2))
                    y_min = int(height * (y_center - y_height / 2))
                    x_max = int(width * (x_center + x_width / 2))
                    y_max = int(height * (y_center + y_height / 2))

                    # "[[xmin1, ymin1, width1, height1,color1], ]"
                    doors.append([x_min, y_min, x_max - x_min, y_max - y_min, idx + 1])

            if len(doors) > 0:
                doors_formatted_str = str(doors)[1:-1]
                fw.write(f"{image_filename}:{doors_formatted_str}\n")
