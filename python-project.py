
# A program to analyse the iris data set of Fisher
# by James Ward, April 2018

# We import numpy and matplotlib to calculate the mean, maximum, minimum and standard deviation  
# of each column in the data set. Graphical analysis is also provided in the form of histograms for
# each column of data. This can be used throughout the entire program.
import numpy
import matplotlib.pyplot as pl


# We import the data in from iris.csv file. We then calculate statistics for the first column
data=numpy.genfromtxt('data/iris.csv', delimiter=',')
firstcol=data[:,0]
meanfirstcol=numpy.mean(data[:,0])
minfirstcol=numpy.min(firstcol)
maxfirstcol=numpy.max(firstcol)
standarddev=numpy.std(firstcol)
print("mean of first column is : ", meanfirstcol)
print("min of first column is : ", minfirstcol)
print("max of first column is : ", maxfirstcol)
print("standard deviation of first column is : ", standarddev)

# This sets the parameters for the histogram window for Column 1
fig = pl.figure()
fig.suptitle('Column 1', fontsize=20)
pl.ylabel('Frequency Range', fontsize=18)
pl.xlabel('Values', fontsize=16)
pl.hist(firstcol)
pl.show()

# We calculate the statistics for Column 2
secondcol=data[:,1]
meansecondcol=numpy.mean(data[:,1])
minsecondcol=numpy.min(secondcol)
maxsecondcol=numpy.max(secondcol)
standarddev=numpy.std(secondcol)
print("mean of second column is : ", meansecondcol)
print("min of second column is : ", minsecondcol)
print("max of second column is : ", maxsecondcol)
print("standard deviation of second column is : ", standarddev)

# This sets the parameters for the histogram window for Column 2
fig = pl.figure()
fig.suptitle('Column 2', fontsize=20)
pl.ylabel('Frequency Range', fontsize=18)
pl.xlabel('Values', fontsize=16)
pl.hist(secondcol)
pl.show()

# We calculate the statistics for Column 3
thirdcol=data[:,2]
meanthirdcol=numpy.mean(data[:,2])
minthirdcol=numpy.min(thirdcol)
maxthirdcol=numpy.max(thirdcol)
standarddev=numpy.std(thirdcol)
print("mean of third column is : ", meanthirdcol)
print("min of third column is : ", minthirdcol)
print("max of third column is : ", maxthirdcol)
print("standard deviation of third column is : ", standarddev)

# This sets the parameters for the histogram window for Column 3
fig = pl.figure()
fig.suptitle('Column 3', fontsize=20)
pl.ylabel('Frequency Range', fontsize=18)
pl.xlabel('Values', fontsize=16)
pl.hist(thirdcol)
pl.show()

# We calculate the statistics for Column 4
fourthcol=data[:,3]
meanfourthcol=numpy.mean(data[:,3])
minfourthcol=numpy.min(fourthcol)
maxfourthcol=numpy.max(fourthcol)
standarddev=numpy.std(fourthcol)
print("mean of fourth column is : ", meanfourthcol)
print("min of fourth column is : ", minfourthcol)
print("max of fourth column is : ", maxfourthcol)
print("standard deviation of fourth column is : ", standarddev)

# This sets the parameters for the histogram window for Column 4
fig = pl.figure()
fig.suptitle('Column 4', fontsize=20)
pl.ylabel('Frequency Range', fontsize=18)
pl.xlabel('Values', fontsize=16)
pl.hist(fourthcol)
pl.show()