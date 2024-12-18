$fn=50;

sensor_hull();

module sensor_hull(){
    difference(){
        cube([31,27,10], true);
        cube([29,25,12], true);
    }
    difference()
    {
        translate([0,0,1])cube([8,8,8], true);
        cube([7,7,12], true);
      
    }
    
    difference(){
        union(){        
            translate([30/2-5,13,5-2])cube([5,6,2]);
            translate([30/2-11,-2.5,5-2])cube([11,1,2]);
            
            translate([-30/2,13,5-2])cube([5,6,2]);
            translate([-30/2,-2.5,5-2])cube([11,1,2]);
        }
        union()
        {
            translate([13.5,15.5,5])rotate([0,0,0])cylinder(5,d=1.5,center=true);
            translate([11.5,15.5,5])rotate([0,0,0])cylinder(5,d=1.5,center=true);
            translate([13.5,17.5,5])rotate([0,0,0])cylinder(5,d=1.5,center=true);
            translate([11.5,17.5,5])rotate([0,0,0])cylinder(5,d=1.5,center=true);
            
            translate([-13.5,15.5,5])rotate([0,0,0])cylinder(5,d=1.5,center=true);
            translate([-11.5,15.5,5])rotate([0,0,0])cylinder(5,d=1.5,center=true);
            translate([-13.5,17.5,5])rotate([0,0,0])cylinder(5,d=1.5,center=true);
            translate([-11.5,17.5,5])rotate([0,0,0])cylinder(5,d=1.5,center=true);
        }
    }
    

    
    

}