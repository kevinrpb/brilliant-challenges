---
title: "How To Climb Out Of A Gravity Well"
description: "2019-04-06"
date: 2019-04-06
challenge_url: https://brilliant.org/daily-problems/falcon-heavy-4/
---

We learn from the challenge that the total energy of a body is constant and equal to the sum of its kinetic and potential energies. From here, it is easy to solve for the speed needed to maintain said energy (just as explained in the post). Said need speed is `v = sqrt( 2GM/r_LEO - 2GM/(r_LEO + r_dest) )` where:

* `G` is the gravitational constant (`G ~= 6.674 * 10^-11`)
* `M` is the mass of the Earth)
* `GM` product is given [in a previous challenge](https://brilliant.org/daily-problems/falcon-heavy-2/) as `GM = 4 * 10^14 m^3/s^2`, which is `GM = 4 * 10^5 km^3/s^2`
* `r_LEO` is the radius in LEO (`6,700 + 400 km`)
* `r_dest` is the radius of destination (`6,700 + 35,000 km`)

Doing some algebra in our initial equation, we get `v = sqrt( 2GM * [1/r_LEO - 1/(r_LEO + r_dest)] )`. This yields `v ~= 10 km/s`. Since in LEO the shuttle already has `7.6 km/s` speed, the needed delta is of about `3 km/s`.
