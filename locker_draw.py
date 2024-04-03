import sys 
import pymxs
from pymxs import runtime as rt

class my_box:	

    chamfer = False
    length_up_gerung_orientation = 0
    length_down_gerung_orientation = 0
    orientation_z = 0
    orientation_y = 0
    orientation_x = 0
    position = [0,0,0]
    
    def set_z_orientation(self, angle):
        self.orientation_z = angle
        
    def set_y_orientation(self, angle):
        self.orientation_y = angle
        
    def set_x_orientation(self, angle):
        self.orientation_x = angle
    
    def add_basic_modifiers(self, object):
        my_modifier = pymxs.runtime.smooth()
        pymxs.runtime.addmodifier(object, my_modifier)

        my_modifier = pymxs.runtime.Quadify_Mesh()
        my_modifier.quadsize = 100
        pymxs.runtime.addmodifier(object, my_modifier)

        my_modifier = pymxs.runtime.Edit_Poly()
        pymxs.runtime.addmodifier(object, my_modifier)


    def add_edit_poly(self, object):
        my_modifier = pymxs.runtime.Edit_Poly()
        pymxs.runtime.addmodifier(object, my_modifier)
     
    def set_position(self, x,y,z):
        self.position = [x,y,z]
        
    def add_mapping_to_object(self, object):
        my_modifier = pymxs.runtime.Uvwmap()
        my_modifier.length = 250
        my_modifier.width = 250
        my_modifier.height = 250
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
        
        box.rotation = rt.EulerAngles( self.orientation_y, self.orientation_z, self.orientation_x)
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
        object.set_z_orientation(90)
        object.add_chamfer(True)
        object.length_gerung(-1,-1)
        
        x = - self.length / 2 + self.thickness / 2
        y = 0
        z = self.height / 2
        
        object.set_position(x,y,z)
        
        object.make_box(self.height, self.width, self.thickness)
        
    def bocnica_desna(self):
        object = self.bocnica_desna_obj
        object.set_z_orientation(90)
        object.add_chamfer(True)
        object.length_gerung(1,1)

        x = self.length / 2 - self.thickness / 2
        y = 0
        z = self.height / 2

        object.set_position(x,y,z)
        object.make_box(self.height, self.width, self.thickness)
      
    
    def ledja(self):
        object = self.ledja_obj
        object.set_y_orientation(90)
        object.set_x_orientation(90)
        object.add_chamfer(False)
        
        height = self.height - 2*self.thickness
        
        x = 0
        z = height / 2 + self.thickness
        y = self.width / 2 - self.thickness_back /2        
        object.set_position(x,y,z)
        
        object.make_box(height, self.length - 2 * self.thickness, self.thickness_back)
    
    def strop(self):
        object = self.strop_obj
        object.set_z_orientation(0)
        object.add_chamfer(True)
        object.length_gerung(-1,-1)
        
        x = 0
        y = 0
        z = self.height - self.thickness / 2
        
        object.set_position(x,0,z)
        
        object.make_box(self.length, self.width, self.thickness)
        
    def pod(self):
        object = self.pod_obj
        object.set_z_orientation(0)
        object.add_chamfer(True)
        object.length_gerung(1,1)
        
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
    number_of_doors = 4
    
    bocnica_ljeva_obj = my_box()
    bocnica_desna_obj = my_box()
    strop_obj = my_box()
    cokl_obj = my_box()
    ledja_obj = my_box()
    vrata_obj = my_box()
    pod_obj = my_box()
    
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
        
        object.set_position(0,0.1,self.cokl_height + self.thickness / 2)
        object.make_box(self.length - 2 * self.thickness, self.width-2*self.thickness - 0.2, self.thickness)
      
    def vrata(self,i):
        object = self.vrata_obj
        number_of_gaps = self.number_of_doors - 1 + 2
        length = (self.length - 2 * self.thickness - number_of_gaps * 0.3) / self.number_of_doors
        height = self.height - self.cokl_height - self.thickness - 1 * 0.3
        
        object.set_y_orientation(90)
        object.set_x_orientation(90)
        
        object.add_chamfer(True)
        
        z = height / 2 + self.cokl_height 
        y = - self.width / 2 + self.thickness /2
        x = - self.length / 2 + self.thickness + 0.3 + length / 2 + (length + 0.3) * i
        object.set_position(x,y,z)
        object.make_box(height, length, self.thickness)
        
    def ledja(self):
        object = self.ledja_obj
        object.set_y_orientation(90)
        object.set_x_orientation(90)
        object.add_chamfer(False)
        
        height = self.height - self.thickness
        
        x = 0
        z = height / 2
        y = self.width / 2 - self.thickness /2        
        object.set_position(x,y,z)
        
        object.make_box(height, self.length - 2 * self.thickness, self.thickness)
      
    def cokl(self):
        object = self.cokl_obj
        object.set_z_orientation(0)
        object.set_y_orientation(90)
        
        object.add_chamfer(True)
        
        x = 0
        z = self.cokl_height / 2
        y = - self.width / 2 + self.thickness / 2 + 3
        object.set_position(x,y,z)
        
        object.make_box(self.length - 2*self.thickness, self.cokl_height, self.thickness)


    def strop(self):
        object = self.strop_obj
        object.set_z_orientation(0)
        object.add_chamfer(True)
        object.length_gerung(-1,-1)
        
        x = 0
        y = 0
        z = self.height - self.thickness / 2
        
        object.set_position(x,0,z)
        
        object.make_box(self.length, self.width, self.thickness)
        
    def bocnica_ljeva(self):
        object = self.bocnica_ljeva_obj
        object.set_z_orientation(90)
        object.add_chamfer(True)
        object.length_gerung(-1,0)
        
        x = - self.length / 2 + self.thickness / 2
        y = 0
        z = self.height / 2
        
        object.set_position(x,y,z)
        
        object.make_box(self.height, self.width, self.thickness)
        
    def bocnica_desna(self):
        object = self.bocnica_desna_obj
        object.set_z_orientation(90)
        object.add_chamfer(True)
        object.length_gerung(1,0)

        x = self.length / 2 - self.thickness / 2
        y = 0
        z = self.height / 2

        object.set_position(x,y,z)
        object.make_box(self.height, self.width, self.thickness)


#locker = locker_type_1()
#locker.set_dimensions(150,20,150)
#locker.draw()

locker = open_shelv()
locker.set_dimensions(50,30,50)
locker.set_thickness(1.8)
locker.draw()
