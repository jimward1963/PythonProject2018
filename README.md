# PythonProject2018

## Introduction

This project contains a basic statistical analysis of the [Fisher iris data set](https://en.wikipedia.org/wiki/Iris_flower_data_set).

![A photograph of Ronald Fisher](Fischer.jpg)

This is a set of measurements of the sepal lengths and widths, and petal lengths and widths of irises, collected by the statistician Ronald Fisher in 1936. This is a multivariate data set introduced by Fisher in his 1936 paper 'The use of multiple measurements in taxonomic problems'.
A Python program was developed to analyse the data in the set.

### Background to data

The data set consists of 50 samples from each of 3 species of Iris (Iris setosa, Iris virginica and Iris versicolor).
Four features were measured from each sample: the lengths and widths of the petals and sepals, in centimetres.
Based on the combination of these 4 features, Fisher developed a linear discriminant model to distinguish the species from each other.

## What the Program does

Column 1 is Sepal length, column 2 is Sepal width, column 3 is Petal length and column 4 is Petal width.
The program carries out a statistical analysis of these columns.
The python program developed calculates the mean, maximum value, minimun value and standard deviation of each of the 4 columns.
It also provides graphical information in the form of 4 histograms of the measured features. The vertical axes show the Frequency ranges, while the horizontal axes show the Values.
The Python package numpy was imported into the program to calculate the statistics for the 4 columns.
The package matplotlib was imported to generate the histogram charts. A reference is provided of a method of assigning labels on the axes of the histogram charts and chart titles.

### To run the program

To run the program in Visual Studio Code, simply type 'python python-project.py' at the command prompt in the Integrated Terminal.

## Results

For columns 1 to 4 of the data set, it gives the mean, minimum, maximum and the standard deviation, and produces a histogram chart for each column.

## Summary/Conclusions

From a viewing of the histograms, it appears the features measured are within certain limits, but the values are not uniform and do not conform to any common distribution.


## References

[Iris Data](https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data)

[Python Tutorial](https://docs.python.org/3/tutorial/)

Patrick S. Hoey [Statistical Analysis of the Iris Dataset](http://patrickhoey.com/downloads/Computer_Science/03_Patrick_Hoey_Data_Visualization_Dataset_paper.pdf)

https://stackoverflow.com/questions/12444716/how-do-i-set-the-figure-title-and-axes-labels-font-size-in-matplotlib

https://docs.scipy.org/doc/numpy-1.13.0/reference/generated/numpy.std.html
