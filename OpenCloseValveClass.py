#!/usr/bin/python
# -*- coding: utf-8 -*-
from ds1820class import Write_temp
import time
import datetime as dt


def Documentation(state):
    with open('valve', 'a+') as f:
        f.write(state)


class OpenCloseValve(object):
    'A class that controls a valve with a close and a open signal'
    def __init__(self):
        self.deadband = 2.0
        self.Time_Open = 3.0  # Seconds the valve shall open
        self.Time_Close = 2.0  # Seconds the valve shall close
        self.Man_Open = False
        self.Man_Close = False
        self.Man_Close_OUT = False
        self.Man_Open_OUT = False
        #Declar instances for logging
        self.Write_Stat_Open = Write_temp(self.Man_Open, 'VS1_SV1_Open')
        self.Write_Stat_Close = Write_temp(self.Man_Close, 'VS1_SV1_Close')

        self.Control_Time = 0
        self.Control_Active = False

    def main(self, PV, SP):
        '''In this method the temperatures
        are compared, and some control variables
        are set for later activaion of the IO
        '''
        self.deltaT = SP - PV
        if self.deadband < self.deltaT:
            'If deltaT is bigger than the deadband, open valve and Heat'
            #Open
            self.Control_Active = True
            self.Man_Open = True
            self.Man_Close = False

        elif self.deltaT > 0 - self.deadband:
            '''If deltaT is less than 0 minus deadband,
            close valve and Dont heat'''
            #close
            self.Control_Active = True
            self.Man_Close = True
            self.Man_Open = False

        else:
            'If none is true, do nothing'
            self.Control_Active = False
            self.Man_Close = False
            self.Man_Open = False

    def control(self):
        '''Here the IO are controlled
        based on the control variables from
        main method
        '''
        if self.Control_Active:
            self.Control_Time = time.time()

            if self.Man_Close:
                if self.Control_Time + self.Time_Close < time.time():
                    self.Man_Close_OUT = True
                    Documentation('Close ' + str(dt.datetime.now()) + ' \n')

                    #Close variable
            else:
                self.Man_Close_OUT = False
                self.Control_Active = False
                Documentation('Close stopped ' + str(dt.datetime.now()) + ' \n')

            if self.Man_Open:
                if self.Control_Time + self.Time_Open < time.time():
                    self.Man_Open_OUT = True
                    #Open variable
                    Documentation('Open ' + str(dt.datetime.now()) + ' \n')
            else:
                self.Man_Open_OUT = False
                self.Control_Active = False
                Documentation('Open stopped ' + str(dt.datetime.now()) + ' \n')

