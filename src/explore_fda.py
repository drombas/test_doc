from oct_converter.readers import FDA
import matplotlib.pyplot as plt

# a sample .fda file can be downloaded from the Biobank resource here:
# https://biobank.ndph.ox.ac.uk/showcase/refer.cgi?id=31
filepath = "sample.fda"
fda = FDA(filepath, printing=False)

volume = fda.read_oct_volume()
meta = fda.read_any_info_and_make_dict(b'@PARAM_SCAN_04')
box = fda.read_any_info_and_make_dict(b'@EFFECTIVE_SCAN_RANGE')
fundus = fda.read_fundus_image().image

box =  box['bounding_box_fundus_pixel']

min_x = box[0]
min_y = box[1]
plt.imshow(fundus)

# volume.peek(show_contours=True)

# n_axial = bscan[0].shape[0]
# # fundus = fda.read_fundus_image()
# # fundus_gray = fda.read_fundus_image_gray_scale()
# seg = fda.read_segmentation()

# # bscan.peek()  # plots a montage of the volume

# fig, ax = plt.subplots()
# i = 12
# ax.imshow(bscan[i], cmap='gray')
# [ax.plot(n_axial - seg[layer][i]) for layer in seg.keys()]
# ax.legend(seg.keys())

# # extract all other metadata
# output_json = dict()
# for key in fda.chunk_dict.keys():
#     if key in [b"@IMG_JPEG", b"@IMG_FUNDUS", b"@IMG_TRC_02", b"@CONTOUR_INFO"]:
#         # these chunks are image chunks and extracted with previous methods
#         continue
#     json_key = key.decode().split("@")[-1].lower()
#     try:
#         output_json[json_key] = fda.read_any_info_and_make_dict(key)
#     except KeyError:
#         print(f"{key} there is no method for getting info from this chunk.")
