import cv2 as cv

def load_image(file_path):
    try:
        image = cv.imread(file_path)
        if image is None:
            raise Exception(f"Error: Unable to load image {file_path}")
        return image
    except Exception as error:
        print(error)

def main():
    image_path = "Shrek_(character).png"  


if __name__ == "__main__":
    main()