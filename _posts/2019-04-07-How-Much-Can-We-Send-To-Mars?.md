---
title: "How Much Can We Send To Mars?"
description: "2019-04-07"
date: 2019-04-07
challenge_url: https://brilliant.org/daily-problems/falcon-heavy-5/
---

Let's start with the info provided in the challenge:

| Orbit | Needed $\Delta v$ | Payload Mass |   Takeoff Mass |
| :---- | ----------------: | -----------: | -------------: |
| LEO   |         $9\ km/s$ | $64\ tonnes$ | $1500\ tonnes$ |
| GTO   |      $11.6\ km/s$ | $27\ tonnes$ | $1500\ tonnes$ |
| Mars  |      $12.6\ km/s$ |  $?\ tonnes$ | $4000\ tonnes$ |

And the rocket equation

$$\Delta v = u\ ln\frac{M_i}{M_f}$$

Here, we can solve for $u$ and for $M_f$

$$u = \frac{\Delta v}{ln\frac{M_i}{M_f}}$$

$$M_f = \frac{M_i}{e^{\Delta v / u}}$$

Using this, and taking the values for `LEO` from the table above, we can calculate `$u \approx 2.853\ km/s$`. Plugging the value in the second equation for Mars data, we get that `$M_f \approx 18.11\ tonnes$`
