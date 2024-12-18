$fn=50;


module pi_holder(){

    difference(){
        union(){        
            cube([32,5,2]);
            
            
            translate([28,0,0])cube([5,15,2]);
            translate([10,0,2])cube([2,5,10]);
            translate([10,0,2])cube([22,1,3]);
            //translate([12,0,0])cube([2,5,10]);
        }
        union()
        {
           
            
            translate([32-1.5,12.5,1])cylinder(5,d=2.5,center=true);
            

            //translate([0,1.5,5])rotate([0,90,0])cylinder(5,d=1.5,center=true);
            translate([03,1.5,0])rotate([0,0,0])cylinder(5,d=1.5,center=true);
            //translate([0,1.4,9])rotate([0,90,0])cylinder(5,d=1.5,center=true);

            //translate([0,3.5,5])rotate([0,90,0])cylinder(5,d=1.5,center=true);
            translate([3,3.5,])rotate([0,0,0])cylinder(5,d=1.5,center=true);
            //translate([0,3.5,9])rotate([0,90,0])cylinder(5,d=1.5,center=true);


        }
    }
}    
pi_holder();
//translate([0,-2,0])mirror([0,1,0])sensor_holder();