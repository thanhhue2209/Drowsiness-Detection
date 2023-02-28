# Drowsiness-Detection

Stage 01:
In the first phase, we took the input and used face landmark 468 to select two diagonal points to crop the two eyes image. Then, feed into the Xception model that predicts eye-opening and closing-eyes

Stage 02:
In the second stage we create a queue with a length of five. Then we sum the queue if the sum is zero we will give the output as dangerous and warn the driver, otherwise if the sum is non-zero we will give the output as safe.
![image](https://user-images.githubusercontent.com/74448277/221800639-5ce33fe2-bbd3-426a-8dc9-08980c487e5a.png)

Result:
Model predicts eye-opening and closing-eyes:

![image](https://user-images.githubusercontent.com/74448277/221800718-ac046ba7-8de3-42bd-92c7-3233d49c629b.png)


