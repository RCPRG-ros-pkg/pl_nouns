#!/usr/bin/env python3

import sys
import rclpy
from rclpy.node import Node
from tiago_msgs.srv import DictionaryQuery

class Cases:
    def __init__(self, resp):
        assert isinstance(resp, DictionaryQuery.Response)
        self.__resp__ = resp

    def getCase(self, case_name):
        for idx, cn in enumerate(self.__resp__.case_names):
            if cn == case_name:
                case_inst = self.__resp__.variants[0]
                return case_inst.singular[idx]
        raise Exception(f'Wrong case_name: "{case_name}"')

class DictionaryServiceClient(Node):
    def __init__(self):
        super().__init__('dictionary_service_client')
        self.cli = self.create_client(DictionaryQuery, '/pl_dict_service')
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available, waiting again...')

    def getCases(self, word):
        req = DictionaryQuery.Request()
        req.word = word
        return self.cli.call_async(req)

def main(args=None):
    rclpy.init(args=args)
    dictionary_service_client = DictionaryServiceClient()
    
    rclpy.shutdown()

if __name__ == '__main__':
    main()
