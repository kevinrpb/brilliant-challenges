---
title: "Octopus Shuffle"
description: "2019-04-06"
date: 2019-04-06
challenge_url: https://brilliant.org/daily-problems/octopus-shuffle/
---

What we get from the challenge explanation is that each shuffle, each card 'doubles' its position (because we are doing a 2-stack shuffle), `modulo X` where `X` is the one less than the size of the deck (in this case the deck size is `8`, therefore `X = 7`). This means that:

* A card in position `0` stays in `0`
* A card in position `1` goes to `2 = 2 mod 7`
* A card in position `2` goes to `4 = 4 mod 7`
* A card in position `3` goes to `6 = 6 mod 7`
* A card in position `4` goes to `1 = 8 mod 7`
* A card in position `5` goes to `3 = 10 mod 7`
* A card in position `6` goes to `4 = 12 mod 7`
* A card in position `7` stays in `7`

Now, for the challenge we are using a 12-card deck. This means `X = 11`. We are also doing 3-stack shuffles, which means each position gets 'tripled'. Using the same logic as before:

* A card in position `0` stays in `0`
* A card in position `1` goes to `3 = 3 mod 11`
* A card in position `2` goes to `6 = 6 mod 11`
* A card in position `3` goes to `9 = 9 mod 11`
* A card in position `4` goes to `1 = 12 mod 11`
* A card in position `5` goes to `4 = 15 mod 11`
* A card in position `6` goes to `7 = 18 mod 11`
* A card in position `7` goes to `10 = 21 mod 11`
* A card in position `8` goes to `2 = 24 mod 11`
* A card in position `9` goes to `5 = 27 mod 11`
* A card in position `10` goes to `8 = 30 mod 11`
* A card in position `11` stays in `11`

We can now follow the changes of a card, lets say, that in position `1`. Changes in position would be

1. From `1` to `3`
2. From `3` to `9`
3. From `9` to `5`
4. From `5` to `4`
5. From `4` to `1`

After the `fifth` shuffle it gets back to position number `1`.
