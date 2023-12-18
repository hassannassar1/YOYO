import shutil
from glob import glob
import os

os.mkdir("data0")
os.mkdir("data0/train")
train_images = "data0/train/images"
train_labels = "data0/train/labels"
os.mkdir(train_labels)
os.mkdir(train_images)

os.listdir("train")
for i in os.listdir("train")[:1]:
  l = os.path.join("train", i, "img1")
  for j in glob(os.path.join(l, "*.txt")):
    name = i+j.split('/')[-1].split(".")[0]+".txt"
    os.rename(j, name)
    shutil.move(name, os.path.join(train_labels ,name))
  for j in glob(os.path.join(l, "*.jpg")):
    name = i+j.split('/')[-1].split(".")[0]+".jpg"
    os.rename(j, name)
    shutil.move(name, os.path.join(train_images ,name))


os.mkdir("data0/valid")
valid_images = "data0/valid/images"
valid_labels = "data0/valid/labels"
os.mkdir(valid_labels)
os.mkdir(valid_images)

os.listdir("valid")
for i in os.listdir("valid")[:1]:
  l = os.path.join("valid", i, "img1")
  for j in glob(os.path.join(l, "*.txt")):
    name = i+j.split('/')[-1].split(".")[0]+".txt"
    os.rename(j, name)
    shutil.move(name, os.path.join(valid_labels ,name))
  for j in glob(os.path.join(l, "*.jpg")):
    name = i+j.split('/')[-1].split(".")[0]+".jpg"
    os.rename(j, name)
    shutil.move(name, os.path.join(valid_images ,name))