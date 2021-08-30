#include <GL/glew.h>
#include <GL/freeglut.h>
#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include<math.h>

using namespace std;

// Function to initialize the drivers
void myInit(void)
{
    // Clear all the screen color
    glClearColor(0.0, 0.0, 0.0, 0.0);

    // Sets background color to black
    glMatrixMode(GL_PROJECTION);

    glLoadIdentity();

    // Specify the display area
    gluOrtho2D(0.0, 400.0, 0.0, 400.0);
}


void myDisplay(void)
{
    // Clear the screen buffer
    glClear(GL_COLOR_BUFFER_BIT);

    glPointSize(4.0);

    // Rectangular part of car
    glColor3f(1.0f, 1.0f, 1.0f);

    // Begin the polygon
    glBegin(GL_POLYGON);

    // Create the polygon
    glVertex2i(100, 100);
    glVertex2i(300, 100);

    glVertex2i(100, 150);
    glVertex2i(300, 150);

    glVertex2i(100, 150);
    glVertex2i(100, 100);

    glVertex2i(300, 150);
    glVertex2i(300, 100);

    glEnd();

     // top part of car
    glColor3f(1.0f, 0.0f, 1.0f);

    // Begin the polygon
    glBegin(GL_POLYGON);

    // Create the polygon
    glVertex2i(140,150);
    glVertex2i(170,220);
    glVertex2i(250,220);
    glVertex2i(300,150);
    glVertex2i(250,220);
    glVertex2i(275,185);
   // glVertex2i(300,220);

    glEnd();

    //window of car
    glColor3f(1.0f, 1.0f, 0.0f);

    // Begin the polygon
    glBegin(GL_POLYGON);

    // Create the polygon
    glVertex2i(145,155);
    glVertex2i(172,215);

    glVertex2i(200,215);
    glVertex2i(200,155);


    glEnd();

    //window of car
    glColor3f(1.0f, 1.0f, 0.0f);

    // Begin the polygon
    glBegin(GL_POLYGON);

    // Create the polygon
    glVertex2i(210,155);
    glVertex2i(210,215);

    glVertex2i(250,215);
    glVertex2i(290,155);


    glEnd();

    glColor3f(1.0f, 0.0f, 0.0f);

    //wheel
    glBegin(GL_POLYGON);
    for(int i=0;i<360;i++)
    {
      float theta=i*3.14/180;
      glVertex2f(150+30*cos(theta),100+30*sin(theta));
    }
    glEnd();


    glColor3f(1.0f, 0.0f, 0.0f);

    //wheel
    glBegin(GL_POLYGON);
    for(int i=0;i<360;i++)
    {
      float theta=i*3.14/180;
      glVertex2f(250+30*cos(theta),100+30*sin(theta));
    }
    glEnd();


    // Sends all output to display
    glFlush();
}

// Driver Code
int main(int argc, char** argv)
{
    // Initialize the init function
    glutInit(&argc, argv);

    // Initialize the toolkit;
    glutInitDisplayMode(
        GLUT_SINGLE | GLUT_RGB);

    // Sets the display mode and
    // specify the colour scheme
    glutInitWindowSize(500, 800);

    // Specify the window size
    glutInitWindowPosition(0, 0);

    // Sets the starting position
    // for the window
    glutCreateWindow("car");

    // Creates the window and
    // sets the title
    glutDisplayFunc(myDisplay);
    myInit();

    // Additional initializations
    glutMainLoop();

    // Go into a loop until event
    // occurs
    return 0;
}
