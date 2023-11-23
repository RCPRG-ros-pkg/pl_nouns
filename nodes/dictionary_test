#!/usr/bin/env python3

import rclpy
from pl_nouns.dictionary_client import DictionaryServiceClient

def main(args=None):
    rclpy.init(args=args)

    # Initialize the DictionaryServiceClient
    dictionary_client = DictionaryServiceClient()

    words = ['kuchnia', 'łazienka', 'fotel', 'spodnie', 'drzwi', 'szczoteczka',
             'pis', 'wośp', 'wrak', 'petrografia', 'petrografie', 'figlarze']

    for w in words:
        print(f'Using dictionary for word "{w}"')
        for case in ['mianownik', 'celownik', 'dopelniacz', 'biernik']:
            # Assuming getCases() is an asynchronous call returning a future
            future = dictionary_client.getCases(w)
            rclpy.spin_until_future_complete(dictionary_client, future)
            result = future.result().getCase(case)
            print(f'    {case}: {result}')

    rclpy.shutdown()

if __name__ == '__main__':
    main()
