#!/usr/bin/env python3

import rclpy
from rclpy.node import Node

from tiago_msgs.srv import DictionaryQuery
from tiago_msgs.msg import CaseInstance

import pl_nouns.odmiana as ro

class DictionaryServiceServer(Node):
    def __init__(self):
        super().__init__('pl_dict_service')

        self.get_logger().info('DictionaryServiceServer loading dictionary...')
        self.dictionary = ro.OdmianaRzeczownikow()

        self.get_logger().info('DictionaryServiceServer creating service...')
        self.service = self.create_service(DictionaryQuery, '/pl_dict_service', self.dictionary_query)
        self.get_logger().info('DictionaryServiceServer ready.')

    def dictionary_query(self, request, response):
        word_uni = request.word
        word_m, word_d, word_c, word_b = self.dictionary.przypadki(word_uni)
        
        response.case_names.append('mianownik')
        response.case_names.append('dopelniacz')
        response.case_names.append('celownik')
        response.case_names.append('biernik')

        case_inst = CaseInstance()
        case_inst.singular.append(word_m)
        case_inst.singular.append(word_d)
        case_inst.singular.append(word_c)
        case_inst.singular.append(word_b)
        response.variants.append(case_inst)

        return response

def main(args=None):
    rclpy.init(args=args)
    dictionary_service_server = DictionaryServiceServer()
    rclpy.spin(dictionary_service_server)
    rclpy.shutdown()

if __name__ == '__main__':
    main()