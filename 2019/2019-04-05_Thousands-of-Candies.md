# [2019-04-05] Thousands of Candies

[Home](../README.md)

[Original Posting](https://brilliant.org/daily-problems/candy-mix/)

* Jar `A` starts with `400 red` candies
* Jar `B` starts with `200 green` candies

First steps

1. Move red candies from `A to B`
2. Move mixed candies from `B to A`

At this point:

* Jar `A` has `X green` and `Y_a red`   candies where X + Y_a = 400
* Jar `B` has `X red`   and `Y_b green` candies where X + Y_b = 200

Next

3. Move mixed candies from A and B to a bowl

We are taking `N` candies from `A` with

* `X/400`       probability of being `green`
* `1 - X/400` probability of being `red`

We are taking `N` candies from `B` with

* `X/200`       probability of being `red`
* `1 - X/200` probability of being `green`

Finally,

4. Randomly select one candy

This candy has `1/2 probability` of coming from either bowl. Therefore, we can draw the next probability tree

```text
                            X/400 -------- green === X/800
                           /
                ---- A ----
               /           \
             1/2            1 - X/400 ----  red  === 1/2 - X/800
            /
 Candy ----
            \
             1/2            X/200 --------  red  === X/400
              \            /
                ---- B ----
                           \
                            1 - X/200 ---- green === 1/2 - X/400
```

This shows that

* `Red`   candies have X/400 + 1/2 - X/800 = `1/2 + X/800 probability`
* `Green` candies have X/800 + 1/2 - X/400 = `1/2 - X/800 probability`

So `red` ones have higher probability
