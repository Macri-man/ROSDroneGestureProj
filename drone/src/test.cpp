#include <ros/ros.h>
#include <nodelet/nodelet.h>
#include <stdio.h>
#include <string>
#include <cv_bridge/cv_bridge.h>
#include <opencv2/core/core.hpp>
#include <opencv2/imgcodecs.hpp>
#include <opencv2/highgui/highgui.hpp>

using namespace std;
using namespace cv;

int main(int argc, char** argv )
{


     ros::init(argc, argv, "test");
     string imageName("test.jpg");
    if ( argc >1 ){
        //printf("usage: test.out <Image_Path>\n");
        //ROS_ERROR("usage: test.out <Image_Path>: \n");
        imageName = argv[1];
    }

    Mat image;

    //cv_bridge::CvImageConstPtr cv_ptr;
    image = imread( imageName.c_str(), 1 );



    if ( !image.data )
    {
        printf("No image data \n");
        ROS_ERROR("No image data \n");
        return -1;
    }


    //cv_ptr->image=image;
    namedWindow("Display Image", WINDOW_AUTOSIZE );
    imshow("Display Image",image);

    waitKey(0);


    ros::spin();
    return 0;
}


