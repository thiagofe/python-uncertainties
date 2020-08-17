# Guia de instalação do módulo Python Uncertainties

## Distribuições Linux (Debian e derivados)

Se você tem [pip](https://pypi.org/project/pip/), você pode instalar a versão mais recente com:

```pip install --upgrade uncertainties```

Se você tiver [setuptools](https://pypi.org/project/setuptools/), você poderá instalar/atualizar automaticamente este pacote 
com:

```easy_install --upgrade uncertainties```

## Windows

Para instalar este pacote com o [conda](https://pypi.org/project/pip/), execute um dos seguintes procedimentos no interpretador prompt de comando:

```conda install -c conda-forge uncertainties``` 

```conda install -c conda-forge/label/gcc7 uncertainties``` 

```conda install -c conda-forge/label/cf201901 uncertainties```

## MacOS

 Usuários que utilizam o gerenciador MacPorts podem instalar uncertainties utilizando:
 
 ```sudo port install py**-uncertainties```, onde ```**``` representa a versão do Python. 
 
# Inicialização do Python (módulos math e uncertainties)
 
### Carregando o módulo Python Uncertainties, que calcula a propagação de incertezas:

```python
>>> import uncertainties import *
```
 
## Definição de parâmetros e fórmulas com incertezas

### Use a função "ufloat" para definir números reais com incertezas:


```python
>>> a = ufloat(23.45, 0.12)
>>> print(a)
23.45+/-0.12
```

```python
 >>> b = ufloat(21.32, 0.21)
 >>> print(b)
21.32+/-0.21
```

```python
>>> c = a + b
>>> print("Resultado = {0:.2f}".format(c))
Resultado = 44.77+/-0.24
```

## Propagação de incertezas para um vetor/lista de valores

### Carregando o [sub-módulo unumpy do módulo Uncertainties](https://pythonhosted.org/uncertainties/numpy_guide.html) para lidar com vetor/lista de valores com incertezas:

```python
>>> from uncertainties import unumpy
```

### Usa-se a função unumpy.uarray() para criar lista de valores, seguida de uma lista de incertezas:

```python
>>> s1vetor = unumpy.uarray([4.45e-3, 2.67e-3, 3.56e-3], [0.05e-3, 0.05e-3, 0.05e-3])
>>> print(s1vetor)
[0.00445+/-5e-05 0.00267+/-5e-05 0.00356+/-5e-05]
```

```python
>>> t1vetor = unumpy.uarray([9.62e-3, 6.19e-3, 6.44e-3], [0.15e-3, 0.15e-3, 0.15e-3])
>>> print(t1vetor)
[0.00962+/-0.00015 0.00619+/-0.00015 0.00644+/-0.00015]
```

### Operações aritméticas simples são feitas normal e transparentemente com lista de valores com incertezas:

```python
>>> v1vetor = s1vetor + t1vetor
>>> for x in v1vetor:
>>>     print("{0:.2e}".format(x))
(1.41+/-0.02)e-02
(8.86+/-0.16)e-03
(1.00+/-0.02)e-02
```
