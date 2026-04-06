---
title: "Tailscale: automatic connection in the office"
url: https://perrotta.dev/2026/03/tailscale-automatic-connection-in-the-office/
last_updated: 2026-03-18
---


**TIL**: [Tailscale](https://tailscale.com/) (a zero-trust VPN) supports
automatically connecting to it on select Wi-Fi networks.

**Use case**: whenever you go to your work office, automatically turn the VPN
on.

On macOS: Settings > Settings > VPN On Demand.
Then, on Wi-Fi, select "Only On" and add the desired SSID ('MyHomeWiFi').

Screenshot for iOS, which is equivalent to the macOS dialog:

![iOS screenshot](https://tailscale.com/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fvpn-on-demand.a0126dd5.png&w=640&q=75)

[Docs: VPN On Demand](https://tailscale.com/docs/features/client/ios-vpn-on-demand).

