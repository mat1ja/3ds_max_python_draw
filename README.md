# 3ds Max furniture modeling
Currently, it is possible to draw two furniture models with just one click. The models are shown in the images below.

## Furniture type 1

```
locker = locker_type_1()
locker.set_dimensions(150,20,150)
locker.set_thickness(3.6)
locker.set_sokl_height(5)
locker.set_number_of_doors(3)
locker.set_mapping(150,150,150)
locker.draw()
```

![Furniture type 1](/screenshot/Screenshot_2.jpg)


## Furniture open shelf

```
locker = open_shelv()
locker.set_dimensions(50,30,80)
locker.set_thickness(3.6)
locker.set_mapping(150,150,150)
locker.draw()
```

![Furniture open shelf](/screenshot/Screenshot_1.jpg)
