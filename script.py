# -*- coding: utf-8 -*-
from actiapi.v3 import ActiGraphClientV3

API_ACCESS_KEY="QlvD0k8Pi1VysTjkAnFSL6dyQi3oTdqq"
API_SECRET_KEY="o4CtKZRSqrEi36six2+08przBGfIHkAYauFDqHmN4yI6s5UGP3aBMVl+qw2aWN/u"

def main():
    api_client = ActiGraphClientV3(API_ACCESS_KEY, API_SECRET_KEY)
    results = api_client.get_study_metadata(993)
    return results


results_list = main()
print(results_list)
