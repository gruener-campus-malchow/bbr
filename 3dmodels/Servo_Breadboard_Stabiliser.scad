$fn=200;

difference(){
    cube([5,60+4,22+4],true);
    cube([11,60,22],true);   
}

scale([1,1.4,0.6])rotate([0,90,0])difference(){
    cylinder(5,d=60+4, center=true);
    cylinder(11,d=60, center=true);
}    