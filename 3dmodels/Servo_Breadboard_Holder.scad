$fn=50;

difference(){
    union(){        
        cube([22,5,2]);
        cube([2,5,10]);
        translate([12,0,0])cube([5,2,5]);
        translate([12,0,0])cube([2,5,10]);
    }
    union(){
       
        
        translate([19,2.5,1])cylinder(5,d=2,center=true);
        

        //translate([0,1.5,5])rotate([0,90,0])cylinder(5,d=1.5,center=true);
        translate([0,1.5,7])rotate([0,90,0])cylinder(5,d=1.5,center=true);
        //translate([0,1.4,9])rotate([0,90,0])cylinder(5,d=1.5,center=true);

        //translate([0,3.5,5])rotate([0,90,0])cylinder(5,d=1.5,center=true);
        translate([0,3.5,7])rotate([0,90,0])cylinder(5,d=1.5,center=true);
        //translate([0,3.5,9])rotate([0,90,0])cylinder(5,d=1.5,center=true);


    }
}
    

