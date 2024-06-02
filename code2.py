import numpy as np
import cv2 as cv


first_object = np.array([[1.5, 0.5], [1.5, 2], [3.5, 2], [3.5, 0.5], [2.5, 1], [1.5, 0.5], [1.5, 2]])
second_object = np.array([[0, 0], [1, 2], [1, 0], [0, 0]])

def start_program():
    while True:
        start_program = input("Do you want to start? Write 'y' or 'n': ").strip().lower()
        if start_program == 'y':
            return True
        elif start_program == 'n':
            print("Program exited.")
            exit()
        else:
            print("You entered an invalid answer. Please enter 'y' or 'n'.")

def objects_visualization(object1, object2, title='Objects in 2D Space'):
    img = np.ones((500, 500, 3), dtype=np.uint8) * 255  # створення білого фону

    object1 = (object1 * 50 + 250).astype(int) # Масштабування об'єктів (для кращої візуалізації)
    object2 = (object2 * 50 + 250).astype(int)

    for i in range(len(object1) - 1): # Малювання першого об'єкта (синій колір)
        cv.line(img, tuple(object1[i]), tuple(object1[i + 1]), (255, 0, 0), 2)
    for i in range(len(object2) - 1): # Малювання другого об'єкта (червоний колір)
        cv.line(img, tuple(object2[i]), tuple(object2[i + 1]), (0, 0, 255), 2)

    cv.imshow(title, img)
    cv.waitKey(0)
    cv.destroyAllWindows()

def rotate_object(object, angle_deg):
    center = tuple(np.mean(object, axis=0))  # Обчислюємо центр об'єкта, аби використовувати його як центр обертання
    rotation_matrix = cv.getRotationMatrix2D(center, angle_deg, 1.0) # Створюємо матрицю обертання для заданого кута в градусах навколо центру об'єкта
    rotated_obj = cv.transform(np.array([object]), rotation_matrix)[0]
    return rotated_obj

def scale_object(object, scale):
    pass

def reflect_object(object, axis):
    pass

def shear_object(object, axis, factor):
    pass

def custom_transform(object, matrix):
    pass



def main():
    start_program()
    while True:
        command = input("Enter command (rotate, scale, reflect, shear, custom, exit): ").strip().lower()
        if command == 'exit':
            print('Exit!')
            break

        obj_choice = input("Choose object (1 or 2): ").strip()
        if obj_choice == '1':
            obj = first_object
        elif obj_choice == '2':
            obj = second_object
        else:
            print("Invalid object. Choose between '1' and '2'.")
            continue

        if command == 'rotate':
            angle = float(input("Write angle in degrees: "))
            result = rotate_object(obj, angle)
        elif command == 'scale':
            scale = float(input("Write scale factor: "))
            result = scale_object(obj, scale)
        elif command == 'reflect':
            axis = input("Write axis (x or y): ").strip().lower()
            result = reflect_object(obj, axis)
        elif command == 'shear':
            axis = input("Write axis (x or y): ").strip().lower()
            factor = float(input("Enter shear factor: "))
            result = shear_object(obj, axis, factor)
        elif command == 'custom':
            matrix = input("Enter custom transformation matrix (as a flattened list): ").strip()
            matrix = np.array([float(x) for x in matrix.split()]).reshape((2, 3))
            result = custom_transform(obj, matrix)
        else:
            print("Invalid command")
            continue

        objects_visualization(result, obj)


if __name__ == "__main__":
    main()
