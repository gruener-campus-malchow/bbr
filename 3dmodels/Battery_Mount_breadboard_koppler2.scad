$fn=100;
difference()
    {
        union(){
            translate([0,0,0])cube([5,5,5]);
            translate([0,12.5-5,0])cube([5,5,20]);
        }
        union()
            {
                translate([1.5,0,1.5])rotate([90,0,0])cylinder(50,d=1.5,center=true);
                translate([3.5,0,1.5])rotate([90,0,0])cylinder(50,d=1.5,center=true);
                translate([1.5,0,3.5])rotate([90,0,0])cylinder(50,d=1.5,center=true);
                translate([3.5,0,3.5])rotate([90,0,0])cylinder(50,d=1.5,center=true);               
            }
        
    }

    
translate([0,0,-5])cube([5,12.5,5]);



translate([12.5,7.5,0])rotate([0,0,90])difference()
    {
        union(){
            translate([0,0,5+11])cube([5,12.5,5]);
        }
        union()
            {
                translate([1.5,1.5,0])rotate([0,0,0])cylinder(50,d=1.5,center=true);
                translate([3.5,1.5,0])rotate([0,0,0])cylinder(50,d=1.5,center=true);
                translate([1.5,3.5,0])rotate([0,0,0])cylinder(50,d=1.5,center=true);
                translate([3.5,3.5,0])rotate([0,0,0])cylinder(50,d=1.5,center=true);               
            }
        
    }
    
    