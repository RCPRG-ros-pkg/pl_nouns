#!/usr/bin/env python
# encoding: utf8

import sys
import rospy
import tiago_msgs.msg
import tiago_msgs.srv

class Cases:
    def __init__(self, resp):
        assert isinstance (resp, tiago_msgs.srv.DictionaryQueryResponse)
        self.__resp__ = resp

    def getCase(self, case_name):
        for idx, cn in enumerate(self.__resp__.case_names):
            if cn == case_name:
                case_inst = self.__resp__.variants[0]
                return case_inst.singular[idx].decode('utf-8')
        raise Exception('Wrong case_name: "' + case_name + '"')

class DisctionaryServiceClient:
    def __init__(self):
        rospy.wait_for_service('/pl_dict_service')
        try:
            self.serv = rospy.ServiceProxy('/pl_dict_service', tiago_msgs.srv.DictionaryQuery)
        except rospy.ServiceException, e:
            print "Service call failed: %s"%e

    def getCases(self, word):
        req = tiago_msgs.srv.DictionaryQueryRequest()
        req.word = word.encode('utf-8')
        resp1 = self.serv(req)
        return Cases( resp1 )
