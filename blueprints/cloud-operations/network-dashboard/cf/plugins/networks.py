# Copyright 2022 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import logging
import urllib.parse

from . import *
from .utils import parse_cai_page_token, parse_cai_results

LEVEL = Level.PRIMARY
NAME = 'networks'
TYPE = 'compute.googleapis.com/Network'

CAI_URL = ('https://content-cloudasset.googleapis.com/v1p1beta1'
           '/{}/resources:searchAll'
           f'?assetTypes={urllib.parse.quote(TYPE)}&pageSize=500')


@register(NAME, Phase.INIT, Step.START)
def init(resources):
  if 'networks' not in resources:
    resources['networks'] = {}


@register(NAME, Phase.DISCOVERY, Step.START, LEVEL, 0)
def start_discovery(resources):
  org_id = resources['organization']['id']
  yield CAI_URL.format(f'organizations/{org_id}')


@register(NAME, Phase.DISCOVERY, Step.END)
def end_discovery(resources, data, url):
  for result in parse_cai_results(NAME, TYPE, data):
    name = result['displayName']
    project_number = result['project'].split('/')[1]
    project_id = resources['projects:number'].get(project_number)
    if not project_id:
      logging.info(f'skipping network {name} in {project_number}')
      continue
    resources['networks'][f'{project_id}/{name}'] = {
        'name': name,
        'project_id': project_id,
        'project_number': project_number
    }
  return parse_cai_page_token(url, data)


@register(NAME, Phase.COLLECTION, Step.START, LEVEL, 0)
def start_collection(resources):
  return


@register(NAME, Phase.COLLECTION, Step.END)
def end_collection(resources, metrics, data):
  return
