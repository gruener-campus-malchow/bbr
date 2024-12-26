$fn=100;
distance=20;

module battery_holder(){
   
    translate([+distance/2,0,0])cube([2,150,5],true);
    translate([-distance/2,0,0])cube([2,150,5],true);

    
    difference()
    {
        translate([0,150/2,0])cube([50,2,5],true);
        union()
            {
                translate([20,150/2,1])rotate([90,0,0])cylinder(5,d=1.5,center=true);
                translate([22,150/2,1])rotate([90,0,0])cylinder(5,d=1.5,center=true);
                translate([20,150/2,-1])rotate([90,0,0])cylinder(5,d=1.5,center=true);
                translate([22,150/2,-1])rotate([90,0,0])cylinder(5,d=1.5,center=true);
                
                translate([-20,150/2,1])rotate([90,0,0])cylinder(5,d=1.5,center=true);
                translate([-22,150/2,1])rotate([90,0,0])cylinder(5,d=1.5,center=true);
                translate([-20,150/2,-1])rotate([90,0,0])cylinder(5,d=1.5,center=true);
                translate([-22,150/2,-1])rotate([90,0,0])cylinder(5,d=1.5,center=true);
                
            }
        
    }
}

translate([0,150/2-5,-2])cube([50,distance/2,1],true);

battery_holder();
translate([0,20,-2])stabilisator(distance);
translate([0,-20,-2])stabilisator(distance);
translate([0,-20-40,-2])stabilisator(distance);

translate([0,0,-2.5])linear_extrude(10)projection([0,0,1]){translate([0,-150/2+0,distance/2-2.5])scale([1.5,1,1])sphere(distance/2);}
translate([0,-150/2+0,distance/2-2.5])scale([1.5,1,1])sphere(distance/2);



module stabilisator(length){
    cube([length,1,1],true);
    translate([0,distance,0])cube([length,1,1],true);
    diagonal=sqrt(length^2 + length^2);
    translate([0,distance/2,0])rotate([0,0,45])cube([diagonal,1,1],true);
    translate([0,distance/2,0])rotate([0,0,-45])cube([diagonal,1,1],true);
}

