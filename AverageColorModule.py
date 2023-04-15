"""
created at 06-10-22 by Halil is
This Module select average color of image 
for i in img
   for j in i
     add totalred to red 
     add totalgreen to green
     add totalblue to blue 
avgred = totalred/(total count of pixel)
"""
from cv2 import imread
from cv2 import IMREAD_COLOR

class averageColorModule:

  def __init__(__self__):

    pass


  """
  args:
  img_location: string value that represent location of image
  """
  def average_color(__self__,img_location):
    try:
        img = imread(img_location,IMREAD_COLOR)
        total_red = 0
        total_blue = 0
        total_green = 0
        total_pixel = 0
        for i in img:
          for j in i:# j is individual rgb values for each pixel [r,g,b]
              total_red += j[0]
              total_green += j[1]
              total_blue += j[2]
              total_pixel +=1
        average_rgb = [int(total_red/total_pixel),int(total_green/total_pixel),int(total_blue/total_pixel)]
        return average_rgb
    except Exception as ex:
        print(ex,':\t',img_location)