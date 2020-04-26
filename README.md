<<<<<<< HEAD
# polynomial_regression
A series of functions for polynomial regression. This project is still in progress.

## Least Squares
Least squares regression produces the line of best fit which minimizes the square of the vertical offsets of each datapoint (their variance). The least squares equation is as follows:
![least squares equation](least_squares.png)

The equations for variance and covariance can be substituted into this equation to produce:
m = covariance/variance and c = y_mean - m * x_mean
This is the equation that was implemented in [main.py](main.py).

More information about the equation can be found [in this MIT lecture.](https://www.youtube.com/watch?v=YwZYSTQs-Hk) The derivation of the formula through minimizing the variance equation can be found [here.](https://docs.google.com/document/d/1vXgizn0Zz5VM_mTEfrRqwydfCyn0OY5DNlkieFLRU68/edit?usp=sharing)

### Example
Here is an example of linear least squares using the data set found in [main.py](main.py):  
![example least squares linear regression](iv_curve.png)

## To Do:
- [x] Variance
- [x] Covariance
- [x] Least Squares Regression
- [ ] Polynomial matrix regression
=======
# Polynomial Regression

## Least Squares Linear Regression
Least squares linear regression is a method of calculating the line of best fit which has the smallest total variance to each point.

The line of best fit has the equation: y = mx + b
The distance to the line of best fit f()
>>>>>>> 6f690d222130785f16dc0008e3aab25a1dc3bc3f
