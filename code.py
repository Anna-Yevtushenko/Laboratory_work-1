import numpy as np
import matplotlib.pyplot as plt

first_object = np.array([[0, 0], [1, 0], [1, 0.5], [0, 1]])
second_object = np.array([[0, 0], [1, 2]])


def objects_visualization(object1, object2):
    plt.figure(figsize=(8,8)) # Створення нового графіку розміром 10x10 дюймів
    plt.plot(object1[:, 0], object1[:, 1], 'b-', label='Object 1') #Вибираємо усі значення першого стовпця(1 та другу координату) з масиву object1
    plt.plot(object2[:, 0], object2[:, 1], 'r-', label='Object 2') #Вибираємо усі значення першого стовпця(1 та другу координату) з масиву object2
    plt.legend()#додаємо легенду на графік (показує де який об'єкт)
    plt.grid(True) #додаємо сітку на графік
#    plt.xlabel('X')
#    plt.ylabel('Y')
    plt.title('Objects in 2D Space')

    plt.xlim(-10, 15)
    plt.ylim(-10, 15)

    plt.axis('equal') #забезпечення рівного масштабу
    plt.show()#створюємо графік

plot_objects = objects_visualization(first_object, second_object)


def rotate_object(object, angle_deg):

    rotation_matrix = np.array([[np.cos(angle_deg), -np.sin(angle_deg)],
                                [np.sin(angle_deg), np.cos(angle_deg)]])


    rotated_obj = np.dot(object, rotation_matrix)
    return rotated_obj

rotated_object = rotate_object(first_object, 90)


def object_scaling(object, scale):
    object_scaling = object * scale
    return object_scaling


scaled_object = object_scaling(second_object, 5)

# Відображення масштабованого та оберненого об'єкта на графіку
objects_visualization(rotated_object, scaled_object)





