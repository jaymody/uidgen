Generate "unique" identifiers of the form `adjective-noun-number`.

**Usage**

```
pip install uidgen
```

Then in python:
```python
>>> import uidgen
>>> uidgen.generate()
spotless-leave-6
>>> uidgen.generate()
wet-diamond-0
>>> uidgen.generate()
dull-court-2
```

Or via CLI:

```
$ python -m uidgen
wild-sport-8
```

**How "unique" are these IDs?**

The total number of possible identifiers is:

```python
>>> from uidgen.data import adjectives, nouns
>>> len(adjectives) * len(nouns) * 10
19996990
```

That's roughly 20 million. The `uidgen.generate()` function samples an ID uniformly from these possibilities. So, if you call `uidgen.generate()` a total of `N` times, the probability that all `N` ID are unique is:

```python
>>> import math
>>> total = len(adjectives) * len(nouns) * 10
>>> for N in [10, 100, 1000, 10000, 100000]:
>>>     print(N, math.prod(total-i for i in range(N)) / total**N)
10 0.9999977496634996
100 0.9997524929700011
1000 0.9753302225997922
10000 0.08204043013318953
100000 1.696918121141932e-109
```

The takeaway: If you're generating under a 200 ID, its very unlikely you'll see a collision. Beyond 200 ID, you're really risking a collision.

So what's the use of this package? Other ID specifications such as `uuid4` have much stronger probabilistic guarantees, however imagine naming a training run of a deep learning model "d986a320-46e1-477e-8b0c-0f53352a8025". It doesn't exactly roll of the tongue when you're in a meeting discussing the takeways from comparing various different runs. You really need something that's easy to say, is memorable, and is unique. This is why [wandb.ai](https://wandb.ai/site) uses this technique to name training runs by default.

You should NOT use this library if:

1) You're application cannot handle name collisions (i.e. the application cannot detect collisions and regenerate a new name).
2) You need to generate a lot of IDs (more than 10000), in which case, even if you regenerate on a collision, you'll be waiting a while until you get a unique ID.
