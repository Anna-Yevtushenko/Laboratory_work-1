import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

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

def objects_visualization(object1, object2):
    plt.figure(figsize=(8, 8))
    plt.plot(object1[:, 0], object1[:, 1], 'b-', label='Object 1')
    plt.plot(object2[:, 0], object2[:, 1], 'r-', label='Object 2')
    plt.legend()
    plt.grid(True)
    plt.title('Objects in 2D Space')
    plt.xlim(-10, 15)
    plt.ylim(-10, 15)
    plt.axis('equal')
    plt.show()
def rotate_object(object, angle_deg):
    center = tuple(np.mean(object, axis=0))  # Обчислюємо центр об'єкта, аби використовувати його як центр обертання
    rotation_matrix = cv.getRotationMatrix2D(center, angle_deg, 1.0) # Створюємо матрицю обертання для заданого кута в градусах навколо центру об'єкта
    rotated_obj = cv.transform(np.array([object]), rotation_matrix)[0]
    return rotated_obj

def scale_object(object, scale):
    scaling_matrix = np.array([[scale, 0, 0], [0, scale, 0]], dtype=np.float32)
    scaled_obj = cv.transform(np.array([object]), scaling_matrix)[0]
    return scaled_obj

def reflect_object(object, axis):
    if axis.lower() == 'x':
        reflection_matrix = np.array([[1, 0], [0, -1]], dtype=np.float32)
    elif axis.lower() == 'y':
        reflection_matrix = np.array([[-1, 0], [0, 1]], dtype=np.float32)
    else:
        raise ValueError("Write 'x' or 'y'")
    # Виконуємо віддзеркалення об'єкта за допомогою матриці віддзеркалення
    reflected_obj = cv.transform(np.array([object]), reflection_matrix)[0]
    return reflected_obj


def shear_object(object, axis, factor):
    if axis.lower() == 'x':
        shear_matrix = np.array([[1, factor], [0, 1]], dtype=np.float32)
    elif axis.lower() == 'y':
        shear_matrix = np.array([[1, 0], [factor, 1]], dtype=np.float32)
    else:
        raise ValueError("Write 'x' or 'y'")

    # Виконуємо зсув об'єкта за допомогою матриці зсуву
    sheared_obj = cv.transform(np.array([object]), shear_matrix)[0]
    return sheared_obj




def main():
    start_program()
    while True:
        command = input("Enter command (rotate, scale, reflect, shear, exit): ").strip().lower()
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

        else:
            print("Invalid command")
            continue

        objects_visualization(result, obj)


if __name__ == "__main__":
    main()
