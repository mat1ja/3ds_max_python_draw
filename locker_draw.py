import sys 
import pymxs
from pymxs import runtime as rt

class my_box:	
    chamfer = False
    length_up_gerung_orientation = 0
    length_down_gerung_orientation = 0
    orientation_top = 0
    orientation_left = 0
    orientation_back = 0
    position = [0,0,0]
    mapping = [250,250,250]

    def set_orientation_top(self, length = False):
        self.orientation_left = 0
        self.orientation_back = 0
        if length == True:
            self.orientation_top = 1
        else:
            self.orientation_top = -1

    def set_orientation_left(self, length = False):
        self.orientation_top = 0
        self.orientation_back = 0
        if length == True:
            self.orientation_left = 1
        else:
            self.orientation_left = -1

    def set_orientation_back(self, length = False):
        self.orientation_top = 0
        self.orientation_left = 0
        if length == True:
            self.orientation_back = 1
        else:
            self.orientation_back = -1

    def add_basic_modifiers(self, object):
        my_modifier = pymxs.runtime.smooth()
        pymxs.runtime.addmodifier(object, my_modifier)

        my_modifier = pymxs.runtime.Quadify_Mesh()
        my_modifier.quadsize = 100
        pymxs.runtime.addmodifier(object, my_modifier)

        my_modifier = pymxs.runtime.Edit_Poly()
        pymxs.runtime.addmodifier(object, my_modifier)

    def set_mapping(self, x,y,z):
        self.mapping = [x,y,z]

    def add_edit_poly(self, object):
        my_modifier = pymxs.runtime.Edit_Poly()
        pymxs.runtime.addmodifier(object, my_modifier)

    def set_position(self, x,y,z):
        self.position = [x,y,z]

    def add_mapping_to_object(self, object):
        my_modifier = pymxs.runtime.Uvwmap()
        my_modifier.length = self.mapping[0]
        my_modifier.width = self.mapping[1]
        my_modifier.height = self.mapping[2]
        my_modifier.axis = 0
        my_modifier.maptype = 4
        pymxs.runtime.addmodifier(object, my_modifier)

    def add_chamfer_to_object(self, object):
        my_modifier = pymxs.runtime.chamfer()
        my_modifier.amount = 0.2
        my_modifier.segments = 5
        my_modifier.tension = 0.5
        my_modifier.SmoothType = 1
        pymxs.runtime.addmodifier(object, my_modifier)

    def add_chamfer(self, state = True):
        self.chamfer = state

    def length_gerung(self, up, down):
        self.length_up_gerung_orientation = up
        self.length_down_gerung_orientation = down

    def make_box(self, length, width, height):
        point_1 = [-length / 2, width / 2, -height / 2]
        point_2 = [length / 2, width / 2, -height / 2]
        point_3 = [-length / 2, -width / 2, -height / 2]
        point_4 = [length / 2, -width / 2, -height / 2]
        point_5 = [-length / 2, width / 2, height / 2]
        point_6 = [length / 2, width / 2, height / 2]
        point_7 = [-length / 2, -width / 2, height / 2]
        point_8 = [length / 2, -width / 2, height / 2]

        if self.length_up_gerung_orientation != 0:
            if self.length_up_gerung_orientation == -1:
                point_4[0] = point_4[0] - height
                point_2[0] = point_2[0] - height

            else:
                point_8[0] = point_8[0] - height
                point_6[0] = point_6[0] - height
                
        if self.length_down_gerung_orientation != 0:
            if self.length_down_gerung_orientation == -1:
                point_3[0] = point_3[0] + height
                point_1[0] = point_1[0] + height
            else:
                point_7[0] = point_7[0] + height
                point_5[0] = point_5[0] + height
                
        box = rt.mesh(
            vertices=[
                rt.point3(point_1[0],point_1[1],point_1[2]),
                rt.point3(point_2[0],point_2[1],point_2[2]),
                rt.point3(point_3[0],point_3[1],point_3[2]),
                rt.point3(point_4[0],point_4[1],point_4[2]),
                rt.point3(point_5[0],point_5[1],point_5[2]),
                rt.point3(point_6[0],point_6[1],point_6[2]),
                rt.point3(point_7[0],point_7[1],point_7[2]),
                rt.point3(point_8[0],point_8[1],point_8[2]),
            ],
            faces=[
                rt.point3(1, 2, 3),
                rt.point3(3,2,4),
                rt.point3(4,2,8),
                rt.point3(2,6,8),
                rt.point3(2,1,6),
                rt.point3(1,5,6),
                rt.point3(1,3,7),
                rt.point3(7,5,1),
                rt.point3(3,4,8),
                rt.point3(8,7,3),
                rt.point3(7,8,6),
                rt.point3(6,5,7)
            ]
        )

        self.add_basic_modifiers(box)

        rt.convertToPoly(box)

        self.add_edit_poly(box)
        
        box.WireColor = rt.color( 242, 220, 202)
                
        if self.chamfer == True:
            self.add_chamfer_to_object(box)
            
        self.add_mapping_to_object(box)
        
        if self.orientation_top != 0:
            if self.orientation_top == -1:
                box.rotation = rt.EulerAngles(0,0,0) #pod dozina
            else:
                box.rotation = rt.EulerAngles(0,0,90) #pod dubina
           
        if self.orientation_back != 0:
            if self.orientation_back == -1:
                box.rotation = rt.EulerAngles(90,0,90) #ledja duzina
            else:
                box.rotation = rt.EulerAngles(90,0,0) #ledja visina

        if self.orientation_left != 0:
            if self.orientation_left == -1:
                box.rotation = rt.EulerAngles(0,90,0) #bocnica visina
            else:
                box.rotation = rt.EulerAngles(0,90,90) #bocnica dubina
                
        box.position= rt.Point3(self.position[0],self.position[1],self.position[2])		
        
        return box

