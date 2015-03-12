'''
Created on 2014-12-16

@author: Administrator
'''

#import the monkeyrunner modules used by this program
import sys
from com.android.monkeyrunner import MonkeyRunner
from com.android.monkeyrunner import MonkeyDevice
from com.android.monkeyrunner import MonkeyImage
from com.android.monkeyrunner.easy import EasyMonkeyDevice
from com.android.monkeyrunner.easy import By

#connect to the device
device = MonkeyRunner.waitForConnection()
print 'Test Start'


#install app
device.installPackage("F:/Zhangdan_5.1.00.apk")
print 'Installation is finished'

edevice = EasyMonkeyDevice(device)

#kill the test processing
device.shell('am force-stop com.zhangdan.app')


#start app
device.startActivity(component = "com.zhangdan.app/.activities.SplashActivity")
MonkeyRunner.sleep(3)

#Login
print 'Start logging in'
edevice.touch(By.id('id/ImageView_Enter'),MonkeyDevice.DOWN_AND_UP)
MonkeyRunner.sleep(5)
edevice.touch(By.id('id/Button_OldUser_Login'),MonkeyDevice.DOWN_AND_UP)
MonkeyRunner.sleep(5)
edevice.touch(By.id('id/EditText_UserName'),MonkeyDevice.DOWN_AND_UP)
device.type('51testN1')
MonkeyRunner.sleep(5)
edevice.touch(By.id('id/EditText_Passwd'),MonkeyDevice.DOWN_AND_UP)
device.type('123456')
MonkeyRunner.sleep(1)
edevice.touch(By.id('id/Button_Login'),MonkeyDevice.DOWN_AND_UP)
MonkeyRunner.sleep(2)

#change to Score tab
edevice.touch(By.id('id/RadioButton_Me'),MonkeyDevice.DOWN_AND_UP)
MonkeyRunner.sleep(3)
edevice.touch(By.id('id/TextView_Msg_Item4'),MonkeyDevice.DOWN_AND_UP)
MonkeyRunner.sleep(8)

#back to home screen
device.press('KEYCODE_HOME','DOWN_AND_UP')