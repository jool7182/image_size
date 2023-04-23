import binascii #As of now only works for png files
import sys

with open(sys.argv[1], 'rb') as f:   #reads binary data of image file
    read_data = f.read()

final = binascii.hexlify(read_data)   #converts binary data into ascii string
x = final.decode('ascii')

my_list = list(x)           
hex_list = []

for i in range(0, len(my_list)-1, 2):          #combines every other list element into one list element
    new_value = my_list[i] + my_list[i+1]
    hex_list.append(new_value)

image_width, image_height = hex_list[16:20], hex_list[20:24]

image_width_string = image_width[0]+image_width[1]+image_width[2]+image_width[3]
image_width_int = int(image_width_string,16)
image_height_string = image_height[0]+image_height[1]+image_height[2]+image_height[3]
image_height_int = int(image_height_string,16)

print(f'This image is {image_width_int} x {image_height_int} pixels')

    


