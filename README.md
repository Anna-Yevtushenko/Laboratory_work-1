# Лабораторна робота №1
#### Лінійні трансформації
---
### Перша частина
1. Для початку потрібно створити і візуалізувати об'єкти, на яких буде відображатись виконана лінійна трансформація у двовимірному просторі. Ваше завдання – створити **два різні** об'єкти.

```
first_object = np.array([[1.5, 0.5], [1.5, 2], [3.5, 2], [3.5, 0.5], [2.5, 1], [1.5, 0.5], [1.5, 2]])
```

```
second_object = np.array([[0, 0], [1, 2], [1, 0], [0, 0]])
```



2. Наступним кроком потрібно реалізувати функції, що будуть виконувати певні лінійні трансформації:
- обертати об'єкт на певний кут *(0,5 бали)*;
- маштабувати об'єкт з певним коефіцієнтом *(0,5 бали)*;
- віддзеркалювати об'єкт відносно певної осі *(0,5 бали)*;
- робити нахил певної осі координат *(0,5 бали)*;
- та універсальну функцію, що буде виконувати трансформацію з переданою у функцію кастомною матрицею трансформації *(0,25 балів)*.


<img src="https://github.com/Anna-Yevtushenko/Laboratory_work-1/assets/150729768/061a648b-0534-4fed-8e17-3ea6572f6522" style="height: 300px;"/> 

<img src="https://github.com/Anna-Yevtushenko/Laboratory_work-1/assets/150729768/3b98c641-2321-4068-a34a-3177d81afc1a" style="height: 300px;"/>

<img src="https://github.com/Anna-Yevtushenko/Laboratory_work-1/assets/150729768/e5c4a61c-d90f-4b6b-a625-da9cab25ccb9" style="height: 300px;"/>

<img src="https://github.com/Anna-Yevtushenko/Laboratory_work-1/assets/150729768/efa0a24b-89b9-412c-b9e7-b322343d4d0d" style="height: 300px;"/>


###


<img src="https://github.com/Anna-Yevtushenko/Laboratory_work-1/assets/150729768/8197c82b-f24b-450b-bad3-781a028a5e9f" style="height: 300px;"/>

<img src="https://github.com/Anna-Yevtushenko/Laboratory_work-1/assets/150729768/4861b8a0-bbc6-4b49-8154-158a63db3115" style="height: 300px;"/>

<img src="https://github.com/Anna-Yevtushenko/Laboratory_work-1/assets/150729768/1b64333f-71ed-499e-a207-23dfeebd2f81" style="height: 300px;"/>

<img src="https://github.com/Anna-Yevtushenko/Laboratory_work-1/assets/150729768/62aaa404-2256-47e1-a5e5-dca7fdd9952f" style="height: 300px;"/>

###

 > [!Tip]
> **Висновки:**
> 
>1)Масштабування (Scaling) - змінює розмір об'єкта вздовж осей X та Y
> 
>2)Обертання (Rotation) - змінює кут положення об'єкта відносно центру обертання.
>
>3)Відзеркалення (Reflection) - створює дзеркальний об’єкт відносно однієї або обох осей
>
>4)Зсув (Shear) - змінює форму об'єкта, нахиляючи його вздовж однієї з осей. 



### Друга частина 

1. Обрати бібліотеку із вже готовими функціями для лінійних трансформацій *(Рекомендую OpenCV, вона має найширший інструментарій; [Корисне посилання 1](https://docs.opencv.org/4.x/da/d6e/tutorial_py_geometric_transformations.html), [Корисне посилання 2](https://medium.com/@conghung43/image-projective-transformation-with-opencv-python-f0028aaf2b6d))*
2. За допомогою інструментарію бібліотеки реалізувати всі лінійни трансформації з пункту 2 попередньої частини на тих самих фігурах, створених у двовимірному просторі. Порівняти результати, отримані за допомогою готових бібліотек, з результатами роботи власних функцій *(1 бал)*.
3. Взяти довільне зображення, зчитати його за допомогою ``image = cv2.imread('image.jpg')`` та виконати 2-3 лінійні трансформації над цим зображенням. Вивести результуючі зображення *(1 бал)*.

   

<img src="https://github.com/Anna-Yevtushenko/Laboratory_work-1/assets/150729768/58e25eae-eff7-4203-81d7-d1ec00f3d0d6" style="height: 300px;"/> 

<img src="https://github.com/Anna-Yevtushenko/Laboratory_work-1/assets/150729768/3b98c641-2321-4068-a34a-3177d81afc1a" style="height: 300px;"/>

<img src="https://github.com/Anna-Yevtushenko/Laboratory_work-1/assets/150729768/e5c4a61c-d90f-4b6b-a625-da9cab25ccb9" style="height: 300px;"/>

<img src="https://github.com/Anna-Yevtushenko/Laboratory_work-1/assets/150729768/a247a448-2e80-4b6f-9e6c-240b18d38e91" style="height: 300px;"/>


###


<img src="https://github.com/Anna-Yevtushenko/Laboratory_work-1/assets/150729768/1afe589f-b5ab-4d41-9bc2-23f5f591c499" style="height: 300px;"/>

<img src="https://github.com/Anna-Yevtushenko/Laboratory_work-1/assets/150729768/61782771-12e9-4b56-8808-2a7a350a3a74" style="height: 300px;"/>

<img src="https://github.com/Anna-Yevtushenko/Laboratory_work-1/assets/150729768/a3b2ec52-e76f-4a7d-b2ee-d94994de66aa" style="height: 300px;"/>

<img src="https://github.com/Anna-Yevtushenko/Laboratory_work-1/assets/150729768/70c12632-fb5b-4b4f-80dc-62685aabc95e" style="height: 300px;"/>



###


3. Взяти довільне зображення, зчитати його за допомогою ``image = cv2.imread('image.jpg')`` та виконати 2-3 лінійні трансформації над цим зображенням. Вивести результуючі зображення *(1 бал)*


###
<img src="https://github.com/Anna-Yevtushenko/Laboratory_work-1/assets/150729768/f8c682f8-ec1a-4204-b1bb-21210f0010b6" style="height: 400px;"/>

---
### Теоретичні запитання *(2 бали)*
#### Відповіді прикріпити до репозиторію в текстовому форматі.
1. Що таке лінійні трансформації? *(0,25 бала)*
2. Як і в яких галузях застосовуються лінійні трансформації? *(0,25 бала)*
3. Що таке матриця лінійної трансформації та як її можна інтерпретувати? *(0,25 бала)*
4. Які особливості та властивості має матриця обертання? *(0,25 бала)*
5. Чи залежить фінальний результат від порядку трансформацій? Провести експерименти з фігурами або зображеннями з частин 1-2.  *(0,25 бала)*
6. Була здійснена якась довільна лінійна трансформація; як знайти матрицю лінійної трансформації, що поверне все до початкового вигляду? Чи завжди можна здійснити обернену трансформацію? *(0,25 бала)*
7. Модуль визначника матриці трансформації менше 1, які висновки можна зробити про дану трансформацію (як змінюється простір при даній трансформації)? А якщо більше 1? Дорівнює 1? Дорівнює 0? *(0,5 бала)*

### Оцінювання
  - Перша частина - 4 бали
  - Друга частина - 2 бали
  - Перша частина "захист" - 3 бали
  - Друга частина "захист" - 1 бал
  - Теоретичні запитання - 2 бали


















