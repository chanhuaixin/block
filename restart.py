import RobotApi 
import time 
RobotApi.ubtRobotInitialize()
ret=RobotApi.ubtRobotConnect("SDK","1","127.0.0.1")
if(0!=ret):
        print("return value:%d" % ret)
        exit(1)
                
                    
servoAngle=RobotApi.UBTEDU_ROBOTSERVO_T()

servoAngle.SERVO1_ANGLE= 90
servoAngle.SERVO2_ANGLE= 140
servoAngle.SERVO3_ANGLE= 160

# Action : keep right arm straight
servoAngle.SERVO4_ANGLE= 90
servoAngle.SERVO5_ANGLE= 40
servoAngle.SERVO6_ANGLE= 20
servoAngle.SERVO7_ANGLE= 90
servoAngle.SERVO8_ANGLE= 60
servoAngle.SERVO9_ANGLE= 75
servoAngle.SERVO10_ANGLE= 110
servoAngle.SERVO11_ANGLE= 90
servoAngle.SERVO12_ANGLE= 90
servoAngle.SERVO13_ANGLE= 120
servoAngle.SERVO14_ANGLE= 105
servoAngle.SERVO15_ANGLE= 70
servoAngle.SERVO16_ANGLE= 90
RobotApi.ubtSetRobotServo(servoAngle,200)
print("done")
RobotApi.ubtRobotDisconnect("SDK","1","127.0.0.1")
RobotApi.ubtRobotDeinitialize()



