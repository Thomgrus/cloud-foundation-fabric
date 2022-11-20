# Notes

- [x] get projects
  `get_monitored_projects_list`
- [ ] set monitoring interval
  `monitoring_interval`
- [ ] read metrics and limits from yaml and create descriptors
  `metrics.create_metrics`
- [x] get project quota
  `limits.get_quota_project_limit`
- [x] get firewall rules from CAI
  `vpc_firewalls.get_firewalls_dict`
- [x] get firewall policies from CAI
  `firewall_policies.get_firewall_policies_dict`
- [x] get instances
  `instances.get_gce_instance_dict`
- [x] get forwarding rules for L4 ILB
  `ilb_fwrules.get_forwarding_rules_dict`
- [x] get forwarding rules for L7 ILB
  `ilb_fwrules.get_forwarding_rules_dict`
- [x] get subnets and secondary ranges
  `networks.get_subnet_ranges_dict`
- [x] get static routes
  `routes.get_static_routes_dict`
- [x] get dynamic routes
  routes.get_dynamic_routes
  - get routers
    `routers.get_routers`
  - get networks
    `networks.get_networks`
  - get router status
    `get_routes_for_network`
    `get_routes_for_router`
- [ ] get and store subnet metrics
  `subnets.get_subnets`
  - get subnets
    `get_all_subnets`
  - calculate subnet utilization
    `compute_subnet_utilization`
    - get instances
      `compute_subnet_utilization_vms`
    - get forwarding rules
      `compute_subnet_utilization_ilbs`
    - get addresses
      `compute_subnet_utilization_addresses`
    - get redis instances
      `compute_subnet_utilization_redis`
  - store metrics
- [ ]calculate and store firewall rule metrics
  `vpc_firewalls.get_firewalls_data`
- [ ] calculate and store firewall policy metrics
  `firewall_policies.get_firewal_policies_data`
- [ ] calculate and store instance per network metrics
  `instances.get_gce_instances_data`
- [ ] calculate and store L4 forwarding rule metrics
  `ilb_fwrules.get_forwarding_rules_data`
- [ ] calculate and store L7 forwarding rule metrics
  `ilb_fwrules.get_forwarding_rules_data`
- [ ] calculate and store static routes metrics
  `routes.get_static_routes_data`
- [ ] calculate and store peering metrics
  `peerings.get_vpc_peering_data`
- [ ] calculate and store peering group metrics
  `metrics.get_pgg_data`
  `routes.get_routes_ppg`
- [ ] write buffered timeseries
  `metrics.flush_series_buffer`


## Inputs

direct inputs

- organization id
- folders (monitored)
- projects (monitored)

derived inputs

- projects in folders via CAI
- networks
- subnets
- routers
- peerings
- quotas
- firewall rules
- firewall policies
- routes
- routers
- dynamic routes
- peerings
- instances

resources

- project quota
- firewall rules in org via CAI
  - key: network
- firewall policies in org via CAI
  - key: network
- networks in org via CAI
- subnets in org via CAI
  - key: project, network?
  - computed metrics: ip usage (used, total, utilization)
  - computed metrics: secondary IP ranges
- instances
  - key: network
  - computed metrics: instance per network (usage, limit, utilization)
- forwarding rules in org via CAI
  - key: network, type
  - computed metrics: fwd rule per network per type (usage, limit, utilization)
- static routes in org via CAI
  - computed metrics: routes per project (usage, limit, utilization)
- dynamic routes via routers
  - computed metrics: routes per project (usage, limit, utilization)



## Resources and data

- projects
  - quotas


## Metrics


## Clients

- compute
- asset inventory
- momnitoring
