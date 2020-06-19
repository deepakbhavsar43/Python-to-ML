#### The below commands can be used with Inbuilt and Custom algorithm.

##### Training the model
To train the model use "-tr" or  "-\-train" in cmd as shown below:
```
>python filename.py -tr
```
##### Testing the model
To test the model use "-te" or "-\-test" in cmd as shown below:
```
>python filename.py -te
```
##### To predict label
To make prediction use "-pr" or "-\-predict".
It also requires input data:
- "-sl" or "-\-sepallength" -> length of sepal
- "-sw" or "-\-sepalwidth" -> width of sepal
- "-pl" or "-\-petallength" -> length of petal
- "-pw" or "-\-petalwidth" -> width of petal

This input data can be given from cmd as shown below
```
>python Inbuilt.py -pr -sl 6.1 -sw 3.3 -pl 5.5 -pw 3.3
```