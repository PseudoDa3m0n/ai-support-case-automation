# Nessus SSH Connectivity Troubleshooting Case

## Purpose

This support case documents a home-lab troubleshooting scenario where SSH connectivity from a Windows host to an Ubuntu VM initially failed during preparation for a Nessus credentialed scan.

## Issue Summary

A Nessus credentialed scan required SSH access to an Ubuntu VM. The Ubuntu VM was reachable from the Windows host by ping, and the SSH service was active and listening on port 22. However, Windows could not connect to SSH on port 22.

The issue was traced to conflicting UFW firewall rules on Ubuntu. The firewall had both deny and allow rules for SSH. After removing the deny rules, SSH connectivity worked and the Nessus credentialed scan completed successfully with authentication passing.

## Environment

- Host machine: Windows PC
- Virtualization platform: VMware Workstation Pro
- Scanner: Tenable Nessus Essentials installed on Windows
- Target system: Ubuntu VM
- Target IP address: 192.168.138.130
- Windows VMnet8 IP address: 192.168.138.1
- Network mode: NAT
- SSH account: nessuslab
- SSH port: 22

## Symptoms

- Ubuntu SSH service was active/running.
- Ubuntu was listening on port 22.
- Windows could ping Ubuntu successfully.
- Windows Test-NetConnection to port 22 returned False.
- SSH login from Windows failed before the firewall fix.
- Nessus could not use SSH credentials until connectivity was corrected.

## Troubleshooting Performed

1. Verified the Ubuntu VM IP address.
2. Verified the Windows VMnet8 IP address.
3. Confirmed both systems were on the same NAT network.
4. Confirmed Windows could ping the Ubuntu VM.
5. Confirmed SSH was active and listening on Ubuntu.
6. Tested port 22 from Windows.
7. Confirmed port 22 connectivity failed.
8. Checked Ubuntu UFW firewall rules.
9. Found conflicting deny and allow rules for SSH/port 22.
10. Removed the deny rules.
11. Confirmed only allow rules remained.
12. Re-tested port 22 from Windows.
13. Confirmed SSH login worked.
14. Ran the Nessus credentialed scan successfully.

## Root Cause

The Ubuntu UFW firewall had conflicting rules for SSH/port 22. Even though allow rules were present, deny rules were also configured and blocked inbound SSH traffic.

## Resolution

Removed the UFW deny rules for SSH/port 22, confirmed SSH allow rules remained, retested port 22 connectivity from Windows, and verified that SSH login worked.

## Validation

The fix was validated by confirming:

- Windows could ping the Ubuntu VM.
- Windows could connect to TCP port 22.
- SSH login from Windows worked.
- The Nessus credentialed scan completed successfully.
- Nessus showed authentication status as Auth: Pass.

## Customer-Facing Response

The issue was caused by firewall rules on the Ubuntu VM that blocked SSH traffic on port 22. Although SSH was running, the firewall had conflicting deny and allow rules. After removing the deny rules and confirming SSH was allowed, the Windows host was able to connect successfully and the Nessus credentialed scan completed with authentication passing.

## Internal Support Notes

The target was reachable at the network layer because ping from Windows to Ubuntu succeeded. SSH was active on Ubuntu, so the issue was isolated to service-level connectivity on TCP port 22. UFW firewall review showed conflicting deny and allow rules for SSH. Removing the deny rules resolved the port connectivity issue and allowed credentialed scanning to complete.

## Knowledge Base Draft

### Title

Nessus Credentialed Scan SSH Connectivity Fails Due to Ubuntu UFW Port 22 Rules

### Applies To

- Nessus Essentials
- Ubuntu VM targets
- VMware Workstation Pro
- SSH credentialed scans
- UFW firewall

### Symptoms

- Scanner can ping the target.
- SSH is running on the target.
- Port 22 test fails.
- SSH login fails.
- Nessus credentialed scan cannot authenticate.

### Cause

Conflicting UFW firewall rules for SSH/port 22 may block SSH traffic even when allow rules are present.

### Resolution

Review UFW rules, remove deny rules for port 22, confirm SSH allow rules, and retest SSH connectivity.

### Verification

The issue is resolved when port 22 is reachable, SSH login works, and Nessus shows Auth: Pass.

## Missing Information

- Exact Ubuntu version
- Exact UFW rule numbers deleted
- Exact SSH restart command used
- Whether SSH password authentication or key-based authentication was used
