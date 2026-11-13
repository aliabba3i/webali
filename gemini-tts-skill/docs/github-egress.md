# GitHub Actions egress IP: what is and is not static

## Short answer

A normal GitHub-hosted Actions runner does **not** have one fixed outbound IP. Its public egress address can change between jobs. GitHub publishes the current Actions address ranges through the `GET /meta` API, and that list is updated periodically; it is not a single permanent address.

GitHub documents static public IP ranges only for eligible **GitHub-hosted larger runners**. The documented requirements currently specify GitHub Enterprise Cloud, and macOS larger runners do not support this feature. Organization owners configure the feature in the organization's runner settings. The assigned value is a range/pool, not a personal static IP for a laptop.

Official documentation:
- https://docs.github.com/en/actions/reference/runners/larger-runners
- https://docs.github.com/en/actions/how-tos/manage-runners/larger-runners/manage-larger-runners
- https://docs.github.com/en/actions/reference/runners/github-hosted-runners

## Important distinction for this project

A static egress range on a GitHub Actions runner only applies to network requests made **from jobs running on that runner**. It does not change the public IP of the user's Windows/Linux computer or their normal browser session.

This project does not turn GitHub Actions into a general-purpose VPN, HTTP/SOCKS proxy, or traffic relay. It must not route AI Studio browser traffic through GitHub to disguise the user's location or bypass Google's regional eligibility, account, CAPTCHA, quota, or security controls.

## Supported use cases

- Run repository tests and diagnostic scripts in GitHub Actions.
- Inspect the runner's network environment for ordinary CI troubleshooting.
- If an organization legitimately needs a stable source IP for an allowlist, an owner can evaluate GitHub Enterprise Cloud larger runners with static IP ranges and configure the allowlist for a service they administer.
- A self-hosted runner can use a static IP supplied by its hosting provider or network administrator; the owner is responsible for its security and maintenance.

## Not supported / not promised

- A fixed IP on standard GitHub-hosted runners.
- A fixed IP just because a workflow runs from a GitHub repository.
- Changing the user's local public IP by running a GitHub workflow.
- Using GitHub runner IP ranges as a consumer VPN or proxy.
- Guaranteeing that Google AI Studio will accept a request based on its source IP or that an IP change resolves account/region eligibility.

## Recommended path

1. Run the local diagnostic scripts first.
2. If a stable public IP is required for a legitimate allowlist, ask the ISP or hosting provider for a dedicated static egress IP.
3. If the organization already has GitHub Enterprise Cloud, ask its owner to verify larger-runner availability and static-IP configuration in the organization settings.
4. Treat Google AI Studio region/account messages as eligibility issues, not as DNS or IP stability problems. Use Google's supported availability and account options.

Never store GitHub tokens, Google credentials, browser cookies, or browser profiles in the repository or workflow logs.
