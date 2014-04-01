#include <math.h>
#include <stdio.h>
#include <stdlib.h>

#define M_PI 3.141592653589793238464
//Casey Gilray
//12/1/2013
//adapted from RK4 solver made in Class

void RK4(int N, double t, double h, const double X[],
	 void (*F)(double t, const double X[], double R[]),
	 double R[])//method taken from RK4 solver made in class
{
  double K1[N];
  F(t,X,K1);

  double T[N], K2[N];
  for (int i = 0; i < N; i++)
    T[i] = X[i] + h/2*K1[i];
  F(t+h/2,T,K2);

  double K3[N];
  for (int i = 0; i < N; i++)
    T[i] = X[i] + h/2*K2[i];
  F(t+h/2,T,K3);

  double K4[N];
  for (int i = 0; i < N; i++)
    T[i] = X[i] + h*K3[i];
  F(t+h,T,K4);

  for (int i = 0; i < N; i++)
    R[i] = X[i] + h/6*(K1[i] + 2*(K2[i] + K3[i]) + K4[i]);
	
}

void Fbaseball(double t, const double X[], double R[])
{
	const double k = 0.002;
	const double g = 32.0;
	double radical = sqrt((X[1]*X[1])+(X[3]*X[3]));
	R[0] = X[1];
	R[1] = -k*X[1]*radical;
	R[2] = X[3];
	R[3] = -k*X[3]*radical - g;
}
void Fplanet(double t, const double X[], double R[])
{
	const double M = 1.9891e30;//mass of sun
	const double m = 3.3022e23;//mass of murc
	const double G = 6.67e-11;//gravitation const
	double r = sqrt(X[0]*X[0]+X[2]*X[2]);//radical x2y2
	double F = (m*M*G)/(r*r);
	double Fx = F*X[0]/r;
	double Fy = F*X[2]/r;
	R[0] = X[1];
	R[1] = -Fx/m;
	R[2] = X[3];
	R[3] = -Fy/m;



}
void F(double t, const double X[], double R[])
{
	R[0] = X[0];
	R[1]= t*X[0];
}

int main()
{
	//change this var to change which solver to use
	//1 = baseball 2=planet 3=equation
	int selecter = 3;
	if (selecter == 1)
	{
		//Baseball (Similar to example in class)
		double t = 0.0;
		double end = 6.5;
 		double h = end/100;
  		double v = 208.0;
  		double theta = 43*M_PI/180;
  		double X[4];
  		X[0] = 0.0; X[1] = v*cos(theta);
  		X[2] = 3.0; X[3] = v*sin(theta);
  		for (t = 0.0; t <= end; t += h) {
  		  printf("%0.10f %0.10f\n", X[0], X[2]);
  		  RK4(4, t, h, X, Fbaseball, X);
  		}
  		return 0;		
	}
	else if (selecter == 2)
	{
		//planet (Similar to example in class)
		double t = 0.0;
 		double h = 100.0;
  		double X[4];
  		X[0] = 46001200000.0;
	 	X[1] = 0.0; 
  		X[2] = 0.0; 
		X[3] = 58980.0; 
  		for (; t <= 7.60052e6; t += h) {
		printf("%0.10f %0.10f\n", X[0], X[2]);
  		  RK4(4, t, h, X, Fplanet, X);
  		}
  		return 0;		
	}
	else
	{
		//Baseball (Similar to example in class)
		double t = 0.0;
		double end = 4.5;
 		double h = 0.01;
  		double X[2];
  		X[0] = 0.355028053887817; X[1] = -0.258819403792807;
  		for (; t <= end; t += h) {
  		  printf("%0.10f\n", X[0]);
  		  RK4(4, t, h, X, F, X);
  		}
  		return 0;	
	}
}
