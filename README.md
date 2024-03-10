Generate "unique" identifiers of the form `adjective-noun-number`.

**Usage**

```
pip install uidgen
```

Then in python:
```
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

**Note**

Identifiers are not actually "unique". There are a total of ~2 million possible identifiers from which one is randomly sampled (uniformly).
