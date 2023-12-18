import os
import re
import configparser
from tqdm import tqdm


# File Format
# <frame>, <id>, <bb_left>, <bb_top>, <bb_width>, <bb_height>, <conf>, <x>, <y>, <z>

classes = {
    "Player": 0,
    "Ball": 1,
    "Goalkeeper": 2,
    "Goalkeepers": 2,
    "Referee": 3,
}

def format_football_data(base_dir=""):
    splits = ["train"]#"test"]

    pattern = re.compile(r"([a-zA-Z])\w+")

    config = configparser.ConfigParser()

    for split in tqdm(splits):
        split_dir = os.path.join(base_dir, split)

        for video in os.listdir(split_dir):
            # print(video)

            lbls_path = os.path.join(split_dir, video, "gt", "gt.txt")
            config.read(os.path.join(split_dir, video, "seqinfo.ini"))
            img_width = int(config["Sequence"]["imWidth"])
            img_height = int(config["Sequence"]["imHeight"])

            config.read(os.path.join(split_dir, video, "gameinfo.ini"))

            with open(lbls_path, "r") as lbls_file:
                lbls = lbls_file.readlines()
                lbls = [lbl.strip() for lbl in lbls]

            for lbl in lbls:
                lbl = lbl.split(",")

                frame, id_, xmin, ymin, bb_width, bb_height, _, _, _, _ = lbl

                c = config["Sequence"][f"trackletID_{id_}"]
                c = re.search(pattern, c)
                c = c.group(0).capitalize()
                if c == "Other":
                    continue
                c = classes[c]
                if c == 3:
                  continue
                if c==2:
                  c=0
                frame, xmin, ymin, bb_width, bb_height = (
                    int(frame),
                    int(xmin),
                    int(ymin),
                    int(bb_width),
                    int(bb_height),
                )

                xmax = xmin + bb_width
                ymax = ymin + bb_height

                x_center = (xmin + xmax) / (2.0 * img_width)
                y_center = (ymin + ymax) / (2.0 * img_height)
                width = (xmax - xmin) / img_width
                height = (ymax - ymin) / img_height

                with open(
                    os.path.join(split_dir, video, "img1", f"{frame:06d}.txt"), "a"
                ) as yolo_file:
                    yolo_file.write(
                        f"{c} {x_center:.6f} {y_center:.6f} {width:.6f} {height:.6f}\n"
                    )

            # with open(
            #     os.path.join(split_dir, video, "img1", "classes.txt"), "w"
            # ) as classes_file:
            #     classes_file.write("Player\n")
            #     classes_file.write("Ball\n")
            #     classes_file.write("Goalkeeper\n")
            #     classes_file.write("Referee\n")

            # return


if __name__ == "__main__":
    # main()
    format_football_data()