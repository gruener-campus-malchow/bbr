$fn=100;

$diameter=25;

//axe
difference()
{
    union(){
        cylinder(4,d=7);
        for (i = [0:60:300]) {
            rotate([0,0,i])cube([($diameter/2)-1,1,4]);

        }
    }
    union(){
        translate([0,0,-1])cylinder(10,d=2.5);
        translate([0,0,2])cylinder(6,d=4.8);
    }
}

//wheel
difference(){
    cylinder(8,d=$diameter);
    translate([0,0,-1])cylinder(12,d=$diameter-2);
}

