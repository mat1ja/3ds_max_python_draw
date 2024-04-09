# 3ds Max furniture modeling
Currently, it is possible to draw two furniture models with just one click. The models are shown in the images below.

## UI screenshots

I also added the possibility to create furniture through a UI interface.

![User interface 1](/screenshot/ui_1.jpg)
![User interface 1](/screenshot/ui_2.jpg)
![User interface 1](/screenshot/ui_4.jpg)

## Furniture type 1

```
locker = locker_type_1()
locker.set_dimensions(80,50,150)
locker.set_thickness(3.6)
locker.set_plinth_height(5)
locker.set_number_of_doors(2)
locker.set_mapping(150,150,150)
locker.draw()
```

![Furniture type 1](/screenshot/Screenshot_2.jpg)


## Furniture open shelf

```
locker = open_shelf()
locker.set_dimensions(50,30,80)
locker.set_thickness(3.6)
locker.set_mapping(150,150,150)
locker.draw()
```

![Furniture open shelf](/screenshot/Screenshot_1.jpg)
![Furniture open shelf](/screenshot/open_shelf_1.jpg)
