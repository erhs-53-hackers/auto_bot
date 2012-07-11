#include "ros/ros.h"
#include "auto_bot/SensorData.h"


void callback(const auto_bot::SensorData::ConstPtr& msg)
{
  ROS_INFO("First: [%f] Second: [%f]", msg->sensorData[0].xdata[0], msg->sensorData[0].xdata[1]);
}

int main(int argc, char **argv)
{
 
  ros::init(argc, argv, "localizer");
  
  ros::NodeHandle n;  
  
  ros::Subscriber sub = n.subscribe("SensorData", 1000, callback);
  
  ros::spin();

  return 0;
}
