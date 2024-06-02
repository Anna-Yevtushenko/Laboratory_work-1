import cv2 as cv

def load_image(file_path):
    try:
        image = cv.imread(file_path)
        if image is None:
            raise Exception(f"Error: Unable to load image {file_path}")
        return image
    except Exception as error:
        print(error)

def display_images(images, titles):
    for image, title in zip(images, titles):
        # Відображаємо кожне зображення у вікні з відповідним заголовком
        cv.imshow(title, image)
    cv.waitKey(0)
    cv.destroyAllWindows()

def rotate_image(image, angle):
    # Отримуємо висоту і ширину зображення
    height, width = image.shape[:2]
    # Визначаємо центр зображення для обертання
    center = (width // 2, height // 2)
    # Створюємо матрицю обертання для заданого кута навколо центру зображення
    rotation_matrix = cv.getRotationMatrix2D(center, angle, 1.0)
    # Виконуємо обертання зображення за допомогою матриці обертання
    rotated_image = cv.warpAffine(image, rotation_matrix, (width, height))
    return rotated_image

def scale_image(image, scale):
    scaled_image = cv.resize(image, None, fx=scale, fy=scale, interpolation=cv.INTER_LINEAR)
    return scaled_image

def reflect_image(image, axis):
    if axis.lower() == 'x':
        # cv.flip з параметром 0 віддзеркалює зображення по горизонталі (відносно осі x)
        reflected_image = cv.flip(image, 0)
    elif axis.lower() == 'y':
        # cv.flip з параметром 1 віддзеркалює зображення по вертикалі (відносно осі y)
        reflected_image = cv.flip(image, 1)
    else:

        print("Axis must be 'x' or 'y'")

    return reflected_image


def main():
    image_path = "Shrek_(character).png"
    image = load_image(image_path)

    if image is not None:
        images = [image]

        # Apply rotation
        rotated_image = rotate_image(image, 45)
        images.append(rotated_image)

        # Apply scaling
        scaled_image = scale_image(image, 0.5)
        images.append(scaled_image)

        # Apply reflection
        reflected_image = reflect_image(image, 'y')
        images.append(reflected_image)

        titles = ['Original Image', 'Rotated Image', 'Scaled Image', 'Reflected Image']
        display_images(images, titles)


if __name__ == "__main__":
    main()