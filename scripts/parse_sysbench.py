#!/usr/bin/env python3
"""
Sysbench Output Parser & Hypervisor Performance Comparator
Calculates percentage differences between Type-1 (Proxmox VE) and Type-2 (VMware Workstation) hypervisors.
"""

def compare_hypervisors():
    proxmox = {
        "hypervisor": "Proxmox VE (Type-1)",
        "eps": 1719.03,
        "total_time": 10.0012,
        "total_events": 17195,
        "min_lat": 0.56,
        "avg_lat": 0.59,
        "max_lat": 2.82,
        "p95_lat": 0.68,
    }

    vmware = {
        "hypervisor": "VMware Workstation (Type-2)",
        "eps": 268.48,
        "total_time": 10.0006,
        "total_events": 2687,
        "min_lat": 3.13,
        "avg_lat": 3.71,
        "max_lat": 9.82,
        "p95_lat": 4.49,
    }

    eps_diff = ((proxmox["eps"] - vmware["eps"]) / vmware["eps"]) * 100
    events_diff = proxmox["total_events"] - vmware["total_events"]
    avg_lat_diff = ((vmware["avg_lat"] - proxmox["avg_lat"]) / vmware["avg_lat"]) * 100
    p95_lat_diff = ((vmware["p95_lat"] - proxmox["p95_lat"]) / vmware["p95_lat"]) * 100

    print("===================================================================================")
    print("      HYPERVISOR CPU PERFORMANCE COMPARISON: TYPE-1 VS TYPE-2                      ")
    print("===================================================================================")
    print(f"Metric                         Proxmox VE (Type-1)   VMware (Type-2)     Difference")
    print("-----------------------------------------------------------------------------------")
    print(f"Throughput (Events/sec)        {proxmox['eps']:<20.2f} {vmware['eps']:<18.2f} +{eps_diff:.2f}% (Proxmox faster)")
    print(f"Total Events (10s)             {proxmox['total_events']:<20} {vmware['total_events']:<18} +{events_diff} events")
    print(f"Minimum Latency (ms)           {proxmox['min_lat']:<20.2f} {vmware['min_lat']:<18.2f} Proxmox {vmware['min_lat']-proxmox['min_lat']:.2f}ms lower")
    print(f"Average Latency (ms)           {proxmox['avg_lat']:<20.2f} {vmware['avg_lat']:<18.2f} Proxmox {avg_lat_diff:.2f}% lower")
    print(f"95th Percentile Latency (ms)   {proxmox['p95_lat']:<20.2f} {vmware['p95_lat']:<18.2f} Proxmox {p95_lat_diff:.2f}% lower")
    print(f"Maximum Latency (ms)           {proxmox['max_lat']:<20.2f} {vmware['max_lat']:<18.2f} Proxmox {vmware['max_lat']-proxmox['max_lat']:.2f}ms lower")
    print("===================================================================================")

if __name__ == "__main__":
    compare_hypervisors()
