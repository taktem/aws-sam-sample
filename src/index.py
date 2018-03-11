# -*- coding: utf-8 -*-

import json

def respond(err, res=None):
    return {
        'statusCode': '400' if err else '200',
        'body': err.message if err else json.dumps(res, sort_keys=True, ensure_ascii=False, indent=2),
        'headers': {
            'Content-Type': 'application/json',
        },
    }

def lambda_handler(event, context):
    return respond(err = '', res = event)
