
# -*-coding: utf-8 -*-
import RobotApi

def say(speak):

    RobotApi.ubtRobotInitialize()
    ret=RobotApi.ubtRobotConnect("SDK","1","127.0.0.1")
    if(0!=ret):
        print("return value:%d"%ret)
        exit(1)

    RobotApi.ubtVoiceTTS(0,speak)
if __name__ == '__main__':
	say("hello")




    RobotApi.ubtRobotDisconnect("SDK","1","127.0.0.1")
    RobotApi.ubtRobotDeinitialize()
