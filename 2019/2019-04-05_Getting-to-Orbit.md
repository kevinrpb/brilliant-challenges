# [2019-04-05] Getting To Orbit

[Home](../README.md)
[Original Posting](https://brilliant.org/daily-problems/falcon-heavy-3/)

We start with the next info:

* Mass when fully loaded is `1500 tonnes`
* Mass of the rocket shell is `100 tonnes`
* Required speed for orbit is `7.2 km/s`
* Rocket combustion speed is `3.2 km/s`

The speed (`Δv`) the rocket can gain after spelling all fuel is given by `Δv = u * ln(M_i / M_f)` where

* `u`: Rocket combustion speed
* `M_i`: Mass of the rocket fully fueled
* `M_f`: Mass of the rocket "empty"

Since the rocket shell mass is 100 tonnes, we are looking for `X = M_f - 100`

Using the equation given for the increment in speed

* `Δv / u = ln(M_i / M_f)`
* `e ^ (Δv / u) = M_i / M_f`
* `M_f = M_i / (e ^ (Δv / u))`

Finally,

* `X = (M_i / (e ^ (Δv / u))) - 100`

Solution is `58.09883684279649` ~ `60 tonnes`
