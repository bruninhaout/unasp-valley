from os import walk
import pygame

def import_folder(path):
	surface_list = []
	
    #get the full path and use to import the imagem as a surface 
	for _, __, img_files in walk(path): #folder name, sub folder, images
		print(img_files)
		for image in img_files:
			full_path = path + '/' + image
			image_surf = pygame.image.load(full_path).convert_alpha()
			surface_list.append(image_surf)

	return surface_list

