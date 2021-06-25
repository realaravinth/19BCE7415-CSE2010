# Lab1

- Name: Aravinth TM
- Registration Number: 19BCE7415

## Script

```bash
#!/bin/sh

export ROLL=19BCE7415SS

mkdir -p 0/1/2/3/

for i in {00..10}
do
	touch $ROLL$i
	touch 0/$ROLL$i
	touch 0/1/$ROLL$i
	touch 0/1/2/$ROLL$i
	touch 0/1/2/3/$ROLL$i
done

rm *.docx
rm *SS*

tree

```

## Output

```bash
.
└── 0
    ├── 1
    │   ├── 19BCE7415SS00
    │   ├── 19BCE7415SS01
    │   ├── 19BCE7415SS02
    │   ├── 19BCE7415SS03
    │   ├── 19BCE7415SS04
    │   ├── 19BCE7415SS05
    │   ├── 19BCE7415SS06
    │   ├── 19BCE7415SS07
    │   ├── 19BCE7415SS08
    │   ├── 19BCE7415SS09
    │   ├── 19BCE7415SS10
    │   └── 2
    │       ├── 19BCE7415SS00
    │       ├── 19BCE7415SS01
    │       ├── 19BCE7415SS02
    │       ├── 19BCE7415SS03
    │       ├── 19BCE7415SS04
    │       ├── 19BCE7415SS05
    │       ├── 19BCE7415SS06
    │       ├── 19BCE7415SS07
    │       ├── 19BCE7415SS08
    │       ├── 19BCE7415SS09
    │       ├── 19BCE7415SS10
    │       └── 3
    │           ├── 19BCE7415SS00
    │           ├── 19BCE7415SS01
    │           ├── 19BCE7415SS02
    │           ├── 19BCE7415SS03
    │           ├── 19BCE7415SS04
    │           ├── 19BCE7415SS05
    │           ├── 19BCE7415SS06
    │           ├── 19BCE7415SS07
    │           ├── 19BCE7415SS08
    │           ├── 19BCE7415SS09
    │           └── 19BCE7415SS10
    ├── 19BCE7415SS00
    ├── 19BCE7415SS01
    ├── 19BCE7415SS02
    ├── 19BCE7415SS03
    ├── 19BCE7415SS04
    ├── 19BCE7415SS05
    ├── 19BCE7415SS06
    ├── 19BCE7415SS07
    ├── 19BCE7415SS08
    ├── 19BCE7415SS09
    └── 19BCE7415SS10
```
