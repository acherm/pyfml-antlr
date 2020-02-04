# pyfml-antlr

prototyping a feature modeling language with Python support

based on https://github.com/FAMILIAR-project/familiar-language/blob/master/org.xtext.example.fml.parent/org.xtext.example.fml/src/org/xtext/example/mydsl/Fml.xtext#L550
and https://github.com/jszheng/py3antlr4book

basic setup instructions
```
pip install antlr4-python3-runtime=4.7.2
# goto https://www.antlr.org/download.html 
# download the latest ver
wget https://www.antlr.org/download/antlr-4.7.2-complete.jar
ln -s antlr-4.7.2-complete.jar antlr.jar
module load ./antlr4module
```

```
[mathieuacher@localhost fml]$ antlr4py3 fml.g4 
[mathieuacher@localhost pyfml-antlr]$ cd fml/
[mathieuacher@localhost fml]$ python test_fml.py foo.fml
(featuremodel FM ( (production a : (child (mandatory b)) (child (optional [ c ])) (child (mandatory d))) ; (production c : (child (xorgroup ( e | f )))) ; (production d : (child (orgroup ( H | JJ | KKKK ) +))) ; (production K : (child (mutexgroup ( Z | Y )?))) ; (production Y : (child (optional [ OOOoooo12 ]))) ; (constraints (constraints Z) -> (constraints H)) ; (constraints (constraints e) & (constraints ( (constraints (constraints JJ) -> (constraints KKKK)) ))) ; ))
```
