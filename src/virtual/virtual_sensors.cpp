//<ros>
#include "ros/ros.h"
#include "auto_bot/SensorData.h"
//</ros>
//<octomap>
#include <octomap/octomap.h>
#include <octomap/OcTree.h>
//</octomap>
//<std>
#include <sstream>
//</std>

using namespace std;
using namespace octomap;





int main(int argc, char **argv) {
  
  ros::init(argc, argv, "virtual_sensors");  
  ros::NodeHandle n;
 
  ros::Publisher sensors_pub = n.advertise<auto_bot::SensorData>("SensorData", 1000);
  
  ros::Rate loop_rate(10);
  
  OcTree map("/home/michael/ros_workspace/auto_bot/bin/map.bt");
  
  point3d start(0, 0, 0);
  point3d end(100, 10, 0);
  vector<point3d> points;
  
  map.computeRay(start, end, points);
  for(int i=0;i<points.size();i++) {
  	point3d p = points[i];
  	ROS_INFO("[%i]coord = [%f, %f, %f]", i, p.x(), p.y(), p.z());
  }
  

  /*
  int count = 0;
  while (ros::ok()) {
  	auto_bot::SensorData msg;
  	auto_bot::Xdata xdata;
  	
  	for(int y=0;y<480;y++) {
  		auto_bot::Xdata xdata;
  		for(int i=0;i<640;i++) {
  			xdata.xdata[i] = (float)i;
  		}
  		msg.sensorData[y] = xdata;
  	}
  	sensors_pub.publish(msg);
  	ros::spinOnce();
  	ROS_INFO("Sent data");

    loop_rate.sleep();
    ++count;
    
  }*/


  return 0;
}
