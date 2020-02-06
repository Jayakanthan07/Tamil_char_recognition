import cv2
import numpy as np

from os import walk, system

def get_files(files_path):
  for (dirpath, dirnames, filenames) in walk(files_path):
    return filenames


def execute_convert(files):
  i = 0
  s = " "
  for file in files:
    exec_string = s.join([
      "convert",
      "atiff\\"+file,
      "-resize",
      "160x160",
      "-gravity",
      "center",
      "-extent",
      "160x160",
      "pngs\\"+str(i)+".png"
    ])
    print(exec_string)
    system(exec_string)
    i += 1


def pngs_to_bin(files):
  datas = []
  for file in files:
    data = "pngs\\"+file
    # print(data)
    image = cv2.imread(data, cv2.IMREAD_GRAYSCALE)
    contents = np.array(image, dtype=bytes)
    np.set_printoptions(precision=3)
    datas.append(contents)
    print(contents)
  
  # np.savetxt("a2.bin", datas)
    




files_path = "./atiff"
png_files_path = "./pngs"

files = get_files(png_files_path)
# execute_convert(files)
pngs_to_bin(files)
