#!/usr/bin/perl

open F, '<', "coursesbyFaculty.txt";
open G, '>', "cleanCourses.txt";
while ($line = <F>){
    print G $line if !($line =~ /http|\d+|GET/);
}
close F;
close G;