#include "mystuff.h"
#include "data.h"
#include "circle.h"
#include "Utilities.cpp"
#include "CircleFitByTaubin.cpp"
#define _USE_MATH_DEFINES
#include <math.h>
#include <iostream>
#include <cmath>
#include <ctime>
#include <cstdlib>
#include <cstring>
#include <cstdio>
#include <iomanip>
#include <vector>
#include <fstream>
#include <string>
#include <sstream>

using namespace std;

int main()
{
	// output file
	remove("circle_fit_mem.dat");
	ofstream output;
	output.open("circle_fit_mem.dat", ios::app);
	output << fixed;
	output << setprecision(7);
	output << "# time \t\t center_x \t\t center_y \t\t radius \t\t sigma \t\t diameter" << endl;

	// parameters
	string trash;
	int trash_no=9;			// number of unimportant lines in input
	double info1, info2, infotype, infox, infoy, infoz, info7, info8, info9;
	int Ncyto;
	ifstream infile;
 	infile.open("Ncyto.txt");
	infile >> Ncyto;
	infile.close();
	cout << "number of cytoplasm particles = " << Ncyto << endl;
	int bead_no = 47920+1440+Ncyto;		// number of beads in simulation
	int bead_counter;		// counter for beads (from 0 to bead_no-1)
	int line_counter;		// counter for input lines
	double x_threshold=0.5;		// x coordinate threshold
	double y_coord[bead_no];	// y coordinates of membrane particles with an x coordinate within x_threshold
	double z_coord[bead_no];	// z coordinates of membrane particles with an x coordinate within x_threshold
	int time_counter=0;
	bool end=false;
	double circle_center_x=0.;	// center position of circle
	double circle_center_y=0.;	// center position of circle
	double circle_radius=53.;	// radius of circle
	double radius_threshold=1.2;	// threshold for radius growth per timestep to exclude large fluctuations

	while(true){
		// reset
		bead_counter=0;
		line_counter=0;
		for(int i=0; i<bead_no; i++){ y_coord[i]=0.; z_coord[i]=0.; }

		// input
		ifstream input;
		input.open("./output.xyz");
		for(int i=1; i<=trash_no+time_counter*(trash_no+bead_no); i++){ getline(input,trash); }
		while(line_counter<bead_no){
			if(input >> info1 >> info2 >> infotype >> infox >> infoy >> infoz >> info7 >> info8 >> info9){
				if(infotype==1 && infox>-1.*x_threshold && infox<x_threshold){
				// all beads of type 1 (membrane beads) with an x_coord within -x_threshold and +x_threshold are taken into account for fit
				// but only if they are within a circle of radius=radius_threshold*old_circle_radius
					if((((infoy-circle_center_x)*(infoy-circle_center_x))+((infoz-circle_center_y)*(infoz-circle_center_y)))<((radius_threshold*circle_radius)*(radius_threshold*circle_radius))){
						y_coord[bead_counter]=infoy;
						z_coord[bead_counter]=infoz;
						bead_counter++;
					}
				}
			}
			else{ cout << "detected end of file!" << endl; end = true; break;}
			line_counter++;
		}
		input.close();

		// check if end of file is reached
		if(end==true){ break; }

		// fit data
		Data data1(bead_counter-1,y_coord,z_coord);
		Circle circle;
		circle = CircleFitByTaubin (data1);

		circle_center_x = circle.a;
		circle_center_y = circle.b;
		circle_radius = circle.r;

		// output
		output << time_counter << "\t\t" << circle.a << "\t\t" << circle.b << "\t\t" << circle.r << "\t\t" << circle.s << "\t\t" << 2.*circle.r << endl;

		// next time
		time_counter++;
	}
}
