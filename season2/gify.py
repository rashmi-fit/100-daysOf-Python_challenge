from PIL import Image
import os

def create_gif(image_folder, output_file, duration=500):
    images = []

    # Get the list of image files in the folder
    for filename in sorted(os.listdir(image_folder)):
        if filename.endswith('.png') or filename.endswith('.jpg'):
            images.append(Image.open(os.path.join(image_folder, filename)))

    # Save as GIF
    images[0].save(output_file, save_all=True, append_images=images[1:], loop=0, duration=duration)

if __name__ == "__main__":
    image_folder = "image"  # Replace with your image folder path
    output_file = "output.gif"  # Replace with your desired output file path
    duration = 500  # Duration in milliseconds for each frame (you can adjust this)

    create_gif(image_folder, output_file, duration)
