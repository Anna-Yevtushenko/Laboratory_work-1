import numpy as np
import matplotlib.pyplot as plt

first_object = np.array([[1.5, 0.5], [1.5, 2], [3.5, 2], [3.5, 0.5], [2.5, 1], [1.5, 0.5], [1.5, 2]])
second_object = np.array([[0, 0], [1, 2], [1, 0], [0, 0]])

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

##plot_objects = objects_visualization(first_object, second_object)

def rotate_object(object, angle_deg):
    angle_rad = np.radians(angle_deg)  # Перетворюємо градуси в радіани
    rotation_matrix = np.array([[np.cos(angle_rad), -np.sin(angle_rad)],
                                [np.sin(angle_rad), np.cos(angle_rad)]])
    rotated_obj = np.dot(object, rotation_matrix)
    return rotated_obj

def object_scaling(object, scale):
    scaled_obj = object * scale
    return scaled_obj

rotated_object = rotate_object(first_object, 90)
scaled_object = object_scaling(second_object, 2)

objects_visualization(rotated_object, scaled_object)