class open_shelv:
    width = 50
    length = 100
    height = 110
    thickness = 3.6
    thickness_back = 1.8
    
    bocnica_ljeva_obj = my_box()
    bocnica_desna_obj = my_box()
    strop_obj = my_box()
    pod_obj = my_box()
    ledja_obj = my_box()

    def set_mapping(self, x,y,z):
        self.mapping = [x,y,z]
            
    def set_dimensions(self,length, width, height):
        self.width = width
        self.length = length
        self.height = height
        
    def set_thickness(self, thickness):
        self.thickness = thickness
    
    def draw(self):
        self.bocnica_ljeva()
        self.bocnica_desna()  
        self.strop()
        self.pod()
        self.ledja()
        
    def bocnica_ljeva(self):
        object = self.bocnica_ljeva_obj
        object.set_orientation_left()
        object.add_chamfer(True)
        object.length_gerung(-1,-1)
        object.set_mapping(self.mapping[0],self.mapping[1],self.mapping[2])
        
        x = - self.length / 2 + self.thickness / 2
        y = 0
        z = self.height / 2
        
        object.set_position(x,y,z)
        
        object.make_box(self.height, self.width, self.thickness)
        
    def bocnica_desna(self):
        object = self.bocnica_desna_obj
        object.set_orientation_left()
        object.add_chamfer(True)
        object.length_gerung(1,1)
        object.set_mapping(self.mapping[0],self.mapping[1],self.mapping[2])

        x = self.length / 2 - self.thickness / 2
        y = 0
        z = self.height / 2

        object.set_position(x,y,z)
        object.make_box(self.height, self.width, self.thickness)
      
    
    def ledja(self):
        object = self.ledja_obj
        object.add_chamfer(False)
        object.set_mapping(self.mapping[0],self.mapping[1],self.mapping[2])
        
        height = self.height - 2*self.thickness
        width = self.length - 2 * self.thickness
        
        if height >= width:
            object.set_orientation_back()
            z = height / 2 + self.thickness
        else:
            object.set_orientation_back(True)
            tmp = height
            height = width
            width = tmp
            z = width / 2 + self.thickness
            
        x = 0
        
        y = self.width / 2 - self.thickness_back /2        
        object.set_position(x,y,z)
        
        object.make_box(height, width, self.thickness_back)
    
    def strop(self):
        object = self.strop_obj
        object.set_orientation_top()
        object.add_chamfer(True)
        object.length_gerung(-1,-1)
        object.set_mapping(self.mapping[0],self.mapping[1],self.mapping[2])
        
        x = 0
        y = 0
        z = self.height - self.thickness / 2
        
        object.set_position(x,0,z)
        
        object.make_box(self.length, self.width, self.thickness)
        
    def pod(self):
        object = self.pod_obj
        object.set_orientation_top()
        object.add_chamfer(True)
        object.length_gerung(1,1)
        object.set_mapping(self.mapping[0],self.mapping[1],self.mapping[2])
        
        x = 0
        y = 0
        z = self.thickness / 2
        
        object.set_position(x,0,z)
        
        object.make_box(self.length, self.width, self.thickness)
    
    




