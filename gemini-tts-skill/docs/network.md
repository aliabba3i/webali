# Network diagnostics and safe configuration

## Definitions
- DNS translates hostnames into IP addresses. It does not change the public IP assigned by the ISP.
- IPv4 and IPv6 are separate protocol families. A host may resolve or connect successfully over one and fail over the other.
- Public egress IP is the address a remote service sees. It may be dynamic.
- A static public IP must be provided by the ISP or a dedicated egress provider.

## Diagnostic order
1. Run the network diagnostics script.
2. Compare IPv4 and IPv6 DNS resolution.
3. Check HTTPS reachability.
4. If only one IP family fails, inspect router and ISP support before changing settings.
5. If DNS fails for both, inspect resolver configuration.
6. If DNS works but HTTPS fails, inspect captive portals, firewall, TLS inspection, router filtering, and ISP connectivity.

## Example public DNS resolvers
- Cloudflare IPv4: 1.1.1.1 and 1.0.0.1
- Cloudflare IPv6: 2606:4700:4700::1111 and 2606:4700:4700::1001
- Google Public DNS IPv4: 8.8.8.8 and 8.8.4.4
- Google Public DNS IPv6: 2001:4860:4860::8888 and 2001:4860:4860::8844

These are examples, not a guarantee of access or eligibility. Choose based on privacy, reliability, and network policy.

## Stable public IP
Ask the ISP whether a static public IPv4 address is available. If a dedicated static-egress VPN is used, evaluate provider trust, privacy, jurisdiction, and applicable service terms. Do not rotate IPs or spoof location to evade access controls.

## Reversibility
Before any DNS or protocol change, record original settings and confirm administrator permission. Change one item at a time and document rollback. The included scripts intentionally make no changes.
