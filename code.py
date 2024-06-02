import numpy as np
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
    PI = 3.141592653589793
    angle_rad = angle_deg * (PI / 180)
    rotation_matrix = np.array([[np.cos(angle_rad), -np.sin(angle_rad)],
                                [np.sin(angle_rad), np.cos(angle_rad)]])
    rotated_obj = np.dot(object, rotation_matrix) #множимо об'єкт на матрицю обертання
    return rotated_obj

def object_scaling(object, scale):
    scaled_obj = object * scale
    return scaled_obj

def reflect_object(object, axis):
    if axis.lower() == 'x':
        reflection_matrix = np.array([[1, 0],
                                      [0, -1]])
    elif axis.lower() == 'y':
        reflection_matrix = np.array([[-1, 0],
                                      [0, 1]])
    else:
        raise ValueError("Write 'x' or 'y'")
    reflected_obj = np.dot(object, reflection_matrix) # множимо на матрицю відзеркалення
    return reflected_obj

def shear_object(object, axis, factor):
    if axis.lower() == 'x':
        shear_matrix = np.array([[1, factor],
                                 [0, 1]])
    elif axis.lower() == 'y':
        shear_matrix = np.array([[1, 0],
                                 [factor, 1]])
    else:
        raise ValueError("Write 'x' or 'y'")
    sheared_obj = np.dot(object, shear_matrix)
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
            print("Invalid object.Choose between '1' and '2': ")
            continue

        if command == 'rotate':
            angle = float(input("Write angle in degrees: "))
            result = rotate_object(obj, angle)

        elif command == 'scale':
            scale = float(input("Write scale factor: "))
            result = object_scaling(obj, scale)
        elif command == 'reflect':
            axis = input("Write axis (x or y): ").strip().lower()
            result = reflect_object(obj, axis)
        elif command == 'shear':
            axis = input("Write axis (x or y): ").strip().lower()
            factor = float(input("Enter shear factor: ")) # кофіцієнт нахилу
            result = shear_object(obj, axis, factor)

        else:
            print("Invalid command ")
            continue
        objects_visualization(result, obj)

        continue

if __name__ == "__main__":
    main()