class locker_type_1:
    width = 50
    length = 100
    height = 110
    cokl_height = 3
    thickness = 1.8
    thickness_border = 3.6
    number_of_doors = 4
    mapping = [250,250,250]

    bocnica_ljeva_obj = my_box()
    bocnica_desna_obj = my_box()
    strop_obj = my_box()
    cokl_obj = my_box()
    ledja_obj = my_box()
    vrata_obj = my_box()
    pod_obj = my_box()

    def set_mapping(self, x,y,z):
        self.mapping = [x,y,z]
        
    def set_thickness(self, value):
        self.thickness_border = value
        
    def set_sokl_height(self, value):
        self.cokl_height = value
        
    def set_number_of_doors(self, value):
        self.number_of_doors = value
    
    def set_dimensions(self,length, width, height):
        self.width = width
        self.length = length
        self.height = height

    def draw(self):
        self.bocnica_ljeva()
        self.bocnica_desna()
        self.strop()
        self.cokl()
        self.ledja()
        self.pod()
        
        for x in range(self.number_of_doors):
            self.vrata(x)

    def pod(self):
        object = self.pod_obj 
        object.add_chamfer(True)
        object.set_mapping(self.mapping[0],self.mapping[1],self.mapping[2])
        
        object.set_position(0,0.1,self.cokl_height + self.thickness / 2)
        object.make_box(self.length - 2 * self.thickness_border, self.width-2*self.thickness - 0.2, self.thickness)
      
    def vrata(self,i):
        object = self.vrata_obj
        number_of_gaps = self.number_of_doors - 1 + 2
        length = (self.length - 2 * self.thickness_border - number_of_gaps * 0.3) / self.number_of_doors
        height = self.height - self.cokl_height - self.thickness_border - 1 * 0.3
        
        object.set_orientation_back()
        object.add_chamfer(True)
        object.set_mapping(self.mapping[0],self.mapping[1],self.mapping[2])
        
        z = height / 2 + self.cokl_height 
        y = - self.width / 2 + self.thickness /2
        x = - self.length / 2 + self.thickness_border + 0.3 + length / 2 + (length + 0.3) * i
        object.set_position(x,y,z)
        object.make_box(height, length, self.thickness)

    def ledja(self):
        object = self.ledja_obj
        object.set_orientation_back()
        object.add_chamfer(False)
        object.set_mapping(self.mapping[0],self.mapping[1],self.mapping[2])
        
        height = self.height - self.thickness_border
        
        x = 0
        z = height / 2
        y = self.width / 2 - self.thickness /2        
        object.set_position(x,y,z)
        
        object.make_box(height, self.length - 2 * self.thickness_border, self.thickness)

    def cokl(self):
        object = self.cokl_obj
        object.set_orientation_back(True)
        object.set_mapping(self.mapping[0],self.mapping[1],self.mapping[2])
        object.add_chamfer(True)
        
        x = 0
        z = self.cokl_height / 2
        y = - self.width / 2 + self.thickness / 2 + 3
        object.set_position(x,y,z)
        
        object.make_box(self.length - 2*self.thickness_border, self.cokl_height, self.thickness)

    def strop(self):
        object = self.strop_obj
        object.set_orientation_top()
        object.add_chamfer(True)
        object.length_gerung(-1,-1)
        object.set_mapping(self.mapping[0],self.mapping[1],self.mapping[2])
        
        x = 0
        y = 0
        z = self.height - self.thickness_border / 2
        
        object.set_position(x,0,z)
        
        object.make_box(self.length, self.width, self.thickness_border)

    def bocnica_ljeva(self):
        object = self.bocnica_ljeva_obj
        object.set_orientation_left()
        object.add_chamfer(True)
        object.length_gerung(-1,0)
        object.set_mapping(self.mapping[0],self.mapping[1],self.mapping[2])
        
        x = - self.length / 2 + self.thickness_border / 2
        y = 0
        z = self.height / 2
        
        object.set_position(x,y,z)
        
        object.make_box(self.height, self.width, self.thickness_border)

    def bocnica_desna(self):
        object = self.bocnica_desna_obj
        object.set_orientation_left()
        object.add_chamfer(True)
        object.length_gerung(1,0)
        object.set_mapping(self.mapping[0],self.mapping[1],self.mapping[2])

        x = self.length / 2 - self.thickness_border / 2
        y = 0
        z = self.height / 2

        object.set_position(x,y,z)
        object.make_box(self.height, self.width, self.thickness_border)




#locker = locker_type_1()
#locker.set_dimensions(150,20,150)
#locker.set_thickness(3.6)
#locker.set_sokl_height(5)
#locker.set_number_of_doors(3)
#locker.set_mapping(150,150,150)
#locker.draw()

locker = open_shelv()
locker.set_dimensions(50,30,80)
locker.set_thickness(3.6)
locker.set_mapping(150,150,150)
locker.draw()
