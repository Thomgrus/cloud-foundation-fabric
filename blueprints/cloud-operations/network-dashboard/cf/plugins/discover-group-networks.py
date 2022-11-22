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

import itertools
import logging

from . import Level, Resource, register_init, register_discovery

LOGGER = logging.getLogger('net-dash.discovery.compute-routes-dynamic')
NAME = 'networks:project'


@register_init
def init(resources):
  LOGGER.info('init')
  if NAME not in resources:
    resources[NAME] = {}


@register_discovery(Level.DERIVED)
def start_discovery(resources, response=None):
  LOGGER.info(f'discovery (has response: {response is not None})')
  grouped = itertools.groupby(resources['networks'].values(),
                              lambda v: v['project_id'])
  for project_id, vpcs in grouped:
    yield Resource(NAME, project_id, [v['self_link'] for v in vpcs])